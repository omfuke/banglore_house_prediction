from houseprice import views
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('houseprice',views.HouseView)
urlpatterns = [
    path('index/',views.index),
    path('api/',include(router.urls)),
    path('status/',views.HousePredict)
]

