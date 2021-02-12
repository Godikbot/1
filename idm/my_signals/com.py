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
    
    
