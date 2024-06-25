from .models import *
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()


def get_books_by_genre(genre):
    return Book.objects.all().filter(book_genre=genre)


def get_book_by_id(book_id):
    return Book.objects.get(pk=book_id)


def get_all_books():
    return Book.objects.all()


def get_popular_books():
    all_books = get_all_books()
    all_books = [(str(book.id), len(book.views)) for book in all_books]
    all_books = dict(all_books)
    all_books_sorted = sorted(all_books.items(), key=lambda book: book[1], reverse=True)
    popular_books = [get_book_by_id(int(book_list[0])) for book_list in all_books_sorted]
    return popular_books


def is_new(user):
    return (user.detectives_count == 0 and
            user.fighters_count == 0 and
            user.romantics_count == 0 and
            user.fantasy_count == 0 and
            user.thrillers_count == 0)


def get_favorite_genre(user):
    """
        0 - Детективи
        1 - Бойовики
        2 - Романтика
        3 - Фентезі
        4 - Трилери
    """
    preferences = [user.detectives_count,
                   user.fighters_count,
                   user.romantics_count,
                   user.fantasy_count,
                   user.thrillers_count]
    return preferences.index(max(preferences))


def get_books_for_user(user):
    favorite_genre = get_favorite_genre(user)
    users_with_similar_preferences = []
    books = []
    # Отримуємо корисувачів зі схожими смаками
    for other_user in User.objects.all():
        if user.id != other_user.id:
            if not is_new(other_user):
                if get_favorite_genre(other_user) == favorite_genre:
                    users_with_similar_preferences.append(other_user)
    # Знаходимо книжки які вони переглядали, та рекомендуємо ті, що користувач не бачив
    if users_with_similar_preferences:
        for other_user in users_with_similar_preferences:
            for other_user_viewed_book in other_user.views_history:
                if other_user_viewed_book not in user.views_history:
                    books.append(get_book_by_id(other_user_viewed_book))
    else:
        books = get_popular_books()
    if not books:
        books = get_popular_books()
    return books


def get_books_by_search(search_request):
    return Book.objects.filter(Q(book_title__icontains=search_request) or Q(book_genre__icontains=search_request))


def get_auto_complete_data(search_request):
    return [book.book_title for book in get_books_by_search(search_request)[:5]]


def create_feedback(user, feedback_content, stars, book_id):
    new_feedback = Feedback(author=user, feedback_text=feedback_content, book=get_book_by_id(book_id), stars=stars)
    new_feedback.save()


def get_feedbacks_for_book(book_id):
    return Feedback.objects.all().filter(book=get_book_by_id(book_id))