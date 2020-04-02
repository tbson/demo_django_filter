from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.validators import UniqueValidator
from .models import Category, Article


class CategoryBaseSr(ModelSerializer):

    class Meta:
        model = Category
        exclude = ()
        read_only_fields = ('id',)

    uid = CharField(validators=[
        UniqueValidator(
            queryset=Category.objects.all(),
            message="Duplicate category",
        )
    ])


class ArticleBaseSr(ModelSerializer):

    class Meta:
        model = Article
        exclude = ()
        read_only_fields = ('id',)
