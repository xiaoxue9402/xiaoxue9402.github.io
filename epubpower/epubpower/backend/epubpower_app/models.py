from django.db import models

# Create your models here.
base_url = f'https://github.com/xiaoxue9402/epubfiles/blob/main/{title}' + f'%20by%20{first_name}%20{last_name}' + '.epub?raw=true'
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    url = models.CharField()
    if author:
        first_name = author.split()[0]
        last_name = author.split()[1]
        url = base_url
    else:
        url = f'https://github.com/xiaoxue9402/epubfiles/blob/main/{title}.epub?raw=true'
