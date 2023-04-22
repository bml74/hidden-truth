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
EPISODE_FIELDS = ['title', 'description', 'locked']
HOST_FIELDS = ['description']
PHOTO_FIELDS = ['image', 'description']


def home(request):
    return render(request, 'home.html')


def trailer(request):
    return render(request, 'episodes/trailer.html')


def episodes(request):
    return render(request, 'episodes.html')


def e1(request):
    return render(request, 'episodes/e1.html')


def e2(request):
    return render(request, 'episodes/e2.html')


def e3(request):
    return render(request, 'episodes/e3.html')


def e4(request):
    return render(request, 'episodes/e4.html')


def about(request):
    return render(request, 'about/about.html')


def photos(request):

    deborah_shick_photos = []
    deborah_shick_photos = [
        "IMG_1293.png",
        "IMG_1294.png",
        "IMG_1295.png",
        "IMG_1296.png",
        "IMG_1297.png",
        "IMG_1298.png",
        "IMG_1299.png",
        "IMG_1300.png",
        "IMG_1301.png",
        "IMG_1302.png",
        "IMG_1303.png",
        "IMG_1304.png",
        "IMG_1305.png"
    ]
    for i in range(len(deborah_shick_photos)):
        deborah_shick_photos[i] = f"https://rwbruno.s3.amazonaws.com/hidden-truth/deborah-shick/{deborah_shick_photos[i]}"
    
    christine_hammond_photos = []
    christine_hammond_photos = [
        "69925403639__70768B8A-2EFA-41B2-95BB-F9FCD5D23222.png",
        "69925406429__F5F9DEE8-9CAF-46FD-BE70-DD75E48863D7.png",
        "69925407770__9DF3E0A8-C961-4B7D-BA0C-95DA9632763F.png",
        "69925412435__48B5A02D-FE77-4119-B839-AAEA574CDE98.png",
        "69925415141__F052B8F4-70AC-4F31-8739-4F80FDB4F2CC.png",
        "IMG_6775.png",
        "IMG_6776.png"
    ]
    for i in range(len(christine_hammond_photos)):
        christine_hammond_photos[i] = f"https://rwbruno.s3.amazonaws.com/hidden-truth/christine-hammond/{christine_hammond_photos[i]}"
    
    erin_flynn_photos = []
    erin_flynn_photos = [
        "IMG_1218.png",
        "IMG_1221.png",
        "IMG_1222.png",
        "IMG_1239.png",
        "IMG_1240.png"
    ]
    for i in range(len(erin_flynn_photos)):
        erin_flynn_photos[i] = f"https://rwbruno.s3.amazonaws.com/hidden-truth/erin-flynn/{erin_flynn_photos[i]}"

    context = {
        "deborah_shick_photos": deborah_shick_photos,
        "christine_hammond_photos": christine_hammond_photos,
        "erin_flynn_photos": erin_flynn_photos
    }
    return render(request, 'about/photos.html', context=context)


def map(request):
    return render(request, 'about/map.html')


def documents(request):
    return render(request, 'about/documents.html')


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


class EpisodeDetailView(UserPassesTestMixin, DetailView):
    model = Episode

    def test_func(self):
        return self.request.user.is_authenticated

    def get(self, request, *args, **kwargs):
        episode = get_object_or_404(Episode, pk=kwargs['pk'])
        context = {
            "episode": episode
        }
        return render(request, 'episode.html', context)


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


class HostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Host
    fields = HOST_FIELDS
    template_name = FORM_VIEW_TEMPLATE_NAME

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(HostUpdateView, self).get_context_data(**kwargs)
        header = "Update host"
        create = False # If update, false; if create, true
        context.update({"header": header, "create": create})
        return context


class PhotoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Photo
    fields = PHOTO_FIELDS
    template_name = FORM_VIEW_TEMPLATE_NAME

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(PhotoCreateView, self).get_context_data(**kwargs)
        header = "Add photo"
        create = True # If update, false; if create, true
        context.update({"header": header, "create": create})
        return context


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = PHOTO_FIELDS
    template_name = FORM_VIEW_TEMPLATE_NAME

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(PhotoUpdateView, self).get_context_data(**kwargs)
        header = "Update photo"
        create = False # If update, false; if create, true
        context.update({"header": header, "create": create})
        return context

