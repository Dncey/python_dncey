from diango.http import HttpResopnse
from django.shortcuts import redirect


def index(request):
	return HttpResponse('index')

def login(request):

	return redirect('/inedx')
