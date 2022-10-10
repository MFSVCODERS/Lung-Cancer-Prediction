import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import Register

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from .models import lungcancerdata



def home(request):
    return render(request,"index.html")

def prediction(request):
    return render(request,"prediction.html")

def login(request):
    if request.method == 'POST':
        #v = DoctorReg.objects.all()
        user = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'prediction.html')
        else:
            messages.info(request, 'Invalid credentials !!')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    global User
    if request.method=='POST':
        f_n=request.POST.get('fname')
        l_n=request.POST.get('lname')
        email=request.POST.get('email')
        user_n=request.POST.get('uname')
        pwd1=request.POST.get('pwd1')
        pwd2=request.POST.get('pwd2')
        if pwd1==pwd2:
            if User.objects.filter(username=user_n).exists():
                messages.info(request,"Username exists")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists(): 
                 messages.info(request,"email exists")
                 return render(request,"register.html")  
            else:
                User=User.objects.create_user(first_name=f_n,last_name=l_n,username=user_n,email=email,password=pwd1)
                User.save()
                return render(request,'login.html')
        else:
            messages.info(request,"Password not matching")
            return render("register.html")
    
    return render(request,"register.html")


def lungcancer(request):
    return render(request,'lcancer.html')

def Predictlung(request):
    if (request.method == 'POST'):
        age=request.POST['age']
        gender=request.POST['gender']
        airpollution=request.POST['airpollution']
        alcoholuse=request.POST['alcoholuse']
        dustallergy = request.POST['dustallergy']
        occupationalhazards=request.POST['occupationalhazards']
        geneticrisk= request.POST['geneticrisk']
        chroniclungdisease=request.POST['chroniclungdisease']
        balanceddiet=request.POST['balanceddiet']
        obesity= request.POST['obesity']
        smoking=request.POST['smoking']
        passivesmoker=request.POST['passivesmoker']
        chestpain=request.POST['chestpain']
        coughingofblood=request.POST['coughingofblood']
        fatigue=request.POST['fatigue']
        weightloss=request.POST['weightloss']
        shortnessofbreath=request.POST['shortnessofbreath']
        wheezing=request.POST['wheezing']
        swallowingdifficulty=request.POST['swallowingdifficulty']
        clubbingoffingernails = request.POST['clubbingoffingernails']
        frequentcold=request.POST['frequentcold']
        dry_cough = request.POST['drycough']
        snoring= request.POST['snoring']

        df = pd.read_csv(r"static/datasets/Lung_cancer.csv")
        df.dropna(inplace=True)
        df.isnull().sum()
        X_train = df[['Age','Gender','Air_Pollution','Alcohol_Use','Dust_Allergy','OccuPational_Hazards','Genetic_Risk','Chronic_Lung_Disease','Balanced_Diet','Obesity',
                      'Smoking','Passive_Smoker','Chest_Pain','Coughing_Of_Blood','Fatigue','Weight_Loss','Shortness_Of_Breath','Wheezing','Swallowing_Difficulty','Clubbing_Of_Finger_Nails',
                      'Frequent_Cold','Dry_Cough','Snoring']]
        y_train = df[['Level']]
        ran = RandomForestClassifier()
        ran.fit(X_train,y_train)
        prediction = ran.predict([[age,gender,airpollution,alcoholuse,dustallergy,occupationalhazards,geneticrisk,chroniclungdisease,balanceddiet,obesity,smoking,passivesmoker,chestpain,coughingofblood,fatigue,
                                   weightloss,shortnessofbreath,wheezing,swallowingdifficulty,clubbingoffingernails,frequentcold,dry_cough,snoring]])
        lungcancer=lungcancerdata.objects.create(Age=age,Gender=gender,Air_Pollution=airpollution,Alcohol_Use=alcoholuse,Dust_Allergy=dustallergy,OccuPational_Hazards=occupationalhazards,Genetic_Risk=geneticrisk,
                                                 Chronic_Lung_Disease=chroniclungdisease,Balanced_Diet=balanceddiet,Obesity=obesity,Smoking=smoking,Passive_Smoker=passivesmoker,Chest_Pain=chestpain,Coughing_Of_Blood=coughingofblood,
                                                 Fatigue=fatigue,Weight_Loss=weightloss,Shortness_Of_Breath=shortnessofbreath,Wheezing=wheezing,Swallowing_Difficulty=swallowingdifficulty,Clubbing_Of_Finger_Nails=clubbingoffingernails,
                                                 Frequent_Cold=frequentcold,Dry_Cough=dry_cough,Snoring=snoring)
        lungcancer.save()
        return render(request,'lungpredict.html',
                      {"lungcancer": prediction,'age':age,'gender':gender,'airpollution':airpollution,'alcoholuse':alcoholuse,'dustallergy':dustallergy,'occupationalhazards':occupationalhazards,'geneticrisk':geneticrisk,'chroniclungdisease':chroniclungdisease,'balanceddiet':balanceddiet,'obesity':obesity,'smoking':smoking,'passivesmoker':passivesmoker,'chestpain':chestpain,'coughingofblood':coughingofblood,'fatigue':fatigue,
                                   'weightloss':weightloss,'shortnessofbreath':shortnessofbreath,'wheezing':wheezing,'swallowingdifficulty':swallowingdifficulty,'clubbingoffingernails':clubbingoffingernails,'frequentcold':frequentcold,'dry_cough':dry_cough,'snoring':snoring })
    else:
        return render(request, 'lungpredict.html')






