from datetime import datetime

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import FeedbackForm, CommentModelForm, BlogForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Article, Comment


def news(request):
    return render(request, 'news.html')

def add_article(request):
    return render(request, 'add_article.html')

def about(request):
    return render(request, 'about.html')

def links(request):
    return render(request, 'links.html')

def pool(request):
    submitted_data = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
    else:
        form = FeedbackForm()

    return render(request, 'pool.html', {'form': form, 'submitted_data': submitted_data})

def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            reg_form = form.save(commit=False)
            reg_form.is_active = True
            reg_form.is_staff = False
            reg_form.is_superuser = False
            reg_form.date_joined = datetime.now()
            reg_form.last_login = datetime.now()
            reg_form.save()
            reg_form.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, reg_form)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован!')
            return redirect("news")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def article_list(request):
    articles = Article.objects.all().order_by('-pub_date')  # Сортировка по дате публикации (новые сначала)
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    new = Article.objects.get(pk=pk)
    title = new.title
    comments = Comment.objects.filter(new=new).order_by("-date_published")
    articles = get_object_or_404(Article, id=pk)
    context = {
        "new": new,
        "title": title,
        "comments": comments,
        'articles': articles
    }

    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.date_published = datetime.now()
            new_comment.new = new
            new_comment.save()
            return redirect("article_detail", pk=pk)
    else:
        form = CommentModelForm()
    context["form"] = form
    return render(request, 'article_detail.html', context)

class CustomLoginView(LoginView):
    template_name = 'auth.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('news')

    def get_success_url(self):
        return self.success_url


def add_article_form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.pub_date = datetime.now()
            blog.save()
            return redirect('article_list')
    else:
        form = BlogForm()
    return render(request, 'add_article.html', {'form': form})

def video_page(request):
    return render(request, 'video.html')

@login_required
def profile(request):
    user = request.user  # Получаем текущего пользователя
    return render(request, 'profile.html', {'user': user})