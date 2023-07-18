from django.shortcuts import render
from django.http import HttpRequest,JsonResponse,HttpResponse
from telegram import Bot,Update
from telegram.ext import Dispatcher, CommandHandler,MessagaHandler,Filter
import json
import os

# Create your views here.

TOKEN = os.environ["TOKEN"]
bot = telegram.Bot(TOKEN)

TOKEN2 = os.environ["TOKEN"]
bot2 = telegram.Bot(TOKEN)


def main(request: HttpRequest):
    
    if request.method=="GET":
        
        return HttpResponse("Webhook working")
    
    elif request.method=="POST":
        data = json.loads(request.body.decode())
        dp = Dispatcher(bot,None,0)
        updater = Update.de_json(data,bot)
        
        dp.add_handler(CommandHandler("start",start)) 
        dp.add_handler(MessagaHandler(Filter.text,search)) 
        
        dp.process_update(updater)
        
        return JsonResponse({"status": 200})
