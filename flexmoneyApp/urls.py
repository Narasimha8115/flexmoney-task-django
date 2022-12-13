from django.urls import path
from .views import yoga_form_data,create_user_admission,Update_details,delete_details,view_details

urlpatterns = [
    path('',yoga_form_data,name='yoga_form_data'),
    path('create/',create_user_admission,name="create_user_admission"),
    path('update/<int:id>/',Update_details,name="Update_details"),
    path('delete/<int:id>/',delete_details,name="delete_details"),
    path('view/<int:id>/',view_details,name="view_details")
    
]