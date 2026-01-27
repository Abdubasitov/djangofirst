from django.shortcuts import render, get_object_or_404
from news.models import News, Category, Comment
from django.shortcuts import redirect

def homepage(request):
	news_all = News.objects.all()
	categories = Category.objects.filter(news__isnull=False).distinct()
	context = {
		'news_all':news_all,
		'categories':categories,
	}
	return render(request, 'index.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    categories = Category.objects.filter(news__isnull=False).distinct()
    
    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")

        if name and text:
            Comment.objects.create(
                news=news,
                name=name,
                text=text
            )
        return redirect(request.path)

    comments = news.comments.all()

    return render(request, 'single-page.html', {
        'news': news,
        'categories': categories,
        'comments': comments,
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news_list = News.objects.filter(category=category)
    categories = Category.objects.filter(news__isnull=False).distinct()

    return render(request, 'category-page.html', {
        'category': category,
        'news_list': news_list,
        'categories': categories,
    })

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.method == "POST":
        comment.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))