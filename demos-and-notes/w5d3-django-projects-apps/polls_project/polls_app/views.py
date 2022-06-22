from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

latest_question_list = [
    {
        'id' : 1,
        'question_text': 'whats up',
        'pub_date':'2022-01-04',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
    {
        'id' : 2,
        'question_text': 'whats new',
        'pub_date':'2022-02-09',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
]

# Create your views here.
def index(request):
    # query the database to get the question_list
    # the keys on our data object can be accessed from the template
    data = { 'latest_question_list': latest_question_list, 'foo':'bar' }
    response = render(request, 'polls_app/index.html', data)
    response.status_code = 418
    print(response)
    return response

def detail(request, question_id):
    question = latest_question_list[question_id-1]
    return render(request, 'polls_app/detail.html', {'question': question})

def results(request, question_id):
    question = latest_question_list[question_id-1]
    return render(request, 'polls_app/results.html', {'question': question})

def vote(request, question_id):
    question = latest_question_list[question_id-1]
    selected_choice = question['choices'][int(request.POST['choice']) -1]
    selected_choice['votes'] += 1
    return HttpResponseRedirect(f'/polls/{question_id}/results')
