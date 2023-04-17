from .models import Podcast, Episode, Host, Photo
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
HOST_FIELDS = ['description']
PHOTO_FIELDS = ['image', 'description']


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about/about.html')


def photos(request):
    context = {"photos": Photo.objects.all()}
    return render(request, 'about/photos.html', context=context)


def map(request):
    return render(request, 'about/map.html')


def hosts(request):
    hosts = Host.objects.all()
    context = {
        "hosts": hosts
    }
    return render(request, 'about/hosts.html', context=context)


def contact(request):
    hosts = Host.objects.all()
    context = {
        "hosts": hosts
    }
    return render(request, 'about/contact.html', context=context)


# class EpisodeDetailView(UserPassesTestMixin, DetailView):
#     model = Episode

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def get(self, request, *args, **kwargs):
#         episode = get_object_or_404(Episode, pk=kwargs['pk'])
#         context = {
#             "item": episode
#         }
#         return render(request, 'market/COURSE_DESIGN.html', context)


# class EpisodeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     model = Episode
#     fields = EPISODE_FIELDS
#     template_name = FORM_VIEW_TEMPLATE_NAME

#     def form_valid(self, form):
#         form.instance.podcast_fk = Podcast.objects.first()
#         return super().form_valid(form)

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def get_context_data(self, **kwargs):
#         context = super(EpisodeCreateView, self).get_context_data(**kwargs)
#         header = "Create episode"
#         create = True # If update, false; if create, true
#         context.update({"header": header, "create": create})
#         return context


# class EpisodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Episode
#     fields = EPISODE_FIELDS
#     template_name = FORM_VIEW_TEMPLATE_NAME

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def test_func(self):
#         return self.request.user.is_superuser

#     def get_context_data(self, **kwargs):
#         context = super(EpisodeUpdateView, self).get_context_data(**kwargs)
#         header = "Update episode"
#         create = False # If update, false; if create, true
#         context.update({"header": header, "create": create})
#         return context


# class HostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Host
#     fields = HOST_FIELDS
#     template_name = FORM_VIEW_TEMPLATE_NAME

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def test_func(self):
#         return self.request.user.is_superuser

#     def get_context_data(self, **kwargs):
#         context = super(HostUpdateView, self).get_context_data(**kwargs)
#         header = "Update host"
#         create = False # If update, false; if create, true
#         context.update({"header": header, "create": create})
#         return context


# class PhotoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     model = Photo
#     fields = PHOTO_FIELDS
#     template_name = FORM_VIEW_TEMPLATE_NAME

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def test_func(self):
#         return self.request.user.is_superuser

#     def get_context_data(self, **kwargs):
#         context = super(PhotoCreateView, self).get_context_data(**kwargs)
#         header = "Add photo"
#         create = True # If update, false; if create, true
#         context.update({"header": header, "create": create})
#         return context


# class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Photo
#     fields = PHOTO_FIELDS
#     template_name = FORM_VIEW_TEMPLATE_NAME

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def test_func(self):
#         return self.request.user.is_superuser

#     def get_context_data(self, **kwargs):
#         context = super(PhotoUpdateView, self).get_context_data(**kwargs)
#         header = "Update photo"
#         create = False # If update, false; if create, true
#         context.update({"header": header, "create": create})
#         return context

