from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from accounts.forms import RegistrationForm, ProfileChangeForm, UserChangeForm
from django.urls import reverse


class RegisterView(CreateView):
    model = get_user_model()
    template_name = "registration/register.html"
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse("webapp:index")


class UserDetailView(UserPassesTestMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def test_func(self):
        return self.request.user == self.get_object() or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        advertiser = self.object.techniques.order_by('is_active')
        paginator = Paginator(advertiser, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['advertiser'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class UsersView(ListView):
    model = get_user_model()
    template_name = "ads/index.html"
    context_object_name = "users"
    ordering = ["username"]


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user == self.get_object() or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.get_profile_form()
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return ProfileChangeForm(**form_kwargs)

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs["pk"] or self.request.user.is_superuser

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.pk})