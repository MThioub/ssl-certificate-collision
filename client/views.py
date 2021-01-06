from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .request_back import return_json
from .models import User
import json
#import engine
from engine.db_settings import PSYCOPG2_DATABASES
from engine.source import get_certificate_info_from_ip_adress
from engine.rsa.gcd import gcd

import psycopg2
"""
def search(Ip_adress):
   get_certificate_info_from_ip_adress(Ip_adress)
   modulus = get_certificate_info_from_ip_adress[0]
   encryption_algo =  get_certificate_info_from_ip_adress[1]


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
"""
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
    default_ip_adress_for_test = {"ip_adress": "104.84.61.159"}
    #print(request.method)
    if request.method != "POST":
        raise
    #parameters = [
    #{"name":"ip_adress", "type":"value", "required":True}
    #]
    #body_request = request.body.decode("utf-8")
    #body = json.loads(body_request)
    #ip_adress = readParameters(body_request, parameters)
    #print(request.text)
    ip_adress = default_ip_adress_for_test.get("ip_adress")
    #print(ip_adress)
    # get large integer

    large_encrypted_int, _ = get_certificate_info_from_ip_adress(ip_adress)

    #print("large encrypted int", large_encrypted_int)

    # connect to db and retrieve all large numbers regitered
    sql_select_ip_property = """SELECT modulus FROM ip_source;"""
    try:
        #print(PSYCOPG2_DATABASES)
        params = PSYCOPG2_DATABASES
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_select_ip_property)
        #print(cur.fetchall())
        list_large_int = (sql_tuple[0] for sql_tuple in cur.fetchall())
        #print(list_large_int)
        non_corrupted = True
        for large_num in list_large_int:
            # test if that element have a common
            # divisor with large_encrypted_int
            # test import engine.rsa
            boolean_common_divisor, common_divisor = gcd(int(large_num), large_encrypted_int)
            non_corrupted &= boolean_common_divisor
            if not non_corrupted:
                corrupted_common_divisor = common_divisor
                break
            #print(boolean_common_divisor)
            #print(type(large_num), type(large_encrypted_int))

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    print(corrupted_common_divisor)
    #result = 1
    #return return_json(1, {"non_corrupted": non_corrupted, "ccd": corrupted_common_divisor})
    return return_json(1, {"non_corrupted": non_corrupted})
