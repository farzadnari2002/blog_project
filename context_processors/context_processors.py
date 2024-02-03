from blog_app.models import Article



def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')[0:3]
    return {'recent_articles':recent_articles}