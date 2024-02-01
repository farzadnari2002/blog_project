from django.db import models


class ArticleManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(title='python')
    
    def counter(self):
        return len(self.all())
    
    def statustrue(self):
        return self.filter(status=True)