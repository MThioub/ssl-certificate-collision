from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .request_back import return_json
from .models import User
import json


def readParameters(jsonObject, expectedParams):
    parameters = []
    for parameter in expectedParams:
        current = None
        if parameter["name"] in jsonObject:
            current = jsonObject[parameter["name"]]
        elif parameter["required"]:
            raise MissingParameterException(
                "Missing parameter {}".format(parameter["name"])
            )
        parameters.append(current)
    for parameter in jsonObject:
        if parameter not in [o["name"] for o in expectedParams]:
            raise InvalidParameterException("Invalid parameter {}".format(parameter))
    if len(parameters) == 1:
        return parameters[0]
    return parameters

# for file uploader
@csrf_exempt
def user(request, token):
    if request.method != "GET":
        raise
    users = User.objects.all()
    print(users)
    result = user_email = users[0].email

    return return_json(1, result)


@csrf_exempt
def search_collision(request, token):
    #print(request.method)
    if request.method != "POST":
        raise
    parameters = [
    {"name":"ip_adress", "type":"value", "required":True}
    ]
    body_request = request.body.decode("utf-8")
    body = json.loads(body_request)
    #ip_adress = readParameters(body_request, parameters)
    #print(request.text)
    result = 1

    return return_json(1, result)
