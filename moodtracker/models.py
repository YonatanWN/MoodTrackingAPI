from django.db import models
from django.forms import ModelForm
import datetime
# Create your models here.


class MoodInput(models.Model):
    user = models.ForeignKey('auth.User', related_name="moodinputs", on_delete=models.CASCADE)
    date = models.DateField()
    mood = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    streak = models.IntegerField(default=1)



class MoodForm(ModelForm):
    class Meta:
        model = MoodInput
        fields= ['mood', 'description']
    def save(self, user,commit=True):
        m = super(ModelForm, self).save(commit=False)
        m.user = user
        m.date =datetime.datetime.now()
        if commit:
            m.save()
        return m
