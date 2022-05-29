from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core import paginator
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .models import Articles
from .models import Category
from .forms import ArticlesForm, RegisterUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView  # Динамически изменяемые страницы
# Create your views here.


# def news_home(request):
#     news = Articles.objects.order_by('-date')  # order_by('date')[:1](сколько записей)
#     paginator = Paginator(news,2)
#
#     page_number = request.GET.get('page')
#     page_obj =paginator.get_page(page_number)
#     return render(request, 'news/news_home.html',{'page_obj': page_obj,'news': news})
class News_home(ListView):
    paginate_by = 2
    model = Articles
    template_name = 'news/news_home.html'
    context_object_name = 'news'

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'
    slug_url_kwarg = 'detail_slug'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
    slug_url_kwarg = 'update_slug'


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'
    slug_url_kwarg = 'del_slug'

class Addpage(LoginRequiredMixin,CreateView):
    form_class = ArticlesForm
    template_name = 'news/create.html'
    login_url = '/admin' #login_url = reverse_lazy

# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else:
#             error = 'Форма была не верна'
#     form = ArticlesForm()
#     data = {
#         'form': form,
#         'error': error,
#     }
#     return render(request, 'news/create.html', data)

def category(request):
    cats = Category.objects.all()
    data = {
        'cats': cats,
        'cat_selected':0,
    }
    return render(request, 'news/category.html',data)

class show_category(ListView):
    paginate_by = 2
    model = Articles
    template_name = 'news/news_home.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Articles.objects.filter(cat__slug=self.kwargs['cat_slug'])
# def show_category(request, cat_slug):
#     news = Articles.objects.filter(cat__slug=self.kwargs['cat_slug'])
#     return render(request, 'news/news_home.html',{'news': news})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'news/register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    Template_name = 'news/login.html'