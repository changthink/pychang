from django.urls import path
from . import views

app_name = 'ahome'

urlpatterns = [
    path('', views.apply_base , name='apply_base'),
    path('pjmanage/', views.pj_list , name='pj_list'),
    path('<int:abase_id>/', views.apply_detail , name='apply_detail'),
    path('ibju/', views.ibju_data , name='ibju_list'),
]