from django.urls import path
from vehicle.api import views as vehicle_views
urlpatterns = [
    path("", vehicle_views.VehicleView.as_view()),
    path("<int:vehicle_id>/",vehicle_views.VehicleDetailsView.as_view())

]