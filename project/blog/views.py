from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import FeedbackForm

def index(request):
	form = FeedbackForm()
	data = { "form": form }
	return render(request, 'base.html', data)