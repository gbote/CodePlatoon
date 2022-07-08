from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def home(request):
  return render(request, 'pages/home.html')


def create_event(request):
  context = {}
  form = EventForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect('events:view_all_events')

  context['form'] = form
  return render(request, 'pages/create_event.html', context)



def view_all_events(request):
  context = {
    "events" : Event.objects.all()
  }
  return render(request, 'pages/view_all_events.html', context)


def view_event(request, id):
  context = {
    'event' : Event.objects.get(pk=id)
  }
  return render(request, 'pages/view_event.html', context)


def edit_event(request, id):
  context = {}
  form = EventForm(request.POST or None, request.FILES or None, instance=Event.objects.get(pk=id))

  if form.is_valid():
    form.save()
    return redirect('events:view_all_events')

  context['form'] = form
  return render(request, 'pages/edit_event.html', context)


def delete_event(request, id):
  event = Event.objects.get(pk=id)
  event.delete()
  return redirect('events:view_all_events')

