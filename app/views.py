from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post,Video, MembershipPlan,Trainer, ClassCategory, Schedule
from django.contrib.auth.models import User
from .forms import ScheduleForm, VideoForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomLoginForm

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

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/blog_detail.html'

class BlogCreateView(CreateView):
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

class VideoListView(ListView):
    model = Video
    template_name = 'app/video_list.html'
    context_object_name = 'videos'

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'app/video.html'
    success_url = reverse_lazy('video_list')  


def MembershipPlanListView(request):
    plans = [
        {"name": "Basic Plan", "description": "Access to gym and basic facilities.", "price": 20},
        {"name": "Premium Plan", "description": "Includes personal trainer and premium facilities.", "price": 50},
        {"name": "VIP Plan", "description": "All-inclusive access with extra perks.", "price": 100},
    ]
    return render(request, 'app/membership_plan_list.html', {'plans': plans})



class TrainerListView(ListView):
    model = Trainer
    template_name = 'app/trainer_list.html'
    context_object_name = 'trainers'

class TrainerDetailView(DetailView):
    model = Trainer
    template_name = 'app/trainer_detail.html'
    context_object_name = 'trainer'  

class ClassCategoryListView(ListView):
    model = ClassCategory
    template_name = "app/class_category_list.html" 
    context_object_name = "categories"

class ClassCategoryDetailView(DetailView):
    model = ClassCategory
    template_name = 'app/class_category_detail.html'
    context_object_name = 'category'  

def schedule_view(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_success')
    else:
        form = ScheduleForm()

    memberships = MembershipPlan.objects.all()
    class_categories = ClassCategory.objects.all()
    trainers = Trainer.objects.all()

    context = {
        'form': form,
        'memberships': memberships,
        'class_categories': class_categories,
        'trainers': trainers,
    }
    return render(request, 'app/schedule_form.html', context)

def schedule_success(request):
    return render(request, 'app/schedule_success.html')