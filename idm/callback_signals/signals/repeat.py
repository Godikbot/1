from idm.objects import dp, SignalEvent
import time


@dp.signal_event_register('повтори', 'скажи', 'напиши')
def repeat(event: SignalEvent) -> str:
    if event.msg['from_id'] in event.db.trusted_users:
        message_id = event.send(message)
        time.sleep(3)
        event.api.msg_op(1, msg_id=message_id)
        return "ok"

    msg = event.payload.lower()
    for word in event.responses['repeat_forbidden_words']:
        if word in msg or (msg.startswith('!') and not msg.startswith('!с')):
            event.send(event.responses['repeat_if_forbidden'])
            return "ok"

    message = f'​{" ".join(event.args[0:])}​{event.payload}​'
    if message == '\n':
        event.send('А че написать-то?')
    else:
        event.send(message, attachment=",".join(event.attachments))
    return "ok"
