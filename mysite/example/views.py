from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

# Create your views here.

def example_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			jsob = {"demo": "12345", "var": "The Count s:"}
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)
			index = 0
			for i in jsob["demo"]:
				index += 1
			index = jsob["var"]+str(index)

			return JsonResponse({"count":index})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h2>ONLY POST MALONES</h2>")

@csrf_exempt
def fib(request):
	jsob = {"startNumber": 0, "length": 10} #DEFAULTS
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)
			#Anything above this line is essential

			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			loop = range(length)

			numarray = []
			fibno = startNumber
			addno = 1
			for l in loop:
				numarray.append(fibno)
				fibno = fibno+addno
				addno = fibno-addno

			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h2>I don't feel so good..</h2>")

@csrf_exempt
def leg(request):
	jsob = {"startNumber": 0, "length": 10} #DEFAULTS
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)
			#Anything above this line is essential

			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			loop = range(length)

			numarray = []
			fibno = startNumber
			addno = 1
			for l in loop:
				numarray.append(fibno)
				fibno = fibno+addno
				addno = fibno-addno

			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("bbobbo")