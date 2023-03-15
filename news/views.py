from django.views.generic import ListView, DetailView

from .models import *


class HomeNews(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'
