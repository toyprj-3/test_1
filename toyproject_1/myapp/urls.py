from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "myapp"

urlpatterns = [
    path("", views.PostList.as_view(), name="list"),
    path("posts/<int:pk>/", views.PostDetail.as_view(), name="detail"),
    path("posts/create/", views.PostCreate.as_view(), name="create"),
    path("posts/update/<int:pk>/", views.PostUpdate.as_view(), name="update"),
    path("posts/delete/<int:pk>/", views.PostDelete, name="delete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
