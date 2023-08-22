from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import BlogPost


def about_page(request):
    """
    View for about page.
    """
    return render(request, "about.html")


# Class used from "I think therefore I blog" walkthrough.
class BlogPage(generic.ListView):
    """
    View for blog page.
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


# Class used from "I think therefore I blog" walkthrough.
class BlogPostPage(View):
    """
    To render the individual blog post
    as a singular web page to the browser.
    """
    