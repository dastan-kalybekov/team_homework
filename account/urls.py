from django.urls import path
from account.views import user_list_api_view

urlpatterns = [
    path('user/', user_list_api_view),

]
