from django.shortcuts import render
from django.views.generic import View
from app.models import Post
from django.shortcuts import get_object_or_404


class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        latestPost = Post.objects.latest("created_at")
        return render(request, "app/home.html", {"posts": posts, "latestPost": latestPost, "page": "home"})


class SingleArticleView(View):
    def get(self, request, slugid):
        post = get_object_or_404(Post, slug=slugid)
        return render(request, "app/article.html", {"post": post})

class BlogView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "app/blog.html", {"posts": posts})
