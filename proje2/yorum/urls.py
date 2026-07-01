from django.urls import path
from .views import admin_liste,yorum_liste,yorum_id,yorum_sil
urlpatterns = [
    path("admin_liste/",admin_liste,name="admin_liste"),
    path("yorum_liste/",yorum_liste,name="yorum_liste"),
    path("yorum_id/<int:pk>/",yorum_id,name="yorum_id"),
    path("yorum_sil/<int:pk>/",yorum_sil,name="yorum_sil"),

 
]
