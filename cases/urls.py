from django.urls import path

from .views import DataListView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('Cases/', DataListView.as_view(), name='case'),
]