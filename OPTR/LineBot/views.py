from typing import Text
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot import LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError,LineBotApiError
from linebot.models import MessageEvent,TextMessage
# api and secret
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# callback function 
@ csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        # 4 events : 'check event' 'create event' 'edit event' 'delete event' 
        for event in events:
            if isinstance(event,MessageEvent):
                if isinstance(event.message,TextMessage):
                    mtext =event.message.text
                    if mtext =='@check event':
                        test_function(event) 
                    if mtext =='@create event':
                        test_function(event)
                    if mtext =='@edit event':
                        test_function(event)
                    if mtext =='@delete event':
                        test_function(event)
        return HttpResponse()

    else:
        return HttpResponseBadRequest()


#  our function's import  

from linebot.models import TextSendMessage

# test function return comand text 
def test_function(event):
    try:
        message = TextMessage(text = event.message.text.strip('@') + " OK!")
        line_bot_api.reply_message(event.reply_token,message)
    
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='error occurred!') )
