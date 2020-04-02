from django.db import models


class Category(models.Model):
    uid = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=250)

    def __str__(self):
        return '{} = {}'.format(self.uid, self.title)

    class Meta:
        db_table = "categories"
        ordering = ['-id']


class Article(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        category = self.category
        if category is None:
            return '{}'.format(self.title)
        return '{}: {}'.format(self.category.title, self.title)

    class Meta:
        db_table = "articles"
        ordering = ['-id']
