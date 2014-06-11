from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from villagalde.apps.blog.models import Post
from django.contrib.syndication.views import Feed


class BlogFeed(Feed):
	title = "Mysite"
	description = "Some ramblings of mine"
	link = "/blog/feed/"

	def items(self):
		return Post.objects.all().order_by("-create")[:2]
	def item_title(self, item):
		return item.title
	def item_description(self, item):
		return item.body
	def item_link(self, item):
		return u"/blog/%d" % item.id




urlpatterns = patterns(
	'villagalde.apps.blog.views',
    url(r'^$', ListView.as_view(
    	queryset=Post.objects.all().order_by("-create")[:2],
    	template_name="blog/blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
    	model=Post,
    	template_name="blog/post.html")),
    url(r'^archives/$', ListView.as_view(
    	queryset=Post.objects.all().order_by("-create"),
    	template_name="blog/archives.html")),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', BlogFeed()),
)