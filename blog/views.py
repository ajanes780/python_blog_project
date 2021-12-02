from django.shortcuts import render

# Create your views here.


def index(responce):

    return render(responce, "blog/index.html")


def posts(reg):
    pass


def post_detail(req):
    pass
