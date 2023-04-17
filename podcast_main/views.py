from .models import Podcast, Episode
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


FORM_VIEW_TEMPLATE_NAME = 'form_view.html'
EPISODE_FIELDS = ['title', 'description']


def home(request):
    return render(request, 'home.html')


class EpisodeDetailView(UserPassesTestMixin, DetailView):
    model = Episode

    def test_func(self):
        return self.request.user.is_authenticated

    def get(self, request, *args, **kwargs):
        episode = get_object_or_404(Episode, pk=kwargs['pk'])
        context = {
            "item": episode
        }
        return render(request, 'market/COURSE_DESIGN.html', context)


class EpisodeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Episode
    fields = EPISODE_FIELDS
    template_name = FORM_VIEW_TEMPLATE_NAME

    def form_valid(self, form):
        form.instance.podcast_fk = Podcast.objects.first()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super(EpisodeCreateView, self).get_context_data(**kwargs)
        header = "Create episode"
        create = True # If update, false; if create, true
        context.update({"header": header, "create": create})
        return context


class EpisodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Episode
    fields = EPISODE_FIELDS
    template_name = FORM_VIEW_TEMPLATE_NAME

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(EpisodeUpdateView, self).get_context_data(**kwargs)
        header = "Update episode"
        create = False # If update, false; if create, true
        context.update({"header": header, "create": create})
        return context

