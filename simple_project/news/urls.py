from django.urls import path
from. import views

urlpatterns = [
    path('',views.News_home.as_view(), name = 'news_home'),#path('',views.News_home.as_view(), name = 'news_home')
    path('create',views.Addpage.as_view(), name = 'create'),
    path('category', views.category, name='category'),#/<int:cat_id>/
    path('<slug:detail_slug>',views.NewsDetailView.as_view(), name = 'news-detail'),#/news/1 2 3
    path('<slug:update_slug>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<slug:del_slug>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('category/<slug:cat_slug>/', views.show_category.as_view(), name='category_show'),

]


