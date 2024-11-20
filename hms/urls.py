"""
URL configuration for hms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from office import views

urlpatterns = [
    path('backend/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('office/', views.office, name='office'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('forgot/', views.forgot, name='forgot'),
    path('debug/', views.debug, name='debug'),
    path('book/', views.book, name='book'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('open_patient/<str:id>', views.open_appointment, name='patient_data'),
    path('patient_detials/<str:id>', views.patient_details, name='patient_details'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('view_staff/', views.view_staff, name='view_staff'),
    path('remove_staff/<str:id>', views.remove_staff, name='remove_staff'),
    path('prev_appointments/<str:id>', views.prev_appointments, name='prev_appointments')
]
