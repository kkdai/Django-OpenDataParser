
# -*- coding: utf-8 -*-
import urllib2, urllib
import os
import csv  
import json
import requests
import sys

try:
    from pyquery import PyQuery as pq
except ImportError:
    print "pip install pyquery"
    sys.exit(1)

'''
Need reset system to utf8 encode way to if we want to decode big5 string
http://legacy.python.org/dev/peps/pep-0263/
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"
'''
Force decode for string codec.
'''
def force_decode(string, codecs=['utf8', 'big5']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
            pass
'''
Force encoding  for string codec.
'''
def force_encode_json(json_content, json_encode = ['utf8', 'big5']):
    for i in json_encode:
           try:
              return json.dumps(json_content, encoding=i)
           except:
              pass

def parse_cvs_to_json(handle_f, skip_lines):
    print skip_lines
    skip_list = []
    for i in skip_lines.split(' '):
        print i
    change_index = 0
    rows = []
    out = []
    for row in csv.reader(handle_f):
        if str(change_index) not in skip_lines.split(' '):  #uncomment to skip what you don't want.
            #print force_decode(row[1])
            rows.append(row)
        else:
            print "skip in " + str(change_index)
        change_index += 1
    out = force_encode_json(rows)
    return out

def parse_file(source_type, source_file, skip_lines):
    if source_type == 'csv':
        f = open(source_file, 'r')
        return parse_cvs_to_json(f, skip_lines)

def parse_url(source_type, source_address, skip_lines):
    if source_type == 'csv':
        #Use request.get to deal with very long URL.
        f = requests.get(source_address)
        return parse_cvs_to_json(f.iter_lines(), skip_lines)

def parse_csv_url(source_address, skip_lines):
    return parse_url('csv', source_address, skip_lines)

def parse_csv_file(source_file, skip_lines):
    return parse_file('csv', source_file, skip_lines)

if __name__ == "__main__":
    #url_address = 'http://data.gov.tw/iisi/logaccess?dataUrl=http%3A%2F%2Fwww.thb.gov.tw%2FTM%2FFiles%2FWebpage%2F201404%2F16_%25E5%2585%25A8%25E5%259C%258B%25E5%25A4%25A7%25E5%25AE%25A2%25E8%25BB%258A%25E7%25A6%2581%25E8%25A1%258C%25E8%25B7%25AF%25E6%25AE%25B5-utf.csv&type=CSV&nid=6794'
    #parse_csv_url(url_address, 'url2.json', 'utf8')
    print parse_csv_url('http://data.gov.tw/iisi/logaccess?dataUrl=http%3A%2F%2Fitaiwan.gov.tw%2Ffunc%2Fhotspotlist.csv&type=CSV&nid=5962', '0 1')
    #parse_csv_file('data/workers_disease.csv', '')
    print 'work!'
    

''' Sample file from OpenData.gov
#open big5 csv
#http://data.gov.tw/node/5962
csvfilename = 'hotspotlist.csv'
parse_csv_file('hotspotlist.csv', 'test2.json', 'big5')
parse_csv_url('http://data.gov.tw/iisi/logaccess?dataUrl=http%3A%2F%2Fitaiwan.gov.tw%2Ffunc%2Fhotspotlist.csv&type=CSV&nid=5962', 'url.json', 'big5')

#open utf8 csv
#http://data.gov.tw/node/6794
print 'car-utf.csv'
csvfilename = 'car-utf.csv'
parse_csv_file(csvfilename, 'test2.json', 'utf8')
url_address = 'http://data.gov.tw/iisi/logaccess?dataUrl=http%3A%2F%2Fwww.thb.gov.tw%2FTM%2FFiles%2FWebpage%2F201404%2F16_%25E5%2585%25A8%25E5%259C%258B%25E5%25A4%25A7%25E5%25AE%25A2%25E8%25BB%258A%25E7%25A6%2581%25E8%25A1%258C%25E8%25B7%25AF%25E6%25AE%25B5-utf.csv&type=CSV&nid=6794'
parse_csv_url(url_address, 'url2.json', 'utf8')
'''
