from django.urls import path
from recipes.views import home, my_view, contato

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', my_view),
]
