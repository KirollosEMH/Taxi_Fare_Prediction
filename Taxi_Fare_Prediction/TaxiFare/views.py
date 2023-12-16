from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
import numpy as np
import pandas as pd
import pickle

with open("./savedModel/model.pkl", 'rb') as model_file:
    model = pickle.load(model_file)
# Create your views here.

def index(request):
    if request.method == 'POST':
        distance = float(request.POST['distance'])
        dropoff_longitude = float(request.POST['dropoff_longitude'])
        ewr_dist = float(request.POST['ewr_dist'])
        nyc_dist = float(request.POST['nyc_dist'])
        pickup_longitude = float(request.POST['pickup_longitude'])
        
        feartures = pd.DataFrame({
            'distance': [distance],
            'dropoff_longitude': [dropoff_longitude],
            'pickup_longitude': [pickup_longitude],
            'ewr_dist': [ewr_dist],
            'nyc_dist': [nyc_dist]
            })

        amount = model.predict(feartures)

        return render(request, 'templates/index.html', {'amount' : amount})
    return render(request, 'templates/index.html')
