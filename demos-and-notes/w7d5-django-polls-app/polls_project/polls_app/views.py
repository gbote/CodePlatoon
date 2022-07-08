from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice
from django.utils import timezone

# Create your views here.
def get_question(question_id):
    return Question.objects.get(id = question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = {'latest_question_list': latest_question_list}

    return render(request, 'polls_app/index.html', data)

def detail(request, question_id):
    question = get_question(question_id)

    # data = {'question': question}
    return  render(request, 'polls_app/detail.html', {'question': question})

def results(request, question_id):
    question = get_question(question_id)

    return render(request, 'polls_app/results.html', {'question': question})

def vote(request, question_id):
    question = get_question(question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        data = {'question': question,
                'error_message': "You didn't select a choice.",}
        return render(request, 'polls_app/detail.html', data)
    
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(f'/polls/{question_id}/results')



# for demo
def add_question(request, question_text):
    question = Question(question_text = question_text, pub_date= timezone.now())
    question.save()

    question.choice_set.create(choice_text='Not much')
    question.choice_set.create(choice_text='The sky', votes= 0)
    question.choice_set.create(choice_text='nothing at all')

    choices = question.choice_set.all()
    return HttpResponse(choices)

