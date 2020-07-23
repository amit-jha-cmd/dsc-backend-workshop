from django.shortcuts import render
from .models import Questions as Question
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

@csrf_exempt
def connect(request):
    res = {
        "message": "SUCCESS",
        "payload": {}
    }

    res = json.dumps(res)
    res = json.loads(res)
    return JsonResponse(res, safe=False)

@csrf_exempt
def questions(request):
    res = {
        "message": "",
        "payload": {}
    }

    if(request.method == "POST"):
        content = json.loads(request.body.decode('utf-8')) # required
        question = Question(question = content["question"],
                            answer = content["answer"])
        question.save()
        res["message"] = "SUCCESS"

    else:
        res["message"] = "FAIL"

    res = json.dumps(res)
    res = json.loads(res)


    return JsonResponse(res, safe=False)

@csrf_exempt
def start(request):
    res = {
        "message": "",
        "payload": {}
    }

    if(request.method == "GET"):
        question = Question.objects.all().values("qn", "question")
        res["message"] = "SUCCESS"
        res["payload"] = json.loads(json.dumps(question[0]))

    else:
        res["message"] = "FAIL"

    res = json.dumps(res)
    res = json.loads(res)


    return JsonResponse(res, safe=False)

@csrf_exempt
def submit(request, qn, ans):
    res = {
        "message": "",
        "payload": {}
    }

    if(request.method == "GET"):
        question = Question.objects.filter(qn = qn).values("qn", "question", "answer")
        if(question[0]["answer"] == ans):
            res["message"] = "SUCCESS"
            q =  Question.objects.all().values("qn", "question")
            if(len(q) == qn):
                res["message"] = "COMPLETE"
            else:
                res["message"] = "SUCCESS"
                res["payload"] = json.loads(json.dumps(q[qn]))
        else:
            res["message"] = "INCORRECT"
            res["payload"] = json.loads(json.dumps(question[0]))

    else:
        res["message"] = "FAIL"

    res = json.dumps(res)
    res = json.loads(res)


    return JsonResponse(res, safe=False)

