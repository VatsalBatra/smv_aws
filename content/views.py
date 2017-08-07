from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
import requests
import time
import re
from bs4 import BeautifulSoup
from django.core.urlresolvers import resolve
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import json
from django.shortcuts import render
from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.template import Context, Template
from django.template import RequestContext
from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse
from django.conf import settings

from django.template import RequestContext
from django.template.loader import render_to_string

from .models import image_slide,our_ride,partners,crew_members,crew_sir,achievement,contact_info,about,forum_form,solution

def first_page(request):

	context = {'slide':image_slide.objects.all(),'ride':our_ride.objects.all(),'partners':partners.objects.all(),'crew_members':crew_members.objects.all(),'sir': crew_sir.objects.all(),'achievement':achievement.objects.all(),'contact':contact_info.objects.all(),'about':about.objects.all()}
	return render(request,'content/base.html',context);

def forum(request):
	context = {
		
	}
	return render(request,'content/forum.html',context)

def add(request):
	print("ouououououoououououououou")
	email = request.GET.get('name','')
	question = request.GET.get('text','')
	print(email)
	#why not working??
	# if not question:
	# 	render(request,'content/forum.html',{'message':'please enter the query'})
	print(question)
	question_object = forum_form(email = email,question =question)
	question_object.save()

	return HttpResponse("ok")
def content(request):
	heading =[]
	question = []
	quest_list = forum_form.objects.all().order_by("-id");
	for q in quest_list:
		heading.append(q.email)
		question.append(q.question)
	context = {
		'heading':heading,
		'question':question
		}

	print("yoooyyoooyyoyoyooyoyoyoyo")
	return JsonResponse(context,safe = False)
def add_ans(request):
	# question = get_object_or_404(question = question)
	# ques_id  = question.id
	# print(ques_id)
	return HttpResponse("ok")
def upload(request):
	return HttpResponse("ok")
# Create your views here.
