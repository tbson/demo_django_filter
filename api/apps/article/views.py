from rest_framework.response import Response
from rest_framework.viewsets import (GenericViewSet, )
from .models import Article
from .srs import ArticleBaseSr
from .filters import ArticleFilter


class ArticleViewSet(GenericViewSet):
    filterset_class = ArticleFilter
    ordering_fields = ('id', 'category', )

    def list(self, request):
        queryset = Article.objects.all()
        queryset = self.filter_queryset(queryset)
        result = ArticleBaseSr(queryset, many=True).data
        return Response(result)
