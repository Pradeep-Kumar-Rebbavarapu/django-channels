import random
import threading
from .models import *
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

fake = Faker()


class CreateStudentsThread(threading.Thread):
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            print('Thread execution started')
            for i in range(self.total):
                print(i)
                Students.objects.create(
                    student_name=fake.name(),
                    student_email=fake.email(),
                    address=fake.address(),
                    age=random.randint(10, 50)
                )

        except Exception as e:
            print(e)
