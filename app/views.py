from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post,Video, MembershipPlan,Trainer, ClassCategory, Schedule
from django.contrib.auth.models import User
from .forms import CustomLoginForm, ScheduleForm, VideoForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class LoginPageView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy('home') 

class LogoutPageView(LogoutView):
    next_page = reverse_lazy('home')

class HomePageView(TemplateView):
    template_name = "app/home.html"

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'author', 'body', 'header_image']
    template_name = 'app/blog_create.html'

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'author', 'body', 'header_image']
    template_name = 'app/blog_update.html'

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog')

class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'app/video_list.html'
    context_object_name = 'videos'

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'app/video.html'
    success_url = reverse_lazy('video_list')  


class MembershipPlanListView(LoginRequiredMixin, ListView):
    model = None  # No model, because we are using a hardcoded list.
    template_name = 'app/membership_plan_list.html'
    context_object_name = 'plans'

    def get_queryset(self):
        # Returning the hardcoded list of plans
        return [
            {"name": "Basic Plan", "description": "Access to gym and basic facilities.", "price": 20},
            {"name": "Premium Plan", "description": "Includes personal trainer and premium facilities.", "price": 50},
            {"name": "VIP Plan", "description": "All-inclusive access with extra perks.", "price": 100},
        ]


class TrainerListView(LoginRequiredMixin, ListView):
    model = Trainer
    template_name = 'app/trainer_list.html'
    context_object_name = 'trainers'

class TrainerDetailView(DetailView):
    model = Trainer
    template_name = 'app/trainer_detail.html'
    context_object_name = 'trainer'  

class ClassCategoryListView(LoginRequiredMixin, ListView):
    model = ClassCategory
    template_name = "app/class_category_list.html" 
    context_object_name = "categories"

class ClassCategoryDetailView(DetailView):
    model = ClassCategory
    template_name = 'app/class_category_detail.html'
    context_object_name = 'category'  

class ScheduleView(LoginRequiredMixin, FormView):
    template_name = 'app/schedule_form.html'
    form_class = ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memberships'] = MembershipPlan.objects.all()
        context['class_categories'] = ClassCategory.objects.all()
        context['trainers'] = Trainer.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return redirect('schedule_success')

class ScheduleSuccessView(TemplateView):
    template_name = 'app/schedule_success.html'

def schedule_success(request):
    return render(request, 'app/schedule_success.html')