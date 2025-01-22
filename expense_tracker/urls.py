
from django.urls import path
from .views import *

urlpatterns = [
    path('', view),
    path('create_expense/',create_expense),
    path('create_income/',create_income),
    path('<pk>/edit/',edit),
    path('<pk>/delete/',delete),
]