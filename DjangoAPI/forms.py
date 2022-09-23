from django import forms
from .models import Skipped

class SkippedForm(forms.ModelForm):
    class Meta:
              model = Skipped
              fields = "__all__"

    not_skipped = forms.IntegerField()
    no_pause_before_play = forms.IntegerField()
    context_type_user_collection =forms.IntegerField()
    hist_user_behavior_reason_start_fwdbtn=forms.IntegerField()
    hist_user_behavior_reason_start_trackdone=forms.IntegerField()
    hist_user_behavior_reason_end_backbtn=forms.IntegerField()
    hist_user_behavior_reason_end_fwdbtn=forms.IntegerField()
    hist_user_behavior_reason_end_trackdone=forms.IntegerField()
    mode_0=forms.IntegerField()
    week_day_Monday=forms.IntegerField()