from django.db import models


# generate sql -> python manage.py makemigrations ->  pdfs/migrations/0001_initial.py
# run sql on db -> python manage.py migrate
class Pdf(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    pages = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_created=True)
