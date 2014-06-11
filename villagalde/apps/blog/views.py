from django.shortcuts import render, render_to_response
from villagalde.apps.blog.models import Post

# Create your views here.

def tagpage(request, tag):
	posts=Post.objects.filter(tags__name=tag)
	return render_to_response("blog/tagpage.html",{"posts":posts, "tag":tag })