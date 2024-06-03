from django.contrib import admin
from .models import Sensor, Data, Alert


class SensorAdmin(admin.ModelAdmin):
    list_display = ('model', 'sensor_type', 'installation_date', 'status')
    list_filter = ('sensor_type', 'status')
    search_fields = ('model', 'sensor_type')


class DataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'sensor', 'temperature',
                    'humidity', 'wind_speed')
    list_filter = ('timestamp', 'sensor')
    search_fields = ('sensor__model',)


class AlertAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'sensor', 'description')
    list_filter = ('timestamp', 'sensor')
    search_fields = ('sensor__model', 'description')


admin.site.register(Sensor)
admin.site.register(Data)
admin.site.register(Alert)
