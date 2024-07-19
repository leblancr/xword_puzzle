from django.db import models

# Create your models here.
class Clue(models.Model):
    entry = models.TextField()
    puzzle = models.TextField()
    clue_text = models.TextField()
    theme = models.BooleanField(default=False)

class Entry(models.Model):
    entry_text = models.TextField(max_length=50)

class Puzzle(models.Model):
    title = models.TextField(max_length=255)
    date = models.DateField()  # required (publication date)
    byline = models.TextField(max_length=255)
    publisher = models.TextField(max_length=12)


