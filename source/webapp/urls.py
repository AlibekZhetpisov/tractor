from django.urls import path
from webapp import views as webapp_views

app_name = "webapp"

urlpatterns = [
    path("", webapp_views.IndexView.as_view(), name="index"),
    path("crane/", webapp_views.CraneView.as_view(), name="crane"),
    path("excavator/", webapp_views.ExcavatorView.as_view(), name="excavator"),
    path("truck/", webapp_views.TruckView.as_view(), name="truck"),
    path("lorry/", webapp_views.LorryView.as_view(), name="lorry"),
    path("small_truck/", webapp_views.SmallTrackView.as_view(), name="small_truck"),
    path("manipulator/", webapp_views.ManipulatorTrackView.as_view(), name="manipulator"),
    path("loader/", webapp_views.LoaderTrackView.as_view(), name="loader"),
    path("build_technique/", webapp_views.BuildTechniqueView.as_view(), name="build_technique"),
    path("tractor/", webapp_views.TractorView.as_view(), name="tractor"),
    path("other_technique/", webapp_views.OtherTechniqueView.as_view(), name="other_technique"),
    path("technique/create/", webapp_views.TechniqueCreateView.as_view(), name="technique_create"),
    path("technique/<int:pk>/change-status/", webapp_views.TechniqueStatusChangeView.as_view(), name="change_status"),
    path("technique/<int:pk>/", webapp_views.TechniqueDetailView.as_view(), name="technique_detail"),
    path("technique/<int:pk>/edit/", webapp_views.TechniqueEditView.as_view(), name="technique_edit"),
    path("technique/<int:pk>/delete/", webapp_views.TechniqueDeleteView.as_view(), name="technique_delete"),
    path("technique/<int:pk>/order/create/", webapp_views.OrderCreateView.as_view(), name="order_create"),
    path("technique/<int:pk>/order/delete/", webapp_views.OrderDeleteView.as_view(), name="order_delete"),
    path("technique/<int:pk>/comment/create/", webapp_views.CommentCreateView.as_view(), name="comment_create")
]