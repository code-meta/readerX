from django.db import models
import uuid
from tinymce import models as tinymce_models

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thumbnail = models.ImageField(upload_to="uploads/")
    title = models.CharField(max_length=220)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField(max_length=320, blank=True)
    content = tinymce_models.HTMLField()
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Publish Date")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Last Updated")
