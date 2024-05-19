from django.contrib import admin
from django.urls import path, include
from my_app import views
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', views.sign_up, name='register'),
    path('plant_management/', views.plant_management, name='plant_management'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('update_plant/<int:plant_id>/', views.update_plant, name='update_plant'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.MainView.as_view(), name='main'),
    path('home/', views.MainView.as_view(), name='home'),
    path('plants/', views.PlantView.as_view(), name='plants'),    
    path('plant_details/<int:plant_id>/', views.display_plant_details, name='plant_details'),
    path('plant/<int:plant_id>/add_to_cart/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('order_management/', views.order_management, name='order_management'),
    path('orders/', views.orders_view, name='orders'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
