from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader	
from django.http import HttpResponseRedirect
from parse_tool import *
from xml2json_parser import *

def index(request):
	context = {'content_list': 'value'}
	return render(request, 'index.html', context)

def xml(request):
    context = {'content_list': 'value'}
    return render(request, 'index_xml.html', context)

def parse(request):
	url_name = request.POST['url_name']
	skip_rows = request.POST['skip_rows']
	print url_name
	print skip_rows
	return HttpResponse(parse_csv_url(url_name, skip_rows))

def xmlparse(request):
    url_name = request.POST['url_name']
    xml_type = request.POST['xml_type']
    print url_name
    print xml_type
    return HttpResponse(url_parse(url_name, xml_type))