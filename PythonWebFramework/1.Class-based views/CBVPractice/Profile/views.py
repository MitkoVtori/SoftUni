from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from CBVPractice.Profile import models
from  CBVPractice.Profile.forms import ArticleForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'User'
        return context


class ArticleListView(ListView):
    context_object_name = "profiles"
    model = models.Profile
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'User'
        context['profile'] = models.Profile
        context['article'] = models.Article.objects.first()
        return context


class ArticleDetailView(DetailView):
    template_name = 'details.html'
    context_object_name = 'article_detail'
    model = models.Article


class CreateArticle(CreateView):
    fields = '__all__'
    model = models.Article
    template_name = 'create_article.html'


class UpdateArticle(UpdateView):
    fields = '__all__'
    model = models.Article
    template_name = "update_article.html"


class ArticleDeleteView(DeleteView):
    fields = '__all__'
    model = models.Article
    form_class = ArticleForm
    template_name = "delete_article.html"
    success_url = reverse_lazy("index")

    def get_initial(self):
        article_object = self.get_object()
        return {"title": article_object.title, "content": article_object.content}