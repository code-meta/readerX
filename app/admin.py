from django.contrib import admin
from app.models import Post
from django import forms


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ["title"]
