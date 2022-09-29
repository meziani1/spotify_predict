from django.db import models

# Create your models here.

class Skipped(models.Model ):
    DAY_CHOICES = (('Monday','Monday'),('Tuesday', 'Tuesday'),('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),
    ('Friday', 'Friday'),('Saturday', 'Saturday'),('Sunday', 'Sunday'))
    CONTEXT_CHOICES=(('catalog','catalog'),('charts','charts'),('editorial playlist',
    'editorial playlist'),('personalized playlist','personalized playlist'),
    ('radio','radio'),('user_collection','user_collection'))
    START_CHOICES=(('appload','appload'),('backbtn','backbtn'),('clickrow','clickrow'),
    ('clickrow','clickrow'),('fwdbtn','fwdbtn'),('playbtn','playbtn'),
    ('remote','remote'),('trackdone','trackdone'),('trackerror','trackerror'))
    END_CHOICES=(('backbtn','backbtn'),('clickrow','clickrow'),('endplay','endplay'),
    ('fwdbtn','fwdbtn'),('logout','logout'),('remote','remote'),('trackdone','trackdone'))
    session_position = models.IntegerField()
    session_length=models.IntegerField()
    no_pause_before_play =models.IntegerField()
    hist_user_behavior_n_seekfwd=models.IntegerField()
    hour_of_day=models.IntegerField()
    premium = models.IntegerField()
    hist_user_behavior_n_seekback=models.IntegerField()
    week_day=models.CharField(max_length=10, choices=DAY_CHOICES)
    context_type=models.CharField(max_length=35, choices=CONTEXT_CHOICES)
    hist_user_behavior_reason_start=models.CharField(max_length=35, choices=START_CHOICES)
    hist_user_behavior_reason_end=models.CharField(max_length=35, choices=END_CHOICES)
    
    def __str__(self):
            return self.week_day, self.context_type ,self.hist_user_behavior_reason_start,self.hist_user_behavior_reason_end 