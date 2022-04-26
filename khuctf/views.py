from django.shortcuts import render


def index(request):
	context = { 'test' : 'test',
	}
	return render(request, 'index.html', context=context)

def qna(request):
	context = { 'test' : 'test',
	}
	return render(request, 'qna.html', context=context)

def scoreboard(request):
	context = { 'test' : 'test',
	}
	return render(request, 'scoreboard.html', context=context)

def challenges(request):
	context = { 'test' : 'test',
	}
	return render(request, 'challenges.html', context=context)