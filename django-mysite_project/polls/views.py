from django.http import HttpResponse, HttpResponseRedirect # brings in the ability to redirect the user
from django.shortcuts import render
from django.urls import reverse # The reverse library gives us the ability to read the previous URL and just use reverse in our code so that we don't need to hard code the URL

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

def get_question(question_id):
    # this is a helper method we've created since we need to find the question in detail(), results(), and vote()
    return latest_question_list[question_id - 1]

def index(request):
    data = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    question = latest_question_list[question_id-1]
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = latest_question_list[question_id-1]
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = latest_question_list[question_id-1]
    selected_choice = question['choices'][int(request.POST['choice'])-1] # find the choice that the user submitted in the form
    selected_choice['votes'] += 1 # add 1 to the number of votes for that selected choice
    return HttpResponseRedirect(reverse('polls:results', args=(question['id'],)))
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.