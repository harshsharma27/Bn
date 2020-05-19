from django.shortcuts import render, HttpResponse
from blog.models import Post
from blog.models import Author


# Create your views here.
def blogHome(request):
    # return HttpResponse('This is bloghome. We will keep all the blog post')
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first
    context = {'post': post}

    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f'This is blogPost: {slug}')


def abou(request):
    ab = Author.objects.all()
    context = {'ab': ab}
    return render(request, 'blog/abou.html', context)