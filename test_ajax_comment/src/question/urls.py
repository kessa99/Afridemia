from django.urls import path, include
from .views import (
   question_detail,
   create_poll,
   liste_sondage_admin,
   save_question_result,
   save_question_result,
   detail_answers,
)

app_name = 'question'
urlpatterns = [
    path('<uuid:question_uid>/', question_detail, name='question_detail'),
    path('create_poll/' , create_poll , name="create_poll"),
    path('liste_sondage_admin/' , liste_sondage_admin , name="liste_sondage_admin"),
    path('detail_answers/<question_uid>' , detail_answers , name="detail_answers"),
    path('question/<question_uid>/' , question_detail , name="question_detail"),
    path('api/save_question_result/' , save_question_result),
    path('save_question_result/', save_question_result, name='save_question_result'),
    path('api-auth/', include('rest_framework.urls'))
]