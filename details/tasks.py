from celery import shared_task
from time import sleep
from .models import Author, Book
from django.db import transaction

@shared_task
def add():
    author=Author(first_name="salam1",last_name="khobi")
    author.save()
@shared_task
def update():
    author=Author.objects.last()
    sleep(10)
    author.first_name="salam"+str(int(author.first_name[len(author.first_name)-1])+1)
    author.save()
    return author.first_name
@shared_task
def get(i):
    author=Author.objects.get(id=i)
    return author.first_name
@shared_task
def updateW():
    with transaction.atomic():
        author=Author.objects.select_for_update(nowait=True).last()
        sleep(20)
        author.first_name="salam"+str(int(author.first_name[len(author.first_name)-1])+1)
        author.save()
        return author.first_name
@shared_task
def getB():
    book=Book.objects.select_related('author').last()
    return book.name