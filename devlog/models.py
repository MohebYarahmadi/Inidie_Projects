from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse  # Allow us to create our own URL

# from django.contrib.auth.models import User # import User model directly as FK

# better import User like this rather than importing User directly.
# This approach ensures compatibility, especially if a custom user model is used in the future.
from django.conf import settings
# or from django.contrib.auth import get_user_model

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     slug = models.SlugField(max_length=100, unique=True,
#                             blank=True, allow_unicode=True)
#
#     class Meta:
#         verbose_name_plural = 'categories'
#
#     def __str__(self):
#         return self.name
