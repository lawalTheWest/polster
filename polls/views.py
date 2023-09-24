from django.shortcuts import render

from .models import Questions, Choice

'''Get question and display them'''
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
