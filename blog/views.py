from django.shortcuts import render


def index(req):

    return render(req, "blog/index.html")


def posts(req):
    return render(req, "blog/all-posts.html")


def post_detail(req, slug):
    return render(req, "blog/post-detail-page.html", )
