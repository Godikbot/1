# TODO: о господи что за дерьмо
from idm.objects import dp, MySignalEvent, DB
from idm.api_utils import get_last_th_msgs
from datetime import datetime, date, timezone, timedelta
import time, re, requests, os, io, json
from microvk import VkApi

@dp.longpoll_event_register('кмдбеседа')
@dp.my_signal_event_register# TODO: о господи что за дерьмо
from idm.objects import dp, MySignalEvent, DB
from idm.api_utils import get_last_th_msgs
from datetime import datetime, date, timezone, timedelta
import time, re, requests, os, io, json
from microvk import VkApi

@dp.longpoll_event_register('кмдбеседа')
@dp.my_signal_event_register('кмдбеседа')
def little_theft(event: MySignalEvent) -> str:
    event.msg_op(2, """все команды начинаются с ".с"
.с реши
.с боты
.с люди
.с имя
.с ад
.с учас
.с беседа""")
    return "ok"

@dp.longpoll_event_register('кмдпростой')
@dp.my_signal_event_register('кмдпростой')
def little_theft(event: MySignalEvent) -> str:
    event.msg_op(2, """
все команды начинаются с ".с"
кража ав
пуши
алло
ксмс
Рестарт
тест
взлом жопы
опрос
спам
время
прочитать все
свалить
связать
повтори
статус
бот
кто
ж
мессага
+аватарка
-аватарка
добавить
кик""")
    return "ok"

@dp.longpoll_event_register('кмдбета')
@dp.my_signal_event_register('кмдбета')
def little_theft(event: MySignalEvent) -> str:
    event.msg_op(2, """
все команды начинаются с ".с"
проф
кража ав
пуши
алло
ксмс
Рестарт
тест
взлом жопы
время
дата
опрос
спам
прочитать все
свалить
связать
повтори
бот
статус
кто
ж
пустой
айди
дру
+аватарка
-аватарка
добавить
кик""")
    return "ok"
