from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)



class Sensor(models.Model):
    """Описание датчика."""
    name = models.TextField()
    description = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'

class Measurement(models.Model):
    """Измерение температуры на объекте."""
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name = 'measurements')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor} - {self.temperature}'
