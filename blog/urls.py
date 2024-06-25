from django.urls import path
from .views import render_main_page, render_book_page, get_book_by_genre_samples_json, \
    get_books_samples_for_user_json, get_books_by_genre_json, render_books_by_genre, search, \
    clear_search_history, get_search_history, get_books_by_search_json, get_auto_complete_data_json, \
    get_books_for_user_json, render_books_for_user_page, write_feedback, get_feedbacks_for_book_json, \
    render_favorite_page, get_favorite_books_json, add_to_favorite, if_favorite_json

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('book/<int:book_id>', render_book_page, name="render_book_page"),
    path('books_for_user', render_books_for_user_page, name="render_books_for_user_page"),
    path('get_book_samples/<str:book_genre>', get_book_by_genre_samples_json, name="get_book_samples"),
    path('get_books_samples_for_user', get_books_samples_for_user_json, name="get_books_samples_for_user_json"),
    path('get_books_for_user/<int:books_index>', get_books_for_user_json, name="get_books_for_user_json"),
    path('get_books_by_genre/<str:books_genre>/<int:books_index>', get_books_by_genre_json, name="get_books_by_genre"),
    path('books/<str:books_genre>', render_books_by_genre, name="render_books_by_genre"),
    path("search", search, name="search"),
    path("get_books_by_search/<str:search_request>/<int:books_index>", get_books_by_search_json, name="get_books_by_search_json"),
    path("clear_search_history", clear_search_history, name="clear_search_history"),
    path("get_search_history", get_search_history, name="get_search_history"),
    path("get_auto_complete_data/<str:search_request>", get_auto_complete_data_json, name="get_auto_complete_data_json"),
    path("write_feedback/<int:book_id>", write_feedback, name="write_feedback"),
    path("get_feedbacks_for_book/<int:book_id>", get_feedbacks_for_book_json, name="get_feedbacks_for_book_json"),
    path("favorite", render_favorite_page, name="render_favorite_page"),
    path("get_favorite_books/<int:books_index>", get_favorite_books_json, name="get_favorite_books_json"),
    path("add_to_favorite/<int:book_id>", add_to_favorite, name="add_to_favorite"),
    path("if_favorite/<int:book_id>", if_favorite_json, name="if_favorite_json")
    # path("add_test_data", add_test_data, name="add_test_data")
]