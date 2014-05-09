from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader	
from django.http import HttpResponseRedirect
from parse_tool import *

def index(request):
	context = {'snippets_list': 'test'}
	return render(request, 'index.html', context)
	#return HttpResponse(TEMPLATE_DIRS)
def parse(request):
	url_name = request.POST['url_name']
	skip_rows = request.POST['skip_rows']
	print url_name
	#skip_rows = request.POST['skip_rows']
	#print skip_rowsx
	out = parse_csv_url(url_name, '')
	return HttpResponse(parse_csv_url(url_name, ''))