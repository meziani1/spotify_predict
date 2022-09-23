from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
# Create your views here.
from .forms import SkippedForm 
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .models import Skipped 
from .serializer import SkippedSerializers 
import joblib
import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 

class SkippedView(viewsets.ModelViewSet): 
    queryset = Skipped.objects.all() 
    serializer_class = SkippedSerializers 

def status(df):
    try:
        
        model = joblib.load(r"C:\Users\admin\Desktop\projet_django\DeployML\DjangoAPI\XGBOOST.sav")
        scaler=StandardScaler()
        scaler.fit(df)
        X = scaler.transform(df) 
        y_pred = model.predict(X) 
        #y_pred=(y_pred==1) 
        #result = "Yes" if y_pred else "No"
        result=y_pred
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 

def FormView(request):
    if request.method=='POST':
        form=SkippedForm(request.POST or None)

        if form.is_valid():
            not_skipped = form.cleaned_data['not_skipped']
            no_pause_before_play = form.cleaned_data['no_pause_before_play']
            context_type_user_collection = form.cleaned_data['context_type_user_collection']
            hist_user_behavior_reason_start_fwdbtn= form.cleaned_data['hist_user_behavior_reason_start_fwdbtn']
            hist_user_behavior_reason_start_trackdone = form.cleaned_data['hist_user_behavior_reason_start_trackdone']
            hist_user_behavior_reason_end_backbtn = form.cleaned_data['hist_user_behavior_reason_end_backbtn']
            hist_user_behavior_reason_end_fwdbtn = form.cleaned_data['hist_user_behavior_reason_end_fwdbtn']
            hist_user_behavior_reason_end_trackdone = form.cleaned_data['hist_user_behavior_reason_end_trackdone']
            mode_0 = form.cleaned_data['mode_0']
            week_day_Monday = form.cleaned_data['week_day_Monday']
           
           
           
            df=pd.DataFrame({'not_skipped':[not_skipped], 'no_pause_before_play':[no_pause_before_play], 
            'context_type_user_collection':[context_type_user_collection],
            'hist_user_behavior_reason_start_fwdbtn':[hist_user_behavior_reason_start_fwdbtn],
            'hist_user_behavior_reason_start_trackdone':[hist_user_behavior_reason_start_trackdone],
            'hist_user_behavior_reason_end_backbtn':[hist_user_behavior_reason_end_backbtn],
            'hist_user_behavior_reason_end_fwdbtn':[hist_user_behavior_reason_end_fwdbtn],
            'hist_user_behavior_reason_end_trackdone':[hist_user_behavior_reason_end_trackdone],
            'mode_0':[mode_0],
            'week_day_Monday':[week_day_Monday]})
            result = status(df)
            return render(request, 'status.html', {"data": result}) 
            
    form=SkippedForm()
    return render(request, 'form.html', {'form':form})