from telegram import Update,InputFile
from telegram.ext import CallbackContext
from .models import Users

def start(update: Update,CallbackContext):
    
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    chat_id = update.message.chat.id
    
    if not chat_id in  Users.objects.all().values_list("chat_id",flat=True):
    
        Users.objects.create(first_name=first_name,last_name=last_name,username=username,chat_id=chat_id)
        update.message.reply_html("<b>ID raqamingizni kiriting.\nRasmdagi namuda ko'rsatilgan raqamni yuboring</b>")
        update.message.reply_photo(photo=InputFile("F:\python_homework\django-home\dtm_bot\DTM_bot\bot\photo_2023-07-16_13-00-16.jpg"))
    else:
        
        update.message.reply_html("<b>Welcome back</b>]nID raqamingizni yuboring")
        update.message.reply_photo(photo=InputFile("F:\python_homework\django-home\dtm_bot\DTM_bot\bot\photo_2023-07-16_13-00-16.jpg"))
