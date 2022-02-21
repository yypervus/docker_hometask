# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer

class SensorAllView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor.objects.create(name=request.data.get('name'), description=request.data.get('description'))
        return Response(status=status.HTTP_201_CREATED)



class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


    def patch(self, request):
        Sensor.objects.create(description=request.data.get('description'), partial=True)
        return Response({'status':'ok'})


class MeasurementAllView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        Measurement.objects.create(sensor_id=request.data.get('sensor'),temperature=request.data.get('temperature'))
        return Response({'status':'ok'})

class MeasurementView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



