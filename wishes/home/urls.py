"""wishes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('data', views.data, name='data'),
    path('delete_data/<int:bd_id>', views.delete_data, name='delete_data'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/edit_data/<int:id>', views.edit_data, name='edit_data'),
]
