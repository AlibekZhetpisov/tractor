from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DeleteView

from webapp.models import Order, Technique
from webapp.forms import OrderForm


class OrderCreateView(View):
    def get(self, request, *args, **kwargs):
        form = OrderForm()
        return render(request, "ads/detail.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = OrderForm(data=request.POST)
        technique = get_object_or_404(Technique, pk=kwargs["pk"])
        user = technique.advertiser
        if form.is_valid():
            order = Order.objects.create(
                technique=technique,
                author=user,
                start_time=form.cleaned_data["start_time"],
                end_time=form.cleaned_data["end_time"],
                description=form.cleaned_data["description"],
                offered_price=form.cleaned_data["offered_price"])

            return redirect("webapp:technique_detail", pk=order.technique.pk)
        else:
            return render(request, "ads/detail.html", {"form": form, "technique": technique})


class OrderDeleteView(UserPassesTestMixin, DeleteView):
    model = Order
    template_name = "user_detail.html"

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser

    def get_success_url(self):
        return reverse("accounts:profile")