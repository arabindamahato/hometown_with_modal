from django.urls import path
from myapp import views
app_name = 'myapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('history/', views.history, name = "history"),
    path('foods/', views.foods, name = "foods"),
    path('places/', views.places, name = "places"),


]   