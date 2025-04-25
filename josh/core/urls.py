from django.urls import path
from django.contrib.auth import views as login_check
from . import views
from .forms import LoginForm
from .views import browse, contact, inbox


app_name = "core"


urlpatterns = [
   
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', login_check.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name='login'),
    path('contact/', views.contact, name='contact'),
    path('browse/', browse, name='browse'),
    path('contact/<int:seller_id>/', contact, name='contact_seller'),
    path('inbox/', inbox, name='inbox'),
#    path('contact/', views.contact, name='contact'), the name='contact' is used here   <a href="{% url 'contact' %}"
]