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
        
        model = joblib.load("./DjangoAPI/XGBOOST.sav")
        #scaler=StandardScaler()
        #scaler.fit(df)
        #X = scaler.transform(df) 
        y_pred = model.predict(df) 
        y_pred=(y_pred==1) 
        result = "This track will be skipped" if y_pred else "No skip"
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 

def FormView(request):
    if request.method=='POST':
        form=SkippedForm(request.POST or None)

        if form.is_valid():
            session_position = form.cleaned_data['session_position']
            session_length = form.cleaned_data['session_length']
            no_pause_before_play = form.cleaned_data['no_pause_before_play']
            hist_user_behavior_n_seekfwd= form.cleaned_data['hist_user_behavior_n_seekfwd']
            hour_of_day = form.cleaned_data['hour_of_day']
            premium = form.cleaned_data['premium']
            hist_user_behavior_n_seekback = form.cleaned_data['hist_user_behavior_n_seekback']
            week_day = form.cleaned_data['week_day']
            context_type = form.cleaned_data['context_type']
            hist_user_behavior_reason_start = form.cleaned_data['hist_user_behavior_reason_start']
            hist_user_behavior_reason_end = form.cleaned_data['hist_user_behavior_reason_end']
           
           
            df=pd.DataFrame({'session_position':[session_position], 
            'session_length':[session_length], 
            'no_pause_before_play':[no_pause_before_play],
            'hist_user_behavior_n_seekfwd':[hist_user_behavior_n_seekfwd],
            'hour_of_day':[hour_of_day],
            'premium':[premium],
            'hist_user_behavior_n_seekback':[hist_user_behavior_n_seekback],
            'week_day':[week_day],
            'context_type':[context_type],
            'context_type_catalog':[context_type],
            'context_type_charts':[context_type],
            'context_type_editorial_playlist':[context_type],
            'context_type_personalized_playlist':[context_type],
            'context_type_radio':[context_type],
            'context_type_user_collection':[context_type],
            'hist_user_behavior_reason_start':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_appload':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_backbtn':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_clickrow':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_endplay':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_fwdbtn':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_playbtn':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_remote':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_trackdone':[hist_user_behavior_reason_start],
            'hist_user_behavior_reason_start_trackerror':[hist_user_behavior_reason_start],

            'hist_user_behavior_reason_end':[hist_user_behavior_reason_end],
            'hist_user_behavior_reason_end_backbtn':[hist_user_behavior_reason_end],
            'hist_user_behavior_reason_end_clickrow':[hist_user_behavior_reason_end],
            'hist_user_behavior_reason_end_endplay':[hist_user_behavior_reason_end],
            'hist_user_behavior_reason_end_fwdbtn':[hist_user_behavior_reason_end],
            'hist_user_behavior_reason_end_logout':[hist_user_behavior_reason_end],
            'hist_user_behavior_reason_end_remote':[hist_user_behavior_reason_end],
            'hist_user_behavior_reason_end_trackdone':[hist_user_behavior_reason_end]})
           

            if df["week_day"].tolist()[0]=="Monday" :
                 df["week_day"] = 0
            elif df["week_day"].tolist()[0]=="Tuesday" :
                 df["week_day"] = 1
            elif df["week_day"].tolist()[0]=="Wednesday" :
                 df["week_day"] = 2
            elif df["week_day"].tolist()[0]=="Thursday" :
                 df["week_day"] = 3
            elif df["week_day"].tolist()[0]=="Friday" :
                 df["week_day"] = 4
            elif df["week_day"].tolist()[0]=="Saturday" :
                 df["week_day"] = 5
            else :
                 df["week_day"] = 6
           
            if df["context_type"].tolist()[0]=='catalog':
                 df["context_type_catalog"]=1
                 df['context_type_charts']=0
                 df['context_type_editorial_playlist']=0
                 df['context_type_personalized_playlist']=0
                 df['context_type_radio']=0
                 df['context_type_user_collection']=0
             

            elif df["context_type"].tolist()[0]=='charts':
                 df["context_type_catalog"]=0
                 df['context_type_charts']=1
                 df['context_type_editorial_playlist']=0
                 df['context_type_personalized_playlist']=0
                 df['context_type_radio']=0
                 df['context_type_user_collection']=0

            elif df["context_type"].tolist()[0]=='editorial playlist':
                 df["context_type_catalog"]=0
                 df['context_type_charts']=0
                 df['context_type_editorial_playlist']=1
                 df['context_type_personalized_playlist']=0
                 df['context_type_radio']=0
                 df['context_type_user_collection']=0

            elif df["context_type"].tolist()[0]=='personalized playlist':
                 df["context_type_catalog"]=0
                 df['context_type_charts']=0
                 df['context_type_editorial_playlist']=0
                 df['context_type_personalized_playlist']=1
                 df['context_type_radio']=0
                 df['context_type_user_collection']=0

            elif df["context_type"].tolist()[0]=='radio':
                 df["context_type_catalog"]=0
                 df['context_type_charts']=0
                 df['context_type_editorial_playlist']=0
                 df['context_type_personalized_playlist']=0
                 df['context_type_radio']=1
                 df['context_type_user_collection']=0
          
            else :
                 df["context_type_catalog"]=0
                 df['context_type_charts']=0
                 df['context_type_editorial_playlist']=0
                 df['context_type_personalized_playlist']=0
                 df['context_type_radio']=0
                 df['context_type_user_collection']=1

            if df["hist_user_behavior_reason_start"].tolist()[0]=='appload':
                 df["hist_user_behavior_reason_start_appload"]=1
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=0

            elif df["hist_user_behavior_reason_start"].tolist()[0]=='backbtn':
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=1
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=0
           
            elif df["hist_user_behavior_reason_start"].tolist()[0]=='clickrow':
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=1
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=0
            elif df["hist_user_behavior_reason_start"].tolist()[0]=='endplay':
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=1
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=0
            elif df["hist_user_behavior_reason_start"].tolist()[0]=='fwdbtn':
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=1
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=0
            elif df["hist_user_behavior_reason_start"].tolist()[0]=='playbtn':
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=1
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=0
            elif df["hist_user_behavior_reason_start"].tolist()[0]=='remote':
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=1
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=0
        
            elif df["hist_user_behavior_reason_start"].tolist()[0]=='trackdone':
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=1
                 df['hist_user_behavior_reason_start_trackerror']=0
            else :
                 df["hist_user_behavior_reason_start_appload"]=0
                 df['hist_user_behavior_reason_start_backbtn']=0
                 df['hist_user_behavior_reason_start_clickrow']=0
                 df['hist_user_behavior_reason_start_endplay']=0
                 df['hist_user_behavior_reason_start_fwdbtn']=0
                 df['hist_user_behavior_reason_start_playbtn']=0
                 df['hist_user_behavior_reason_start_remote']=0
                 df['hist_user_behavior_reason_start_trackdone']=0
                 df['hist_user_behavior_reason_start_trackerror']=1
          
           # END 

            if df["hist_user_behavior_reason_end"].tolist()[0]=='logout':
                 df["hist_user_behavior_reason_end_logout"]=1
                 df['hist_user_behavior_reason_end_backbtn']=0
                 df['hist_user_behavior_reason_end_clickrow']=0
                 df['hist_user_behavior_reason_end_endplay']=0
                 df['hist_user_behavior_reason_end_fwdbtn']=0
                 df['hist_user_behavior_reason_end_remote']=0
                 df['hist_user_behavior_reason_end_trackdone']=0
            elif df["hist_user_behavior_reason_end"].tolist()[0]=='backbtn':
                 df["hist_user_behavior_reason_end_logout"]=0
                 df['hist_user_behavior_reason_end_backbtn']=1
                 df['hist_user_behavior_reason_end_clickrow']=0
                 df['hist_user_behavior_reason_end_endplay']=0
                 df['hist_user_behavior_reason_end_fwdbtn']=0
                 df['hist_user_behavior_reason_end_remote']=0
                 df['hist_user_behavior_reason_end_trackdone']=0
            elif df["hist_user_behavior_reason_end"].tolist()[0]=='clickrow':
                 df["hist_user_behavior_reason_end_logout"]=0
                 df['hist_user_behavior_reason_end_backbtn']=0
                 df['hist_user_behavior_reason_end_clickrow']=1
                 df['hist_user_behavior_reason_end_endplay']=0
                 df['hist_user_behavior_reason_end_fwdbtn']=0
                 df['hist_user_behavior_reason_end_remote']=0
                 df['hist_user_behavior_reason_end_trackdone']=0
            elif df["hist_user_behavior_reason_end"].tolist()[0]=='endplay':
                 df["hist_user_behavior_reason_end_logout"]=0
                 df['hist_user_behavior_reason_end_backbtn']=0
                 df['hist_user_behavior_reason_end_clickrow']=0
                 df['hist_user_behavior_reason_end_endplay']=1
                 df['hist_user_behavior_reason_end_fwdbtn']=0
                 df['hist_user_behavior_reason_end_remote']=0
                 df['hist_user_behavior_reason_end_trackdone']=0
            elif df["hist_user_behavior_reason_end"].tolist()[0]=='fwdbtn':
                 df["hist_user_behavior_reason_end_logout"]=0
                 df['hist_user_behavior_reason_end_backbtn']=0
                 df['hist_user_behavior_reason_end_clickrow']=0
                 df['hist_user_behavior_reason_end_endplay']=0
                 df['hist_user_behavior_reason_end_fwdbtn']=1
                 df['hist_user_behavior_reason_end_remote']=0
                 df['hist_user_behavior_reason_end_trackdone']=0
            elif df["hist_user_behavior_reason_end"].tolist()[0]=='remote':
                 df["hist_user_behavior_reason_end_logout"]=0
                 df['hist_user_behavior_reason_end_backbtn']=0
                 df['hist_user_behavior_reason_end_clickrow']=0
                 df['hist_user_behavior_reason_end_endplay']=0
                 df['hist_user_behavior_reason_end_fwdbtn']=0
                 df['hist_user_behavior_reason_end_remote']=1
                 df['hist_user_behavior_reason_end_trackdone']=0
            else :
                 df["hist_user_behavior_reason_end_logout"]=0
                 df['hist_user_behavior_reason_end_backbtn']=0
                 df['hist_user_behavior_reason_end_clickrow']=0
                 df['hist_user_behavior_reason_end_endplay']=0
                 df['hist_user_behavior_reason_end_fwdbtn']=0
                 df['hist_user_behavior_reason_end_remote']=0
                 df['hist_user_behavior_reason_end_trackdone']=1         
            categorical_variables=['context_type','hist_user_behavior_reason_start','hist_user_behavior_reason_end']
            df = df.drop(categorical_variables, axis=1)
        
            result = status(df)
            return render(request, 'status.html', {"data": result}) 
            
    form=SkippedForm()
    return render(request, 'form.html', {'form':form})