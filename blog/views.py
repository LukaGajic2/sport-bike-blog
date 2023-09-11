from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import BlogPost, BlogComment
from .forms import CommentForm


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


def blog_post_page(request, slug, *args, **kwargs):
    """
    A function-based view to view the detail of a post.
    Largely the same as the class-based, but we don't have
    different methods for GET and POST. Because it's not a
    class, all of the extra "self" stuff is removed too.

    Functionally, it's the same, but it is a bit clearer
    what's going on. To differentiate between request methods,
    we use request.method == "GET" or request.method == "POST"
    """

    queryset = BlogPost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    liked = False
    commented = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment awaiting moderation.')
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "post.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
    )


def blog_post_like(request, slug, *args, **kwargs):
    """
    The view to update the likes. Although it should always be
    called using the POST method, we have still added some
    defensive programming to make sure.
    """
    post = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post', args=[slug]))


def delete_comment(request, slug, comment_id, *args, **kwargs):
    comment = get_object_or_404(BlogComment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('post', kwargs={"slug": slug}))


'''
def edit_comment(request, comment_id, *args, **kwargs):
    comment = get_object_or_404(BlogComment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(data=request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return render(request, 'blog.html')
'''


def edit_comment(request, comment_id, *args, **kwargs):
    comment = get_object_or_404(BlogComment, id=comment_id)

    # Ensure the user can edit the comment (for example, they are the author or an admin)
    # Remove this check if not needed.
    if request.user != comment.author:
        messages.add_message(request, messages.ERROR,
                             'You do not have permission to edit this comment.')
        # Replace 'some_view_name' with a relevant view name or URL
        return redirect('some_view_name')

    if request.method == 'POST':
        form = CommentForm(data=request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            # Replace 'some_view_name' with where you want to redirect after successful update
            return redirect('some_view_name')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')
    else:
        # This is a GET request, so initialize the form with the comment instance
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form})
