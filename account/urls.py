from django.urls import path
from account.views import user_list_api_view

urlpatterns = [
    path('api/user/', user_list_api_view),

]
