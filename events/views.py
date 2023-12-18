from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import EventPost, EventComment
from .forms import CommentForm


class EventsPage(generic.ListView):
    """
    View for blog page.
    """
    model = EventPost
    queryset = EventPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'events.html'
    paginate_by = 3


def event_post_page(request, slug, *args, **kwargs):

    queryset = EventPost.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    event_comments = event.comments.filter(approved=True).order_by("-created_on")
    event_comment_count = event.comments.filter(approved=True).count()
    liked = False
    commented = False

    if event.likes.filter(id=request.user.id).exists():
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
        "events.html",
        {
            "event": event,
            "comments": event_comments,
            "comment_count": event_comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
    )


def event_post_like(request, slug, *args, **kwargs):
    event = get_object_or_404(EventPost, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

    return HttpResponseRedirect(reverse('event', args=[slug]))

# delete comment view


def delete_comment(request, slug, comment_id, *args, **kwargs):
    event_comment = get_object_or_404(EventComment, id=comment_id)
    event_comment.delete()
    return HttpResponseRedirect(reverse('event', kwargs={"slug": slug}))

# edit view comment


def edit_comment(request, comment_id, *args, **kwargs):
    event_comment = get_object_or_404(EventComment, id=comment_id)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            return redirect('event')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'edit_event_comment.html', {'comment_form': comment_form})
