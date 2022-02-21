from django.urls import path
from measurement.views import SensorAllView, SensorView, MeasurementAllView, MeasurementView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAllView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('measurements/', MeasurementAllView.as_view()),

]
