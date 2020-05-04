from django.urls import path
from app import views
from django.conf.urls import url

app_name = 'app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreate.as_view(), name='create'),
    path('update/<pk>/', views.SchoolUpdate.as_view(), name='update'),
    path('delete/<pk>/', views.SchoolDelete.as_view(), name='delete'),

]

