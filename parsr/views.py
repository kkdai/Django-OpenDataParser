from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader	
from django.http import HttpResponseRedirect
#import os

def index(request):
	context = {'snippets_list': 'test'}
	return render(request, 'index.html', context)
	#return HttpResponse(TEMPLATE_DIRS)
def parse(request):
	return HttpResponse("test!")