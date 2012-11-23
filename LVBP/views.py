'''
Created on Nov 22, 2012

@author: amilano
'''
from django.http import HttpResponse



def home(request):
    
    return HttpResponse("Here we go")

