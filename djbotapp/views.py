from django.shortcuts import render
from django.http import HttpResponse
import json
import telebot
import requests
import unittest
import unittest.mock
# Create your views here.

tb = telebot.TeleBot('Token')


tb.set_webhook(url="test", certificate=open('mycert.pem') )

def index(request):
    return HttpResponse("Hello it's a test stuff")

def add_movie(request):
    if
        movie =

##def set_webhook()
    url =
    certificate = /path/to/certificate

def tg_responce
