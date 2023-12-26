from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseServerError, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


# Vue de creation du sondage
@login_required
def create_poll(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        answers = request.POST.getlist('answers')

        #Verifions si la question et au moins une reponses sont presentes
        if question_text and answers:
            question_obj = Question.objects.create(
                user=request.user,
                question_text=question_text,
            )

            for answer in answers:
                Answer.objects.create(answer_text=answer, question=question_obj)

            messages.info(request, 'Sondage créé')
            return render(request, 'question/create_poll.html')
        else:
            messages.error(request, 'Saisir au moins une reponses')

    return render(request, 'question/create_poll.html')



# affichage de la liste de sondage
@login_required
def liste_sondage_admin(request):
    try:
        questions = Question.objects.filter(user=request.user)
        return render(request ,'question/liste_sondage_admin.html' ,{'questions' : questions})
    except Exception as e:
        print("une erreur s'est produite: {}".format(e))
        return HttpResponseServerError("Une erreur s'est produite lors de la recuperation des sondages.")


# vote des elements du sondage
@login_required
@require_POST
def vote(request):
    if request.POST.get('action') == 'post':
        question_uid = request.POST.get('question_uid')
        answer_uid = request.POST.get('answer_uid')

        # Vérifiez si la question et la réponse existent
        question = get_object_or_404(Question, uid=question_uid)
        answer = get_object_or_404(Answer, uid=answer_uid)

        # Vérifiez si l'utilisateur a déjà voté pour cette question
        if question.answers.filter(voters=request.user).exists():
            question.answers.remove(request.user)
            answer.counter -= 1
            result = answer.counter
        else:
            question.answers.add(request.user)
            answer.counter += 1
            result = answer.counter

        question.save()
        answer.save()

        return JsonResponse({'result': result, 'message': 'Votre vote a été enregistré avec succès.'})

    return JsonResponse({'result': 'error', 'message': 'Mauvaise requête.'})






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

    # Récupération des données de la requête
    data = request.data
    question_uid = data.get('question_uid')
    answer_uid = data.get('answer_uid')

    # Vérification que les deux identifiants sont présents dans les données
    if question_uid is None and answer_uid is None:
        payload = {'data' : 'L\'identifiant de la question et l\'identifiant de la réponse sont tous deux requis.' , 'status' : False}
        return Response(payload)

    try:
        # Récupération des objets Question et Answers correspondants aux identifiants
        question_obj = Question.objects.get(uid = question_uid)
        answer_obj  = Answer.objects.get(uid = answer_uid)

    except ObjectDoesNotExist:
        # Gestion de l'exception si l'un des objets n'existe pas
        payload = {'data': 'Id de la question Invalide ou Id de la reponse invalid', 'status': False}
        return Response(payload)

    # Incrémentation du compteur de la réponse
    answer_obj.counter += 1
    answer_obj.save()

    # Calcul du pourcentage et préparation de la réponse
    payload = {'data' : question_obj.calculate_percentage() , 'status' : True}

    # Envoi de la réponse
    return Response(payload)


@login_required
def question_detail(request , question_uid):
    try:
        question_obj = Question.objects.get(uid = question_uid)
        context = {'question' : question_obj}
        return render(request , 'question.html' , context)

    except Exception as e :
        print(e)