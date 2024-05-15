"""
URL configuration for Phood1 project.

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
from django.urls import path, re_path
from pages.views import homepage_view, allrecipes_view, specific_recipe_view, add_recipe_view, ing_fset_view, update_recipe_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage_view, name='home'),
    path('recipes/<str:ingredient>/', allrecipes_view, name='recipes'),
    path('spec_rec/<int:recipe_id>/', specific_recipe_view, name='specific_recipe'),
    path('add_recipe<int:form1_done>/', add_recipe_view, name='add_recipe'),
    path('update_rec/<int:recipe_id>/', update_recipe_view, name='update_recipe'),
    path('ing_fset/', ing_fset_view, name='ing_fset'),

]
