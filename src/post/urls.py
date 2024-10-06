from django.urls import path
from .views import BlogHome, BlogPostCreateView, BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView


app_name = "post"
urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('create/',BlogPostCreateView.as_view(), name='create'),
    path('edit/<str:slug>/', BlogPostUpdateView.as_view() , name='edit'),
    path('delete/<str:slug>/', BlogPostDeleteView.as_view() , name='delete'),
    path('<str:slug>/', BlogPostDetailView.as_view() , name='posts'),
]
