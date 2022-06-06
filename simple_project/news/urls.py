from django.urls import path
from. import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(views.News_home.as_view()), name = 'news_home'),#path('',views.News_home.as_view(), name = 'news_home')
    path('create',views.Addpage.as_view(), name = 'create'),
    path('login',views.LoginUser.as_view(), name = 'login'),
    path('logout',views.logout_user, name = 'logout'),
    path('register',views.RegisterUser.as_view(), name = 'register'),
    path('category', views.category, name='category'),#/<int:cat_id>/
    path('contact', views.ContactFormView.as_view(), name='contact'),
    path('<slug:detail_slug>',views.NewsDetailView.as_view(), name = 'news-detail'),#/news/1 2 3
    path('<slug:update_slug>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<slug:del_slug>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('category/<slug:cat_slug>/', views.show_category.as_view(), name='category_show'),

]


