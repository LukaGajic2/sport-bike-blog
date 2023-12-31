from . import views
from django.urls import path


urlpatterns = [
    path('', views.about_page, name='about'),
    path('blog/', views.BlogPage.as_view(), name='blog'),
    path('like/<slug:slug>', views.blog_post_like, name='post_like'),
    path('edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('<slug:slug>/', views.blog_post_page, name='post'),
]
