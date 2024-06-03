from django.db import models


class Sensor(models.Model):
    sensor_type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model} - {self.sensor_type}"


class Data(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.timestamp} - Sensor: {self.sensor.model}"


class Alert(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.sensor.model} at {self.timestamp}"
