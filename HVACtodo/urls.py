from django.urls import path
from . import views
# from .views import IndexView

app_name = 'HVACtodo'
urlpatterns = [
    path('', views.index, name='index'),
    # This is a class view or object view, instead of just a function view.
    # path('', IndexView.as_view(), name='index'),
    path('list.html', views.list, name='list'),
    path('status.html', views.status, name='status'),
    
]

