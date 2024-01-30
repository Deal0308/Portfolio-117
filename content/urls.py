from django.urls import path
from content import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.projects_list, name='projects_list'),
    path('new/', views.project_new, name='new_project'),
    path('experience_list/', views.experience_list, name='experience_list'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)