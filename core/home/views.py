from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
import time
from faker import Faker
from .models import *
# Create your views here.
from .thread import *

fake = Faker()
import random
def home(request):
    # for i in range(1,10):
    #     channel_layer = get_channel_layer()
    #     data = {'count':i}
    #     await (channel_layer.group_send)(
    #         "new_consumer_group", {
    #             'type': 'send_notification',
    #             'value': json.dumps(data)
    #         }
    #     )
    #     time.sleep(0.5)
    
    CreateStudentsThread(100).start()
    params = {'data':'your task started'}
    return render(request,'home.html',params)
