from django.urls import path
from cucumber_app import views
app_name = "cucumber_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("showall/", views.showall, name="showall"),
    path("upload/", views.upload, name="upload"),
    path("result/", views.result, name="result"),
]
