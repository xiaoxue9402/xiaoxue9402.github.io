from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    url = models.TextField()

    @classmethod
    def create(cls, title, author):
        book = cls(title=title, author=author)
        if author:
            first_name = author.split()[0]
            last_name = author.split()[1]
            base_url = f'https://github.com/xiaoxue9402/epubfiles/blob/main/{title}' + f'%20by%20{first_name}%20{last_name}' + '.epub?raw=true'

            url = base_url
        else:
            url = f'https://github.com/xiaoxue9402/epubfiles/blob/main/{title}.epub?raw=true'
