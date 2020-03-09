from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('it\'s index page')


def archive(request, article_number):
    return HttpResponse(f"This is archive of article number {article_number}")


def article(request):
    return HttpResponse("article page")


def article_num(request, article_number):
    return HttpResponse(f"Number of this article is {article_number}")


def users(request):
    return HttpResponse("uses page")


def user_identification(request, user_id):
    return HttpResponse(f"You are user number {user_id}")
