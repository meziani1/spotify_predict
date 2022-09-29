from django import forms
from .models import Skipped

class SkippedForm(forms.ModelForm):
    class Meta:
              model = Skipped
              fields = "__all__"

    session_position = forms.IntegerField()
    session_length= forms.IntegerField()
    no_pause_before_play= forms.IntegerField()
    hist_user_behavior_n_seekfwd=forms.IntegerField()
    hour_of_day=forms.IntegerField()
    premium = forms.IntegerField()
    hist_user_behavior_n_seekback=forms.IntegerField()
    week_day=forms.TypedChoiceField(choices=[('Monday','Monday'),('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),
    ('Friday', 'Friday'),('Saturday', 'Saturday'),('Sunday', 'Sunday')])
   
    context_type=forms.TypedChoiceField(choices=[('catalog','catalog'),('charts','charts'),
   ('editorial playlist','editorial playlist'),('personalized playlist',
   'personalized playlist'),('radio','radio'),('user collection','user collection')])
    hist_user_behavior_reason_start =forms.TypedChoiceField(choices=[('appload','appload')
    ,('backbtn','backbtn'),('clickrow','clickrow'),
    ('fwdbtn','fwdbtn'),('playbtn','playbtn'),('remote','remote'),
    ('trackdone','trackdone'),('trackerror','trackerror')])
    hist_user_behavior_reason_end=forms.TypedChoiceField(choices=[('backbtn','backbtn'),
    ('clickrow','clickrow'),('endplay','endplay'),('fwdbtn','fwdbtn'),
    ('logout','logout'),('remote','remote'),('trackdone','trackdone')])
    
            
