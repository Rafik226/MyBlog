from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from post.models import BlogPost

# Create your views here.
class BlogHome(ListView):
    model = BlogPost
    template_name = "post/blog_post_list.html"
    context_object_name = 'posts'

    def get_queryset(self):
        Queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return Queryset
        return Queryset.filter(published= True)

    
@method_decorator(login_required, name='dispatch')
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "post/blogpost_create.html"
    fields = ['title', 'content','published' ]

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "post/blogpost_edit.html"
    fields = ['title', 'content','published' ]

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "post/blogpost_detail.html"
    context_object_name = 'posts'


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "post/blogpost_delete.html"
    context_object_name = 'post'
    success_url = reverse_lazy('post:home')
