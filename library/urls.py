from django.conf.urls import include, url
from django.contrib import admin

from views import IndexView, Copy_of_the_book_add, DeleteCopy_of_the_book, Reader_add, DeleteReader, Book_lending_add, DeleteBook_lending, Delay_add, DeleteDelay

urlpatterns = [
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^Copy_of_the_book', Copy_of_the_book_add.as_view()),
    url(r'^delete_book', DeleteCopy_of_the_book.as_view()),
    url(r'^Reader', Reader_add.as_view()),
    url(r'^delete_reader', DeleteReader.as_view()),
    url(r'^Book_lending', Book_lending_add.as_view()),
    url(r'^delete_lending', DeleteBook_lending.as_view()),
    url(r'^Delay', Delay_add.as_view()),
    url(r'^delete_delay', DeleteDelay.as_view())
]
