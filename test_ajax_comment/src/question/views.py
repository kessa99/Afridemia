from django.shortcuts import render, redirect
from .models import Question, Answers
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_poll(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        answers = request.POST.getlist('answers')

        question_obj = Question.objects.create(
            user=request.user,
            question_test=question_text,
        )

        for answer in answers:
            Answers.objects.create(answers_text=answer, question=question_obj)

        messages.info(request, 'Sondage créé')
        return render(request, 'question/create_poll.html')

    return render(request, 'question/create_poll.html')


@login_required
def liste_sondage_admin(request):
    questions = Question.objects.filter(user = request.user)
    return render(request ,'question/liste_sondage_admin.html' ,{'questions' : questions})


@login_required
def detail_answers(request, question_uid):
    try:
        question_obj = Question.objects.filter(uid=question_uid, user=request.user)
        context = {'question': question_obj}
        return render(request, 'question/see_ansswers.html', context)
    except Question.DoesNotExist:
        return redirect('question:liste_sondage_admin')
    except Exception as e:
        print(e)
        return redirect('question:liste_sondage_admin')



@login_required
@api_view(['POST'])
@csrf_exempt
def save_question_result(request):
    data = request.data
    question_uid = data.get('question_uid')
    answer_uid = data.get('answer_uid')

    if question_uid is None and answer_uid is None:
        payload = {'data' : 'both question uid and answer uid are required' , 'status' : False}

        return Response(payload)

    question_obj = Question.objects.get(uid = question_uid)
    answer_obj  = Answers.objects.get(uid = answer_uid)
    answer_obj.counter += 1
    answer_obj.save()

    payload = {'data' : question_obj.calculate_percentage() , 'status' : True}

    return Response(payload)

@login_required
def question_detail(request , question_uid):
    try:
        question_obj = Question.objects.get(uid = question_uid)
        context = {'question' : question_obj}
        return render(request , 'question.html' , context)

    except Exception as e :
        print(e)