from django.shortcuts import render, get_object_or_404
from diary.models import Post
from diary.forms import PostForm
from django.http import HttpResponseRedirect
import datetime
# Create your views here.

def index(request):
    objects = []
    for object in Post.objects.all():
       objects.append(object)
    return render(request, 'diary/index.html', {'objects':objects})


def post(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Submit':
            form = PostForm(request.POST)
            if form.is_valid():
                form.clean_data()
                object = Post(author=form.author,title=form.title,content=form.content,date=datetime.datetime.now())
                object.save()
                return HttpResponseRedirect('/diary/')
    else:
        form = PostForm()
    return render(request, 'diary/post.html',{'form':form})

def archive(request):
     list_posts =getposts()
     return render(request, 'diary/archive.html',{'list':list_posts})

def detail(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    if request.method == 'POST':
        if request.POST['action'] == 'Delete':
            post.delete()
            return HttpResponseRedirect('/diary/')
    return render(request, 'diary/detail.html', {'post': post})

def getposts():
    posts = Post.objects.filter().order_by('-date')
    if not posts:
        return []
    posts_dict = {}
    for i in range(posts[0].date.year, posts[len(posts)-1].date.year-1, -1):
        posts_dict[i] = {}
        for month in range(1,13):
            posts_dict[i][month] = []
    for post in posts:
        posts_dict[post.date.year][post.date.month].append(post)
    post_sorted_keys = list(reversed(sorted(posts_dict.keys())))
    list_posts = []
    for key in post_sorted_keys:
        adict = {key:posts_dict[key]}
        list_posts.append(adict)
    return list_posts
