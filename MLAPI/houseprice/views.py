from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HouseSerializers
from .models import HouseModel
from rest_framework.decorators import api_view
from sklearn.externals import joblib
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.response import Response
import numpy as np
import json


# Create your views here.


class HouseView(viewsets.ModelViewSet):

    queryset = HouseModel.objects.all()
    serializer_class = HouseSerializers



@api_view(['POST'])
def HousePredict(request):
    predictive_model = joblib.load('C:\\Users\\omfuk\\Desktop\\Django\\DjangoML\\MLAPI\\houseprice\\banglore_home_prices_model.pickle')
    mydata = request.data

    with open('C:\\Users\\omfuk\\Desktop\\Django\\DjangoML\\MLAPI\\houseprice\\columns.json') as f:
        columns = json.load(f)['data_columns']

    unit = list(mydata.values())
    unit = unit[1:]
    unit[0] = str(unit[0])
    unit[1] = int(unit[1])
    unit[2] = int(unit[2])
    unit[3] = int(unit[3])

    x = np.zeros(len(columns))

    x[0] = unit[1]
    x[1] = unit[2]
    x[2] = unit[3]

    for i in columns:
        if i == str(unit[0].lower()):
            x[columns.index(i)] = 1


    x = x.reshape(1,-1)
    predict = predictive_model.predict(x)



    return JsonResponse('{}'.format(predict),safe=False)


def index(request):

    return render(request,'houseprice/index.html')

