from django.urls import path
from . import views  # Import the views module from the same directory.

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("finches/", views.finches_index, name="index"),
    path("finches/<int:finch_id>/", views.finches_detail, name="detail"),
]
