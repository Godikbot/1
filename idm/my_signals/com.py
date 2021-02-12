# TODO: о господи что за дерьмо
from idm.objects import dp, MySignalEvent, DB
from idm.api_utils import get_last_th_msgs
from datetime import datetime, date, timezone, timedelta
import time, re, requests, os, io, json
from microvk import VkApi

@dp.longpoll_event_register('п')
@dp.my_signal_event_register('п')
def little_theft(event: MySignalEvent) -> str:
    if event.args[0] != 'беседа': return "ok"
    event.msg_op(2, """все команды начинаются с ".с"
    .с реши
    .с боты
    .с люди
    .с имя
    .с ад
    .с учас
    .с беседа""")
    return "ok"
    
@dp.longpoll_event_register('п')
@dp.my_signal_event_register('п')
def little_theft(event: MySignalEvent) -> str:
    if event.args[0] != 'простойдеж': return "ok"
    event.msg_op(2, """
    .с кража ав 
    .с пуши
    .с алло
    .с ксмс
    .с Рестарт
    .с тест
    .с взлом жопы
    .с опрос
    .с спам
    .с прочитать все
    .с свалить
    .с связать
    .с повтори
    .с статус
    .с бот
    .с кто
    .с ж
    .с люди 
    .с беседа
    .с боты
    .с мессага""")
    return "ok"
