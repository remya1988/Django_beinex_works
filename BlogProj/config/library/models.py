from django.db import models

# Create your models here.
class Author(models.Model):
    author_name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_title=models.CharField(max_length=100)
    book_author=models.ForeignKey(Author,on_delete=models.CASCADE)
    summary=models.TextField(null=True)
    published_date=models.DateField(auto_now_add=True)



