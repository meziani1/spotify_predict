from django.db import models

# Create your models here.

class Skipped(models.Model ):
    not_skipped = models.IntegerField()
    no_pause_before_play = models.IntegerField()
    context_type_user_collection =models.IntegerField()
    hist_user_behavior_reason_start_fwdbtn=models.IntegerField()
    hist_user_behavior_reason_start_trackdone=models.IntegerField()
    hist_user_behavior_reason_end_backbtn=models.IntegerField()
    hist_user_behavior_reason_end_fwdbtn=models.IntegerField()
    hist_user_behavior_reason_end_trackdone=models.IntegerField()
    mode_0=models.IntegerField()
    week_day_Monday=models.IntegerField()
