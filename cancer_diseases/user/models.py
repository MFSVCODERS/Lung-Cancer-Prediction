from django.db import models

# Create your models here.
class Register(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=67)
    password=models.CharField(max_length=67)
    username=models.CharField(max_length=89)

class lungcancerdata(models.Model):
    Age=models.IntegerField()
    Gender=models.IntegerField()
    Air_Pollution=models.IntegerField()
    Alcohol_Use=models.IntegerField()
    Dust_Allergy=models.IntegerField()
    OccuPational_Hazards=models.IntegerField()
    Genetic_Risk=models.IntegerField()
    Chronic_Lung_Disease=models.IntegerField()
    Balanced_Diet=models.IntegerField()
    Obesity=models.IntegerField()
    Smoking=models.IntegerField()
    Passive_Smoker=models.IntegerField()
    Chest_Pain=models.IntegerField()
    Coughing_Of_Blood=models.IntegerField()
    Fatigue=models.IntegerField()
    Weight_Loss=models.IntegerField()
    Shortness_Of_Breath=models.IntegerField()
    Wheezing=models.IntegerField()
    Swallowing_Difficulty=models.IntegerField()
    Clubbing_Of_Finger_Nails=models.IntegerField()
    Frequent_Cold=models.IntegerField()
    Dry_Cough=models.IntegerField()
    Snoring=models.IntegerField()







