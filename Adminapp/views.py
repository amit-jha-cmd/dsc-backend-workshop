from django.shortcuts import render
from .models import Questions as Question
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json



