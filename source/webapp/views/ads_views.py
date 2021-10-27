from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView

from accounts.admin import User
from webapp.models import Technique


class IndexView(View):
    ordering = ["username"]
    # paginate_by = 5

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, "ads/index.html", {"users": users})
