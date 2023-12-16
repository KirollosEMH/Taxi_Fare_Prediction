from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
import numpy as np
from joblib import load
model = load('./savedModel/xgb.joblib')
scaler = load('./savedModel/scaler.joblib')
# Create your views here.

def index(request):
    if request.method == 'POST':
        pickup_longitude = request.POST['pickup_longitude']
        pickup_latitude = request.POST['pickup_latitude']
        dropoff_longitude = request.POST['dropoff_longitude']
        dropoff_latitude = request.POST['dropoff_latitude']
        hour = request.POST['hour']
        month = request.POST['month']
        weekday = request.POST['weekday']
        year = request.POST['year']
        jfk_dist = request.POST['jfk_dist']
        ewr_dist = request.POST['ewr_dist']
        lga_dist = request.POST['lga_dist']
        sol_dist = request.POST['sol_dist']
        nyc_dist = request.POST['nyc_dist']
        distance = request.POST['distance']
        bearing = request.POST['bearing']
        
        feartures = [[pickup_longitude, pickup_latitude, dropoff_longitude,
                     dropoff_latitude, hour, month, weekday, year, jfk_dist,
                     ewr_dist, lga_dist, sol_dist, nyc_dist, distance, bearing]]
        
        amount = model.predict(scaler.fit_transform(feartures))
        return render(request, 'templates/index.html', {'result' : amount})
    return render(request, 'templates/index.html')
