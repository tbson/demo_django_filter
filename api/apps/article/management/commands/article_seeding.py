from django.core.management.base import BaseCommand
from apps.article.utils import ArticleUtils


class Command(BaseCommand):
    help = 'Seeding categories and articles'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start...'))
        ArticleUtils.seeding(10)
        self.stdout.write(self.style.SUCCESS('Done!!!'))
