from django.shortcuts import render, redirect
from django.http import JsonResponse
from .controllers import *
import urllib.parse


def get_dict_books(books):
    books_json = {"books": {}}
    for book in books:
        book_id = book.id
        book_title = book.book_title
        book_image = book.book_image
        book_price = book.book_price
        book_author = book.book_author
        book_genre = book.book_genre
        book_url = book.book_url
        book_data = {"book_id": book_id,
                     "book_title": book_title,
                     "book_image": book_image,
                     "book_price": book_price,
                     "book_author": book_author,
                     "book_genre": book_genre,
                     "book_url": book_url}
        books_json["books"][f"book{book_id}"] = book_data
    return books_json


def render_main_page(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        return redirect("/auth/signup")


def render_book_page(request, book_id):
    if request.user.is_authenticated:
        book = get_book_by_id(book_id)
        if request.user.id not in book.views:
            if book.book_genre == "Бойовики":
                request.user.fighters_count += 1
            elif book.book_genre == "Детективи":
                request.user.detectives_count += 1
            elif book.book_genre == "Романтика":
                request.user.romantics_count += 1
            elif book.book_genre == "Трилери":
                request.user.thrillers_count += 1
            elif book.book_genre == "Фентезі":
                request.user.fantasy_count += 1
            request.user.save()
            book.add_view(request.user.id)
            request.user.add_view_log(book.id)
        return render(request, "book.html", context={"book": book})
    else:
        return redirect("/auth/signup")


def render_books_by_genre(request, books_genre):
    if request.user.is_authenticated:
        return render(request, "books_by_genre.html", context={"books_genre": books_genre})
    else:
        return redirect("/auth/signup")


def get_books_by_genre_json(request, books_genre, books_index):
    book_genre = urllib.parse.unquote(books_genre)
    books = get_books_by_genre(book_genre)
    if int(books_index) == 1:
        books = books[:45]
    else:
        books = books[(45 * int(books_index) - 45):45 * int(books_index)]
    return JsonResponse(get_dict_books(books))


def get_book_by_genre_samples_json(request, book_genre):
    books = get_books_by_genre(urllib.parse.unquote(book_genre))[:3]
    return JsonResponse(get_dict_books(books))


def render_books_for_user_page(request):
    if request.user.is_authenticated:
        return render(request, "books_for_user.html")
    else:
        return redirect("/auth/signup")


def get_books_samples_for_user_json(request):
    user = request.user
    if is_new(user):
        books = get_popular_books()[:3]
    else:
        books = get_books_for_user(user)[:3]
    return JsonResponse(get_dict_books(books))


def get_books_for_user_json(request, books_index):
    user = request.user
    if is_new(user):
        books = get_popular_books()
    else:
        books = get_books_for_user(user)
    if int(books_index) == 1:
        books = books[:45]
    else:
        books = books[(45 * int(books_index) - 45):45 * int(books_index)]
    return JsonResponse(get_dict_books(books))


def search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form_data = request.POST.dict()
            search_request = form_data["searchRequest"]
            if search_request not in request.user.search_history:
                if len(request.user.search_history) == 5:
                    request.user.search_history.remove(request.user.search_history[-1])
                request.user.search_history.insert(0, search_request)
                request.user.save()
            return render(request, "books_by_search.html", context={"search_request": search_request})
        return redirect("/")
    else:
        return redirect("/auth/signup")


def get_books_by_search_json(request, search_request, books_index):
    books = get_books_by_search(urllib.parse.unquote(search_request))
    if int(books_index) == 1:
        books = books[:45]
    else:
        books = books[(45 * int(books_index) - 45):45 * int(books_index)]
    return JsonResponse(get_dict_books(books))


def clear_search_history(request):
    request.user.search_history.clear()
    request.user.save()
    return redirect("/")


def get_search_history(request):
    search_history = {"search_history": request.user.search_history}
    return JsonResponse(search_history)


def get_auto_complete_data_json(request, search_request):
    auto_complete_data = {"auto_complete_data": get_auto_complete_data(urllib.parse.unquote(search_request))}
    return JsonResponse(auto_complete_data)


def write_feedback(request, book_id):
    if request.method == "POST":
        form_data = request.POST.dict()
        feedback_content = form_data["feedbackContent"]
        stars = form_data["rating"]
        create_feedback(request.user, feedback_content, int(stars), book_id)
        return redirect(f"/book/{book_id}")
    return redirect(f"/book/{book_id}")


def get_feedbacks_for_book_json(request, book_id):
    feedbacks_json = {"feedbacks": {}}
    feedbacks = get_feedbacks_for_book(book_id)

    for feedback in feedbacks[::-1]:
        feedback_id = feedback.id
        feedback_author = feedback.author.username
        feedback_stars = feedback.stars
        feedback_text = feedback.feedback_text

        feedback_data = {
            "feedback_id": feedback_id,
            "feedback_author": feedback_author,
            "feedback_stars": feedback_stars,
            "feedback_text": feedback_text
        }

        feedbacks_json["feedbacks"][f"feedback{feedback_id}"] = feedback_data
    return JsonResponse(feedbacks_json)


def render_favorite_page(request):
    return render(request, "favorite_books.html")


def get_favorite_books_json(request, books_index):
    books = [get_book_by_id(book_id) for book_id in request.user.favorite_books][::-1]
    if int(books_index) == 1:
        books = books[:45]
    else:
        books = books[(45 * int(books_index) - 45):45 * int(books_index)]
    return JsonResponse(get_dict_books(books))


def add_to_favorite(request, book_id):
    if book_id not in request.user.favorite_books:
        request.user.favorite_books.append(book_id)
        json_response = {"if_favorite": 1}
    else:
        request.user.favorite_books.remove(book_id)
        json_response = {"if_favorite": 0}
    request.user.save()
    return JsonResponse(json_response)


def if_favorite_json(request, book_id):
    if book_id in request.user.favorite_books:
        json_response = {"if_favorite": 1}
    else:
        json_response = {"if_favorite": 0}
    return JsonResponse(json_response)
# def add_test_data(request):
#     import csv; import os;
#     if not os.path.exists("test_data/status.txt"):
#         genres = ["Бойовики", "Детективи", "Романтика", "Трилери", "Фентезі"]
#         for genre in genres:
#             with open(fr"C:\Users\tvtes\AppData\Local\Programs\Python\workspace\Portfolio_Projects\Project_1\blog\test_data\{genre}.csv", "r", encoding="utf-8") as books:
#                 books = list(csv.reader(books))[1:]
#                 for row in books:
#                     print(row)
#                     book_title = row[0]
#                     book_image = row[1]
#                     book_price = row[2]
#                     book_author = row[3]
#                     book_genre = genre
#                     book_url = row[5]
#                     print(book_genre)
#                     new_book = Book(book_title=book_title,
#                                     book_image=book_image,
#                                     book_price=book_price,
#                                     book_author=book_author,
#                                     book_genre=book_genre,
#                                     book_url=book_url)
#                     new_book.save()
#     else:
#         print("Data is already in database.")
#     return redirect("/")