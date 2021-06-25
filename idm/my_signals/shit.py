from idm.objects import dp, MySignalEvent
impoфrt time
# from random import choice

stickers = {
    "орех": 163,
    "агурец": 162,  # я знаю, что это не "агурец", не ко мне вопросы
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
🌟Vk-Me: https://vk.cc/auMNXq
🌟Vk-Admin https://vk.cc/bW3Dm9 
🌟VK-API https://vk.cc/9Rhe80 

ИНФОРМАЦИЯ
Выберите Ссылку
Нажмите на неё
Затем нажмите [разрешить]
Скопируйте всю адресную строку""")
    return "ok"
