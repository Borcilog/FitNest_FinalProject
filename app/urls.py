from django.urls import path
from .views import (HomePageView, AboutPageView, LoginPageView, LogoutPageView, BlogListView, 
                    BlogDetailView,BlogCreateView,BlogUpdateView,
                    BlogDeleteView,VideoCreateView,VideoListView,TrainerListView,
                    TrainerDetailView,ClassCategoryListView,ClassCategoryDetailView )
from . import views

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('accounts/login/', LoginPageView.as_view(), name='login'),
    path('accounts/logout/', LogoutPageView.as_view(), name='logout'),
    
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    
    path('videos/', VideoListView.as_view(), name='videos'),
    path('video/Upload', VideoCreateView.as_view(), name='video_list'),
    
    path("plans/", views.MembershipPlanListView, name="membership_plan_list"),
    
    path('trainers/', TrainerListView.as_view(), name='trainer_list'),
    path('trainers/<int:pk>/', TrainerDetailView.as_view(), name='trainer_detail'),    
    
    path("categories/", ClassCategoryListView.as_view(), name="class_category_list"),
    path('categories/<int:pk>/', ClassCategoryDetailView.as_view(), name='class_category_detail'),
    
    path('schedule/', views.schedule_view, name='schedule'),
    path('schedule/success/', views.schedule_success, name='schedule_success'),
    
    
]