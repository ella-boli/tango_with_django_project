from django.db import models

    # CharField: a field for storing character data
    # URLField for storing resource URLs
    # IntegerField stores integers
    # DateField stores a Python datetime.date object
    # each category name must be unique and be used the field as a primary key


class Category(models.Model):
    name = models.CharField(max_length=128, unique = True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0) 

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

