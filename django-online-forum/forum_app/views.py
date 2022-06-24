from django.shortcuts import redirect, render, reverse
from .models import *


def index(request):
    my_data = {
        "posts": all_posts
    }
    return render(request, 'pages/index.html', my_data)


def new_post(request):
    if request.method == "POST":
        new_post = Post(request.POST['title'], request.POST['author'], request.POST['body'])
        Post.add_post(new_post)
        return redirect(reverse('post_details', args=(new_post.id,)))
    return render(request, 'pages/add_post.html')


def post_details(request, post_id):
    my_data = {
        'post': None
    }
    for this_post in all_posts:
        if this_post.id == post_id:
            my_data['post'] = this_post
            break

    if request.method == 'POST':
        new_comment = Comment(post_id, request.POST['author'], request.POST['body'])
        my_data['post'].add_comment(new_comment)
    return render(request, "pages/post_details.html", my_data)
