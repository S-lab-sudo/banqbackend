from django.shortcuts import HttpResponse,render
from django.http import JsonResponse
import json
from backend.models import Reservation,Reviews
from datetime import date
from email_validator import validate_email
from django.core.exceptions import ValidationError
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from email_validator import validate_email



def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


def home(request):
    return render("Working")


@csrf_exempt
def makeReservation(req):
    dataToSend={"success":False,"message":""}
    try:
        data=json.loads(req.body)
        name,phonenumber,dateofvisit,purposeofvisit,description,hallno=data.values()
    # Security conditioning
        if(len(name)<7|len(name)>100):
            data["message"]="Please Enter Valid or Personal Username"
            return JsonResponse(dataToSend)
        if(len(phonenumber)<10):
            data["message"]="Please Enter Valid or Personal Phone Number"
            return JsonResponse(dataToSend)
        # TODO CREATE A CONDITION THAT WILL CHECK IF THE TIME IS AVAILABLE OR NOT IN THE SAME DATE
        Reserve=Reservation(name=name,phonenumber=phonenumber,dateofvisit=dateofvisit,purposeofvisit=purposeofvisit,description=description,hallno=hallno)
        Reserve.save()
        dataToSend["message"]="Your reservation has been completed"
        dataToSend["success"]=True
        return JsonResponse(dataToSend)
    except Exception as e:
        print(e)
        dataToSend["message"]="An error Occured"    
        dataToSend["success"]=False    
        return JsonResponse(dataToSend)



@csrf_exempt
def getAvailableDates(req):
    data=json.loads(req.body)
    today = date.today()
    reservations = Reservation.objects.filter(dateofvisit__gte=today).values("dateofvisit","hallno")
    total=list(reservations)
    return JsonResponse(total, safe=False)


@csrf_exempt
def addreviews(req):
    dataToSend={"success":False,"message":""}
    try:
        data=json.loads(req.body)
        username,emailaddress,stars,description=data.values()
        if len(username)<7 or len(username)>100:
            dataToSend["message"] = "Please Enter Valid or Personal Username"
            print("I am logging")
            return JsonResponse(dataToSend)
        if not validate_email(emailaddress):
            dataToSend["message"]="Please Enter Valid Email Address"
            return JsonResponse(dataToSend)
        SaveReviews=Reviews(username=username,emailaddress=emailaddress,stars=stars,description=description)
        SaveReviews.save()
        dataToSend["message"]="Your review has been added"
        dataToSend["success"]=True
        return JsonResponse(dataToSend,safe=False)
    except Exception as e:
        print(e)
        dataToSend["message"]="An error Occured"
        dataToSend["success"]=False
        return JsonResponse(dataToSend)
    
def getreviews(req):
    try:
        reviews = Reviews.objects.all().values("username", "stars", "description")
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse(list(reviews), safe=False)