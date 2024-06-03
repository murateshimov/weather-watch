from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, DataViewSet, AlertViewSet, login_view, ExampleView

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'data', DataViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('example/', ExampleView.as_view(), name='example'),
    path('accounts/', include('allauth.urls')),
    path('login/', login_view, name='login'),
]
