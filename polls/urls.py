from django.urls import path
from polls.views import IndexView,DetailView,ResultsView,vote,create_view,create_choice_view,delete_poll
from django.conf import settings
from django.conf.urls.static import static

app_name="polls"
urlpatterns = [
    path("" ,  IndexView.as_view(), name="index"),
    path("<int:pk>/" , DetailView.as_view() , name="detail"),
    path("<int:question_id>/vote/" , vote , name="vote"),
    path("<int:pk>/results/" , ResultsView.as_view() , name="results"),
    path("create-poll/" , create_view , name="create_view"),
    path("create-choice/<int:question_id>" , create_choice_view , name="create_choice_view"),
    path("delete-choice/<int:question_id>" , delete_poll , name="delete_view")
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)