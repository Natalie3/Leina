# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView, View
from django.shortcuts import redirect
from models import Reader, Copy_of_the_book, Book_lending, Delay
#from django.contrib import admin

#copy_of_the_book_list = Copy_of_the_book.objects.all()
#book_lending_list = Book_lending.objects.all()
#delay_list = Delay.objects.all()

class Copy_of_the_book_add(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
      fio_author_value = self.request.POST['fio_author']
      title_value = self.request.POST['title']
      genre_value = self.request.POST['genre']
      publishing_house_value = self.request.POST['publishing_house']
      imprint_date_value = self.request.POST['imprint_date']
      Copy_of_the_book.objects.create(
          fio_author=fio_author_value,
          title=title_value,
          genre=genre_value,
          publishing_house=publishing_house_value,
          imprint_date=imprint_date_value)
      return  redirect('/')


class DeleteCopy_of_the_book(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        book_delete = self.request.POST['delete_book']
        Copy_of_the_book.objects.filter(id=int(book_delete)).delete()
        return redirect('/')


class Reader_add(View):
    template_name = "index.html"

    def post(self, *args,**kwargs):
        surname_value = self.request.POST['surname']
        name_value = self.request.POST['name']
        patronymic_value = self.request.POST['patronymic']
        dob_value = self.request.POST['dob']
        address_value = self.request.POST['address']
        Reader.objects.create(
            surname=surname_value,
            name=name_value,
            patronymic=patronymic_value,
            dob=dob_value,
            address=address_value
        )
        return redirect('/')


class DeleteReader(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        reader_delete = self.request.POST['delete_reader']
        Reader.objects.filter(id=int(reader_delete)).delete()
        return redirect('/')


class Book_lending_add(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        id_book_value = self.request.POST['id_book']
        id_reader_value = self.request.POST['id_reader']
        date_of_issue_value = self.request.POST['date_of_issue']
        return_date_value = self.request.POST['return_date']
        expected_return_date_value = self.request.POST['expected_return_date']
        delay_of_book_value = self.request.POST['delay_of_book']
        Book_lending.objects.create(
            id_book=Copy_of_the_book.objects.filter(id=int(id_book_value))[0],
            id_reader=Reader.objects.filter(id=int(id_reader_value))[0],
            date_of_issue=date_of_issue_value,
            return_date=return_date_value,
            expected_return_date=expected_return_date_value,
            delay_of_book=delay_of_book_value
        )
        return redirect('/')


class DeleteBook_lending(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        lending_delete = self.request.POST['delete_lending']
        Book_lending.objects.filter(id=int(lending_delete)).delete()
        return redirect('/')


class Delay_add(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        id_lending_value = self.request.POST['id_lending']
        payment_value = self.request.POST['payment']
        Delay.objects.create(
            id_lending=Book_lending.objects.filter(id=int(id_lending_value))[0],
            payment=payment_value
        )
        return redirect('/')


class DeleteDelay(View):
    template_name = "index.html"

    def post(self, *args,  **kwargs):
        delay_delete = self.request.POST['delete_delay']
        Delay.objects.filter(id=int(delay_delete)).delete()
        return redirect('/')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        reader_list = Reader.objects.all()
        copy_of_the_book_list = Copy_of_the_book.objects.all()
        book_lending_list = Book_lending.objects.all()
        delay_list = Delay.objects.all()
        context.update(
            {
                'reader_list': reader_list,
                'copy_of_the_book_list': copy_of_the_book_list,
                'book_lending_list': book_lending_list,
                'delay_list': delay_list,
            }
        )
        return context
