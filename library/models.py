__author__ = 'user'

from django.db import models

class Copy_of_the_book(models.Model):
    fio_author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    publishing_house = models.CharField(max_length=20)
    imprint_date = models.PositiveIntegerField()

class Reader(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=30)

class Book_lending (models.Model):
    id_book = models.ForeignKey(Copy_of_the_book)
    id_reader = models.ForeignKey(Reader)
    date_of_issue = models.DateField()
    return_date = models.DateField(default=False)
    expected_return_date = models.DateField()
    delay_of_book = models.PositiveIntegerField()

class Delay (models.Model):
    id_lending = models.ForeignKey(Book_lending)
    payment = models.BooleanField(default=False)

##Copy_of_the_book.objects.create(fio_author="Robert Shtilmark", title="Heir from Calcutta", genre="adventure", publishing_house="BMM", imprint_date=2014)
##Reader.objects.create(surname="Berezkin", name="Constantine", patronymic="Petrovich", dob='13.05.93', address="Pushkin street 66")
##Book_lending.objects.create(id_book=1, id_reader=1, date_of_issue='1.05.15', return_date='11.05.15', expected_return_date='15.05.15', delay_of_book=0)
##Delay.objects.create(id_lending=1, payment='False')






