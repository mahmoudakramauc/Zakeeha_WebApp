# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_restful import Resource, Api, abort
from string import Template
import requests 
from flask import request
app = Flask(__name__)


scholars_details = {'Alhabib ALi Aljifri' : {'imagethumb':'/static/images/thumbs/alhabeebalialjafri.jpg',
                                 'imagefull': '/static/images/fulls/alhabeebalialjafri.jpg',
                                 'bio' : 'Chairman of Tabah Foundation Management Board , Abu Dhabi  Member of the Board of Director of Dar Al-Mustafa for Islamic Studies in Tarim http://www.alhabibali.com/en/bio/',   
                                 'dars': 'Alhabib ALi Aljifri'
                                },
                                
                    'amr elwerdany': { 'imagethumb': '/static/images/thumbs/amrelwerdani.jpg',
                                    'imagefull': '/static/images/fulls/amrelwerdani.jpg',
                                    'bio' : 'http://www.alhabibali.com/ar/bio/',
                                    'dars': 'amr elwerdany'
  
                                   },

                    'muhammad mehanna': { 'imagethumb': '/static/images/thumbs/muhammadmehanna.jpg',
                                          'imagefull': '/static/images/fulls/muhammadmehanna.jpg',
                                          'bio' : 'http://www.alhabibali.com/ar/bio/',
                                          'dars': 'muhammad mehanna'
  
                                        }, 

                    'ali gomaa': { 'imagethumb': '/static/images/thumbs/aligomaa.jpg',
                                          'imagefull': '/static/images/fulls/aligomaa.jpg',
                                          'bio' : 'http://www.alhabibali.com/ar/bio/',
                                          'dars': 'ali gomaa'
  
                                        },                             
                   
                    'mo3ez mas3ood' :{ 'imagethumb': '/static/images/thumbs/moezmasoud.jpg',
                                       'imagefull': '/static/images/fulls/moezmasoud.jpg',
                                       'bio' : 'Egyptian scholar, public intellectual and television presenter who focuses on the fields of contemporary spirituality, inter-faith dialogue, and Islam in the modern world.',
                                       'dars': 'mo3ez mas3ood'
                                 
                                     }}
            

# home page
@app.route('/')
def home( ):
    r = requests.get("https://zakkeeha.herokuapp.com/all_deroos")
    scholars_active = {}
    scholars_inactive = {}
    for dars in r.json()["active"]:
      scholars_active[dars['scholar_name']] = scholars_details[dars['scholar_name']]
    #  print(scholars_active)
    for dars in r.json()["inactive"]:
      scholars_inactive[dars['scholar_name']] = scholars_details[dars['scholar_name']]
    #  print(scholars_inactive)
    return render_template('home.html', active_scholars=scholars_active, inactive_scholars=scholars_inactive)

# active topics page
@app.route('/activetitles')
def titles():
    r = requests.get("https://zakkeeha.herokuapp.com/all_deroos")
    titles =[]
    for dars in r.json()["active"]:
      if dars["title"] not in titles:
         titles.append(dars["title"])
   
    return render_template('titles.html', titles=titles)

@app.route('/activetopics')
def topics():
    r = requests.get("https://zakkeeha.herokuapp.com/all_deroos")
    topics =[]
    for dars in r.json()["active"]:
      if dars["topic"] not in topics:
         topics.append(dars["topic"])     
    #print(titles)
    return render_template('topics.html', topics=topics)

@app.route('/scholarsdetails')
def scholarsdetails():
    r = requests.get("https://zakkeeha.herokuapp.com/all_deroos")
    scholar_name = "alhabib"
    deroos_by_scholar_name = []
    for dars in r.json()["active"]:
            if dars["scholar_name"] == scholar_name:
               deroos_by_scholar_name.append(dars)
    print(deroos_by_scholar_name)
    return render_template('scholarsdetails.html', deroos_by_scholar_name=deroos_by_scholar_name)

@app.route('/deroos_by_scholar_name')
def deroos_by_scholar_name():
    r = requests.get("https://zakkeeha.herokuapp.com/all_deroos")
    scholar_name = request.args.get('my_var', None)

    deroos_by_scholar_name = []
    for dars in r.json()["active"]:
            if dars["scholar_name"] == scholar_name:
               deroos_by_scholar_name.append(dars)
    print (deroos_by_scholar_name)
    return render_template('deroos_by_scholar_name.html', deroos_by_scholar_name=deroos_by_scholar_name)

@app.route('/scholarnames')
def scholar_names():
    r = requests.get("https://zakkeeha.herokuapp.com/all_deroos")
    scholar_names = []
    for dars in r.json()["active"]:
      if dars["scholar_name"] not in scholar_names:
         scholar_names.append(dars["scholar_name"])

    return render_template('scholarnames.html', scholar_names=scholar_names)


@app.route('/details')
def details():
    r = requests.get("https://zakkeeha.herokuapp.com/all_deroos")
    titles =[]
    topics =[]
    for dars in r.json()["active"]:
      if dars["title"] not in titles:
         titles.append(dars["title"])
    for dars in r.json()["active"]:
      if dars["topic"] not in topics:
         topics.append(dars["topic"])
    return render_template('sidemenu.html', titles=titles, topics=topics)
   

if __name__ == '__main__':
    app.run(debug=True)
                   
