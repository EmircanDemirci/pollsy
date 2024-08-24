from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = "user"
urlpatterns = [
    path("login/" , views.login_user , name="login"),
    path("logout/" , views.logout_user , name="logout"),
    path("register/" , views.register_user , name="register_user"),
    path("profile/" , views.profile , name="profile"),
    path("profile/<int:user_id>" , views.profile_another , name="profile_another"),
    path("profile_edit/" , views.profile_edit , name="profile_edit")
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)