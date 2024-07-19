from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import PostCreateForm

class IndexView(generic.ListView):
    model=Post
    
class CreateView(generic.CreateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('twitter:index')
    
class DetailView(generic.DetailView):
    model=Post