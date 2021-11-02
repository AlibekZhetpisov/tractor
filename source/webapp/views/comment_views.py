from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from webapp.forms import CommentForm
from webapp.models import Comment, Technique


class CommentCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, "comment/create.html", {"form": form, "pk":kwargs["pk"]})
    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        technique = get_object_or_404(Technique, pk=kwargs["pk"])
        user = technique.advertiser
        if form.is_valid():
            comment = Comment.objects.create(
                technique=technique,
                author=user,
                text=form.cleaned_data["text"])

            return redirect("webapp:technique_detail", pk=comment.technique.pk)
        else:
            return render(request, "comment/create.html", {"form": form})