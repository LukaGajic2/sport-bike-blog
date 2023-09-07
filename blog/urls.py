from . import views
from django.urls import path


urlpatterns = [
    path('', views.about_page, name='about'),
    path('blog/', views.BlogPage.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogPostPage.as_view(), name='post'),
    path('like/<slug:slug>', views.BlogPostLike.as_view(), name='post_like'),
]
