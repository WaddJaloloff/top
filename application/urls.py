from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('all-posts/', AllPostsView.as_view(), name='all_posts'),
]