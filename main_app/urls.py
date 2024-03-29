from django.urls import path

from . import views  # Import the views module from the same directory.

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("finches/", views.finches_index, name="index"),
    path("finches/<int:finch_id>/", views.finches_detail, name="detail"),
    path("finches/create/", views.FinchCreate.as_view(), name="finches_create"),
    path(
        "finches/<int:pk>/delete/", views.FinchDelete.as_view(), name="finches_delete"
    ),
    path(
        "finches/<int:pk>/update/", views.FinchUpdate.as_view(), name="finches_update"
    ),
]
