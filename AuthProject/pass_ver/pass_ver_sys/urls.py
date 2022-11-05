from django.urls import path
from .views import Home_page,Register_page,Login_page,Logout_page,Dashboard_page,Admin_page
urlpatterns = [
    path('', Home_page, name='Home'),
    path('Register', Register_page, name='Register'),
    path('Login', Login_page, name='Login'),
    path('Logout', Logout_page, name='Logout'),
    path('Dashboard', Dashboard_page, name='Dashboard'),
    path('admin', Admin_page, name='admin'),
]