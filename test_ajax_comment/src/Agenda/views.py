from django.shortcuts import render
from django.http import JsonResponse 
from .models import Events
 
 
# Create your views here.
def index(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'calendar/index.html',context)




def all_events(request):
    all_events = Events.objects.all()
    print(all_events)
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M"),
        })

    return JsonResponse(out, safe=False)


def vue_calendar(request):  
    all_events = Events.objects.all()
    context = {
        "simple_events_vue":all_events,
    }
    return render(request,'calendar/vue_calendar.html',context)

def all_events_vue(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M"),
        })

    return JsonResponse({'events': out}, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
