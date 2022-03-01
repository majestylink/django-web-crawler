from django.urls import path
from .views import Index, Thanks

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('thanks/', Thanks.as_view(), name='thanks'),
]
