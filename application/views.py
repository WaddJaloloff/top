from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name='index.html'
    context_object_name = 'posts'  # object_list o'rniga posts ishlatamiz

    def get_queryset(self):
        return Post.objects.all()[:8] 
    

class AllPostsView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()[8:] 