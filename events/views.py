from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import EventPost, EventComment
from .forms import CommentForm


class EventsPage(generic.ListView):

    model = EventPost
    queryset = EventPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'events.html'
    paginate_by = 3


def event_post_page(request, slug, *args, **kwargs):

    queryset = EventPost.objects.filter(status=1)
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
        "eventpost.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
    )

# view used from PP4_masterclass blog


def event_post_like(request, slug, *args, **kwargs):

    post = get_object_or_404(EventPost, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('event_post', args=[slug]))

# delete comment view


def delete_comment_event(request, slug, comment_id, *args, **kwargs):
    comment = get_object_or_404(EventComment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('event_post', kwargs={"slug": slug}))

# edit view comment


def edit_comment_event(request, comment_id, *args, **kwargs):
    comment = get_object_or_404(EventComment, id=comment_id)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            return redirect('events')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'comment_form': comment_form})
