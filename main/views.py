from django.shortcuts import get_object_or_404, render

from .models import Post, Project


SOCIAL_LINKS = {
    'github': 'https://github.com/mahmudovah',
    'telegram': 'https://t.me/nrs_20257',
    'linkedin': 'https://linkedin.com/in/hadija-mahmudova-108332348/',
}


def home(request):
    projects = Project.objects.all()[:3]
    posts = Post.objects.all()[:3]
    return render(
        request,
        'main/home.html',
        {
            'projects': projects,
            'posts': posts,
            'social_links': SOCIAL_LINKS,
        },
    )


def about(request):
    return render(request, 'main/about.html', {'social_links': SOCIAL_LINKS})


def projects(request):
    items = Project.objects.all()
    return render(
        request,
        'main/projects.html',
        {
            'projects': items,
            'social_links': SOCIAL_LINKS,
        },
    )


def blog_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'main/blog_list.html',
        {
            'posts': posts,
            'social_links': SOCIAL_LINKS,
        },
    )


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        'main/blog_detail.html',
        {
            'post': post,
            'social_links': SOCIAL_LINKS,
        },
    )
