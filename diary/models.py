from django.db import models

class Diary(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to = "diary/", blank = True, null = True)


    def __str__(self):
        return self.title
