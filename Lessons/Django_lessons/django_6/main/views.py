from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class Main(View):
    def get(self, *args, **kwargs):
        title= self.request.GET.get('title', 'YBXT YT GTHTLFKB')
        title= self.request.GET.get('deck', 'YBXT YT hghdhfsd')
        return render(self.request, 'index.html', {})

    def post(self, *args, **kwargs):
        return render(self.request, 'post.html', {})


class AboutViews(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = "О мне"
        return context


class SuperAboutView(AboutViews):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = "О супер мне"
        return context