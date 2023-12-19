from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import *
from .forms import *

@login_required
def index(request):
    polls = Sondagechoix.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sondages:index')
    else:
        form = CreatePollForm()
    context = {'form': form}
    return render(request, 'polls/create.html', context)

@login_required
def detail(request):
    context = {}
    return render(request, 'polls/detail.html', context)


@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Sondagechoix, pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST.get('poll')

        if selected_option in ['option1', 'option2', 'option3']:
            if selected_option == 'option1':
                poll.option_one_count += 1
            elif selected_option == 'option2':
                poll.option_two_count += 1
            elif selected_option == 'option3':
                poll.option_three_count += 1

            poll.save()
            return redirect('sondages:results', poll_id)
        else:
            return HttpResponse('Invalid option', status=400)

    context = {'poll': poll}
    return render(request, 'polls/vote.html', context)


@login_required
def results(request, poll_id):
    poll = get_object_or_404(Sondagechoix, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})


@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Sondagechoix, pk=poll_id)
    poll.delete()
    return redirect('sondages:index')

@login_required
def update_poll(request, poll_id):
    poll = get_object_or_404(Sondagechoix, pk=poll_id)
    if request.method == 'POST':
        form = CreatePollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            return redirect('sondages:index')
    else:
        form = CreatePollForm(instance=poll)
    context = {
        'form': form,
        'poll': poll,
    }
    return render(request, 'polls/update.html', context)