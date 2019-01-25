from django.shortcuts import render

def index(request):
	return render(request, 'emoR/home.html')

def smartbot(request):
	return render(request, 'emoR/smartbot.html')	
