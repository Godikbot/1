from idm.objects import dp, MySignalEvent
from time import sleep

farm_data = {
    "owner_id": -174105461,
    "post_id": 6713149
}


@dp.longpoll_event_register('ферма','ирис')
@dp.my_signal_event_register('ферма','ирис')
def farming(event: MySignalEvent) -> str:
    comment_id = event.api('wall.createComment', message='ферма', **farm_data)['comment_id']
    event.msg_op(2, 'Ирис кони мне коины...')
    sleep(2)
    reply_text = event.api('wall.getComments', **farm_data,
                           comment_id=comment_id)['items'][0]['text']
    event.msg_op(2, reply_text)
    return "ok"
