from django.urls import path
from khuctf import views


urlpatterns = [
	path('', views.index, name='index'),
	path('qna.html', views.qna, name='qna'),
 	path('scoreboard.html', views.qna, name='scoreboard'),
	path('challenges.html', views.qna, name='challenges'),
]
