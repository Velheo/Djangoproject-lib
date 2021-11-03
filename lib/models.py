from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    def get_absolut_url(self):
        return reverse('lib:genre_detail', args=(self.id,))


    class Meta:
        ordering=["name"]
class Author(models.Model):
    first=models.CharField(max_length=50)
    last=models.CharField(max_length=50)
    year=models.IntegerField(default=0)
    img=models.URLField(blank=True, null=True)
    def __str__(self):
        return self.first+' '+self.last
    def get_absolute_url(self):
        return reverse('lib:author_detail', args=(self.id,))

    def get_genres(self):
        genres = []
        for book in self.book_set.all():
            for genre in book.genre.all():
                genres.append(genre)
        return list(set(genres))

    class Meta:
        ordering=["last"]
class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary=models.TextField(blank=True, null=True)
    genre=models.ManyToManyField(Genre)
    img = models.URLField(blank=True, null=True)
    def __str__(self):
        return f'"{self.title}"'
    def genres_str(self):
        return ', '.join(genre.name for genre in self.genre.all())
    def get_absolute_url(self):
        return reverse('lib:book_detail', args=(self.id,))

    class Meta:
        ordering=["title"]

class BookInstance(models.Model):
    book=models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    LOAN_STATUSES=(
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('o', 'On Loan'),
    )
    status=models.CharField(max_length=1, choices=LOAN_STATUSES, default='a')
    due_back=models.DateField(null=True, blank=True)
    def __str__(self):
        return f'{self.book} id={self.id} status={self.status}'


# Create your models here.
