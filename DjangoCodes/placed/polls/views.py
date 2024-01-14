from django.shortcuts import render
import numpy as np
import pandas as pd
from polls.forms import Placement
from .models import *
from django.contrib.auth.models import User
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import svm


def Predict(request):

    dataset = pd.read_csv('static/collegePlace.csv')
    X = dataset[['Internships','CGPA','Hostel','HistoryOfBacklogs']]
    Y =dataset['PlacedOrNot']

    value = ''

    if request.method == 'POST':

        # age, sex, cp = map(float, request.POST.get())

        internship = float(request.POST['Internships'])
        cgpa = float(request.POST['CGPA'])
        hostel = float(request.POST['Hostel'])  # chest pain
        backlog = float(request.POST['HistoryOfBacklogs'])  # resting blood pressure
        

        user = Place(Internship=internship , CGPA = cgpa, Hostel=hostel, HistoryOfBacklogs=backlog)
        user.save()

        user_data = np.array(
            (internship,cgpa,hostel,backlog)
        ).reshape(1, 4)

        print(user_data)

        rf = svm.SVC(probability=True)

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        
        X_train , X_test,Y_train,Y_test = train_test_split(X, Y,test_size = 0.3)

        predictions = rf.predict(X_test)

        confidence_scores = rf.predict_proba(user_data)

        class_1_probability = (confidence_scores[0][1]*100)

        X = np.nan_to_num(X)
        
        # calculated_prediction = int(predictions[0])
        #Model Accuracy Score
        Accuracy = accuracy_score(Y_test,predictions)
        print("Accuracy Score: ",Accuracy*100,"%")
        # value = 'will' if calculated_prediction == 1 else "will not"

        value = class_1_probability

        # print(classProbability)
        # class_1_probability = str(class_1_probability)
        # perc = class_1_probability
        # if int(predictions[0]) == 1:
        #     value = 'have'
        # elif int(predictions[0]) == 0:
        #     value = "don\'t have"

    return render(request,
                  'Predict.html',
                  {
                      'result': value,                  
                      'title': 'Placement Prediction',
                      'active': 'btn btn-success peach-gradient text-black',
                      'heart': True,
                      'form': Placement(),
                  })


def home(request):

    name = Place.objects.all()

    return render(request,
                  'home.html', {'name': name})


def handler404(request):
    return render(request, '404.html', status=404)
