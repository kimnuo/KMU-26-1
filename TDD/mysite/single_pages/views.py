from django.shortcuts import render
from blog.models import Category, Post, Tag

# Create your views here.
def landing(request):
    return render(
        request,
        "single_pages/landing.html",
        {
            "categories": Category.objects.all(),
            "no_category_post_count": Post.objects.filter(category=None).count(),
            "post_count": Post.objects.count(),
            "category_count": Category.objects.count(),
            "tag_count": Tag.objects.count(),
            "recent_posts": Post.objects.order_by("-pk")[:3],
        },
    )

def about_me(request):
    return render(request, 'single_pages/about_me.html')