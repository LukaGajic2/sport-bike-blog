from . import views
from django.urls import path


urlpatterns = [
    path('events/', views.EventsPage.as_view(), name='events'),
    path('<slug:slug>/', views.event_post_page, name='event_post'),
    path('like/<slug:slug>', views.event_post_like, name='event_post_like'),
    path('edit_comment/<int:comment_id>',
         views.edit_comment_event, name='edit'),
    path('<slug:slug>/delete/<int:comment_id>/',
         views.delete_comment_event, name='delete'),
]
