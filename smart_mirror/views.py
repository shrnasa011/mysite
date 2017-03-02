from django.shortcuts import render

import datetime
import json
from urllib2 import urlopen

def time_converter(time):

    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')

    return converted_time

def url_builder(id):

    user_api = '92753bbe4c688f5bcee15f9ec1faf3e3'  
    unit = 'metric' 
    api = 'http://api.openweathermap.org/data/2.5/forecast/daily?id=1258044'  
    full_api_url = api + str(id) + '&mode=json&units=' + unit + '&APPID=' + user_api

    #full_api_url = 'http://api.openweathermap.org/data/2.5/forecast/daily?id=1258044&lang=zh_cn&appid=92753bbe4c688f5bcee15f9ec1faf3e3'

    return full_api_url


def data_fetch(full_api_url):

    url = urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()

    return raw_api_dict

def data_organizer(raw_api_dict):

    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
#        temp= 
        temp_max=entry[temp_max],
        temp_min=entry[temp_min],

    )

    return data

"""
def data_output(data):

    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
"""
    

def data_fetch_news(url):

    url = urlopen(url)
    output = url.read().decode('utf-8')
    raw_data = json.loads(output)
    url.close()

    return raw_data



def index(request):

    try:
   
#        id=1258044
#        data = data_organizer(data_fetch(url_builder(id)))
     	url_news= 'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=15f23ada1b3d4740b80a2e4c16943993'
    	raw_data=(data_fetch_news(url_news))

	entry0=raw_data["articles"][0]
	data0=dict(
		source_from= raw_data["source"],
		title=entry0["title"],
                author=entry0["author"],
	)

	entry1=raw_data["articles"][1]

	data1=dict(
		source_from= raw_data["source"],
		title=entry1["title"],
                author=entry1["author"],

	)

	entry2=raw_data["articles"][2]

	data2=dict(
		source_from= raw_data["source"],
		title=entry2["title"],
                author=entry2["author"]

	)

	entry3=raw_data["articles"][3]

	data3=dict(
		source_from= raw_data["source"],
		title=entry3["title"],
                author=entry3["author"]

	)

	entry4=raw_data["articles"][4]

	data4=dict(
		source_from= raw_data["source"],
		title=entry4["title"],
                author=entry4["author"]

	)


        return render(request, 'smart_mirror/index.html', {'data0':data0, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4})

    except IOError:

        return render(request, 'smart_mirror/index.html', {'error_message' : "No internet"} )



"""def url_builder(key):

	apiKey=key

	url= 'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey='+apiKey

	return url

	"""



"""
#def data_organizer_news(raw_data):

    #elements_array=raw_data["articles"][1] #getting number of elements under article

    #len(elements_array)
	print('{},\n {}:'.format(data0['author'],data0['title']))

	print('{},\n {}:'.format(data1['author'],data1['title']))

	print('{},\n {}:'.format(data2['author'],data2['title']))

	print('{},\n {}:'.format(data3['author'],data3['title']))

	print('{},\n {}:'.format(data4['author'],data4['title']))

	#data5= [data0,data1,data2,data3,data4] // unable to pass multiple argument

	#return (data5)

   def data_output(data5):

    #print(len(elements_array))

	print('{},\n {}:'.format(data0['author'],data0['title']))

	print('{},\n {}:'.format(data1['author'],data1['title']))

	

	print('{},\n {}:'.format(data2['author'],data2['title']))

	

	print('{},\n {}:'.format(data3['author'],data3['title'])

	print('{},\n {}:'.format(data4['author'],data4['title']))

	#print(len(no_data))

	#print('{}'.format(elements_array))

	"""


