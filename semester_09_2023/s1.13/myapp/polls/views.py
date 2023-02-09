from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from polls.models import Question


def index(request):
    response = []

    # for question in Question.objects.all():
    #     response.append({
    #         "title": question.question_text,
    #         "publish_date": question.pub_date
    #     })

    context = {
        "question_list": Question.objects.all()
    }

    return render(request, 'index.html', context)
