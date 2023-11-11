from django.urls import path

from . import views

app_name = "wikipedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("results", views.searchBox, name="results"),
    path("new-page", views.newPage, name="newPage"),
    path("edit-page", views.editPage, name="editPage"),
    path("random-page", views.randomPage, name="randomPage"),
    path("<str:entry>", views.entryPage, name="entryPage")
]
