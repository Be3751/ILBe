from django.urls import path
from listitems import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('detail/<int:pk>/', views.ItemDetail.as_view(), name='detail'),
    path('request/<int:pk>/', views.RequestView.as_view(), name='request'),
]

# handler500 = views.my_customized_server_error