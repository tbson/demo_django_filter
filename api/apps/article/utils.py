from django.db import models
from .srs import CategoryBaseSr, ArticleBaseSr


class ArticleUtils:
    @staticmethod
    def seeding(index: int) -> models.QuerySet:
        for i in range(index):
            cateory_data = {
                'uid': "uid_{}".format(i),
                'title': "title {}".format(i),
            }
            category_sr = CategoryBaseSr(data=cateory_data)
            category_sr.is_valid(raise_exception=True)
            category = category_sr.save()

            if i == 0:
                article_data = {
                    'title': "title {}".format("NONE"),
                    'content': "content {}".format("NONE"),
                }
                article_sr = ArticleBaseSr(data=article_data)
                article_sr.is_valid(raise_exception=True)
                article_sr.save()
            else:
                for j in range(i):
                    article_data = {
                        'category': category.pk,
                        'title': "{}: title {}".format(category.uid, j),
                        'content': "{}: content {}".format(category.uid, j),
                    }
                    article_sr = ArticleBaseSr(data=article_data)
                    article_sr.is_valid(raise_exception=True)
                    article_sr.save()
