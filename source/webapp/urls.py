from django.urls import path
from webapp import views as webapp_views

app_name = "webapp"

urlpatterns = [
    path("", webapp_views.IndexView.as_view(), name="index")
    # path("projects/create/", webapp_views.ProjectCreateView.as_view(), name="project_create"),
    # path("projects/<int:pk>/", webapp_views.ProjectView.as_view(), name="project_detail"),
    # path("projects/<int:pk>/edit/", webapp_views.ProjectUpdateView.as_view(), name="project_update"),
    # path("projects/<int:pk>/delete/", webapp_views.ProjectDeleteView.as_view(), name="project_delete"),
    # path("projects/<int:pk>/issue/", webapp_views.ProjectIssueView.as_view(), name="issue_detail"),
    # path("projects/<int:pk>/issue/create/", webapp_views.ProjectIssueCreateView.as_view(), name="issue_create"),
    # path("projects/<int:pk>/issue/edit/", webapp_views.ProjectIssueUpdateView.as_view(), name="issue_update"),
    # path("projects/<int:pk>/issue/delete/", webapp_views.ProjectIssueDeleteView.as_view(), name="issue_delete"),
    # path("projects/<int:pk>/user/add/", webapp_views.ProjectUserAddView.as_view(), name="user_add"),
    # path("projects/<int:pk>/user/delete/", webapp_views.ProjectUserDeleteView.as_view(), name="user_delete")
]