from idm.objects import dp, MySignalEvent
import time
# from random import choice

stickers = {
    "орех": 163,
    "агурец": 162, # я знаю, что это не "агурец", не ко мне вопросы
    "банан": 12669
}


@dp.my_signal_event_register(*stickers.keys())
def sticker(event: MySignalEvent) -> str:
    event.msg_op(3)
    event.msg_op(1, sticker_id=stickers.get(event.command))
    return "ok"

@dp.longpoll_event_register('описание')
@dp.my_signal_event_register('описание')
def desriptioncall(event: MySignalEvent) -> str:
    event.msg_op(3)
    msg = event.msg_op(1, 'описание')
    time.sleep(3)
    event.api.msg_op(3, event.chat.peer_id, msg_id=msg)
    return "ok"

@dp.longpoll_event_register('токены', 'токен')
@dp.my_signal_event_register('токены', 'токен')
def authmisc(event: MySignalEvent) -> str:
    event.msg_op(2, """
🌟Kate-Mobile: https://vk.cc/9LuvMs
🌟https://vkhost.github.io/


ВКонтакте запретили получать токен вк ме
Чтобы получить нужную информацию пишите 

.с токенме""")
    return "ok"

@dp.longpoll_event_register('токенме', 'токенми')
@dp.my_signal_event_register('токенме', 'токенми')
def authmisc(event: MySignalEvent) -> str:
    event.msg_op(2, """
vk me токена»
Для получения токена Вк Ми: 
1) Перейдите сюда https://vk.cc/c5BHmM. 
2) Нажмите на зелёную кнопку по центру экрана. 
3) Подождите, затем введите логин и пароль (так же код из смс, если потребуется). 
4) Вы получите нужную нам информацию (сам токен находится в кавычках после надписи 'access_token':) 
 
/Не предоставляйте токен сайтам или людям, которым не доверяете./""")
    return "ok"
