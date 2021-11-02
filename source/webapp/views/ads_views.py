from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from accounts.admin import User
from webapp.forms import TechniqueStatusForm, SearchForm
from webapp.models import Technique


class IndexView(ListView):
    model = User
    template_name = "ads/index.html"
    context_object_name = "users"
    ordering = ["username"]

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["query"] = urlencode({"q": self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(username__icontains=self.search_value) | Q(techniques__category__name=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["q"]


class CraneView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="truck crane")
        return render(request, "ads/technique.html", {"techniques": techniques})

class ExcavatorView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="excavator")
        return render(request, "ads/technique.html", {"techniques": techniques})

class TruckView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="truck")
        return render(request, "ads/technique.html", {"techniques": techniques})


class LorryView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="lorry")
        return render(request, "ads/technique.html", {"techniques": techniques})


class SmallTrackView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="small track")
        return render(request, "ads/technique.html", {"techniques": techniques})


class LoaderTrackView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="loader")
        return render(request, "ads/technique.html", {"techniques": techniques})


class ManipulatorTrackView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="manipulator")
        return render(request, "ads/technique.html", {"techniques": techniques})


class BuildTechniqueView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="build technique")
        return render(request, "ads/technique.html", {"techniques": techniques})


class TractorView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="tractor")
        return render(request, "ads/technique.html", {"techniques": techniques})


class OtherTechniqueView(View):
    ordering = ["is_active"]

    def get(self, request, *args, **kwargs):
        techniques = Technique.objects.filter(category__name="other technique")
        return render(request, "ads/technique.html", {"techniques": techniques})


class TechniqueDetailView(DetailView):
    model = Technique
    template_name = "ads/detail.html"


class TechniqueCreateView(CreateView):
    model = Technique
    fields = ["category", "name", "foto", "price", "price_description", "description", "sale_price", "qty"]
    template_name = "ads/create.html"

    def form_valid(self, form):
        form.instance.advertiser = self.request.user
        return super(TechniqueCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("webapp:index")


class TechniqueEditView(UserPassesTestMixin, UpdateView):
    model = Technique
    fields = ["category", "name", "foto", "price", "price_description", "description", "sale_price", "qty"]
    template_name = "ads/edit.html"

    def test_func(self):
        return self.request.user == self.get_object().advertiser or self.request.user.is_superuser

    def get_success_url(self):
        return reverse("webapp:technique_detail", kwargs={"pk": self.get_object().pk})


class TechniqueDeleteView(UserPassesTestMixin, DeleteView):
    model = Technique
    template_name = "ads/detail.html"

    def test_func(self):
        return self.request.user == self.get_object().advertiser or self.request.user.is_superuser

    def get_success_url(self):
        return reverse("webapp:index")


class TechniqueStatusChangeView(UserPassesTestMixin, View):

    def test_func(self):
        technique = get_object_or_404(Technique, pk=self.kwargs["pk"])
        return self.request.user == technique.advertiser or self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        form = TechniqueStatusForm()
        return render(request, "ads/detail.html", {"form": form})

    def post(self, request, *args, **kwargs):
        technique = get_object_or_404(Technique, pk=kwargs["pk"])
        technique.status = request.POST.get('status')
        technique.save()
        return render(request, "ads/detail.html", {"technique": technique})
