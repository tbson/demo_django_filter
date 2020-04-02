import os
from django.urls import path
from .views import (
    ArticleViewSet,
)


BASE_ENDPOINT = ArticleViewSet.as_view({
    'get': 'list',
})

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path('', BASE_ENDPOINT),
]
