from django.urls import path
from app.views import HomeView, SingleArticleView, BlogView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/<slug:slugid>/", SingleArticleView.as_view(), name="article"),
]
