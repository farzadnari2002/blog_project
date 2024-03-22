from blog_app.models import Article, Category
from contacts_app.models import Contact


def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')[0:3]
    return {'recent_articles':recent_articles}



def categories(request):
    categories = Category.objects.all()
    return {"categories":categories}


def contacts(request):
    contacts = Contact.objects.all().first()
    return {'contacts':contacts}
    