from django_filters import rest_framework as filters
from .models import Article


class ArticleFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category_id')
    category_uid = filters.CharFilter(field_name='category__uid')

    class Meta:
        model = Article
        fields = {
            'category': ['exact', 'isnull'],
            'category_uid': ['exact'],
        }
