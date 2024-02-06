# urls.py

from django.urls import path
from .views import registration_view,show_data,Update_view,delete_registration

urlpatterns = [
    path('register/', registration_view, name='registration_view'),
    path('show/', show_data, name='show'),
    path('update/<int:id>/', Update_view, name='update_registration'),
     path('delete/<int:id>/', delete_registration, name='delete_registration'),
]
