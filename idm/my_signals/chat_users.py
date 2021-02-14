from typing import Tuple, List
from math import ceil
from idm.utils import get_index, format_push
from idm.objects import dp, MySignalEvent

def users_getter(event: MySignalEvent) -> Tuple[MySignalEvent, List[dict], List[dict]]:  # noqa
    all_users = event.api('messages.getConversationMembers',
                          peer_id=event.chat.peer_id)

    def find_member_info(uid: int, group: bool) -> dict:
        for user in all_users['groups'] if group else all_users['profiles']:
            if user['id'] == uid:
                return user

    users = []
    groups = []
    for member in all_users['items']:
        if member['member_id'] > 0:
            info = find_member_info(member['member_id'], False)
            info.update(member)
            users.append(info)
        else:
            info = find_member_info(abs(member['member_id']), True)
            info.update(member)
            groups.append(info)
    return event, users, groups

@dp.longpoll_event_register('люди')
@dp.my_signal_event_register('люди')
@dp.wrap_handler(users_getter)
def list_users(event: MySignalEvent, users: List[dict], _):
    try:
        page = int(get_index(event.args, 0, 1)) - 1
        if page < 0:
            raise ValueError
    except ValueError:
        page = 0
    count = len(users)
    pages = ceil(count/20)
    msg = ''
    for i, user in enumerate(users[page*20:page*20+20], 1 + page*20):
        msg += f"\n{i}. [id{user['id']}|{user['first_name']} {user['last_name']}]"  # noqa
    if msg == '':
        msg = f'\nСтраница {page + 1} пуста'
    else:
        msg = f'\nУчастники беседы (страница {page + 1} из {pages}):' + msg
    event.msg_op(1, msg, disable_mentions=1, reply_to=event.msg['id'])
    return "ok"

@dp.longpoll_event_register('беседа', 'чат')
@dp.my_signal_event_register('беседа', 'чат')
@dp.wrap_handler(users_getter)
def chat_info(event: MySignalEvent, users: List[dict], groups: List[dict]):
    admins = []
    owner = None
    for member in users + groups:
        if member.get('is_owner') is True:
            owner = member
        elif member.get('is_admin') is True:
            admins.append('\n-- ' + format_push(member))
    msg = f"""
    Беседа: {event.chat.name}
    Создатель: {format_push(owner)}
    Iris ID: {event.chat.iris_id}
    Я дежурный в чате: {'✅' if event.chat.installed else '❌'}
    Население чата: {len(users) + len(groups)}
    Участников: {len(users)}
    Ботов: {len(groups)}

    Администраторы:{''.join(admins) if admins else 'Админы невидимые 🌚👍'}
    """.replace('    ', '')
    event.msg_op(1, msg, disable_mentions=1, reply_to=event.msg['id'])
    return "ok"

@dp.longpoll_event_register('боты')
@dp.my_signal_event_register('боты')
@dp.wrap_handler(users_getter)
def list_groups(event: MySignalEvent, _, groups: List[dict]):
    try:
        page = int(get_index(event.args, 0, 1)) - 1
        if page < 0:
            raise ValueError
    except ValueError:
        page = 0
    count = len(groups)
    pages = ceil(count/20)
    msg = ''
    for i, group in enumerate(groups[page*20:page*20+20], 1 + page*20):
        msg += f"\n{i}. [public{group['id']}|{group['name']}]"
    if msg == '':
        msg = f'Страница {page + 1} пуста'
    else:
        msg = f'Группы беседы (страница {page + 1} из {pages}):' + msg
    event.msg_op(2, msg)
    return "ok"

@dp.longpoll_event_register('учас', 'участники')
@dp.my_signal_event_register('учас', 'участники')
@dp.wrap_handler(users_getter)
def chat_info(event: MySignalEvent, users: List[dict], groups: List[dict]):
    admins = []
    owner = None
    for member in users + groups:
        if member.get('is_owner') is True:
            owner = member
        elif member.get('is_admin') is True:
            admins.append('\n-- ' + format_push(member))
    msg = f"""
    Число людей 🇷🇺: {len(users)} 👤
    Население чата: {len(users) + len(groups)} 👪
    Ботов: {len(groups)} (♡_♡)
    """.replace('    ', '')
    event.msg_op(1, msg, disable_mentions=1, reply_to=event.msg['id'])
    return "ok"

@dp.longpoll_event_register('ад','Админы')
@dp.my_signal_event_register('ад','админы')
@dp.wrap_handler(users_getter)
def chat_info(event: MySignalEvent, users: List[dict], groups: List[dict]):
    admins = []
    owner = None
    for member in users + groups:
        if member.get('is_owner') is True:
            owner = member
        elif member.get('is_admin') is True:
            admins.append('\n-- ' + format_push(member))
    msg = f"""
    Создатель 🇷🇺: {format_push(owner)} 😎
    Администраторы:\n{' '.join(admins) if admins else 'Админы невидимые 🌚👍'}
    """.replace('    ', '')
    event.msg_op(1, msg, disable_mentions=1, reply_to=event.msg['id'])
    return "ok"

@dp.longpoll_event_register('имя', 'название')
@dp.my_signal_event_register('имя', 'название')
@dp.wrap_handler(users_getter)
def chat_info(event: MySignalEvent, users: List[dict], groups: List[dict]):
    admins = []
    owner = None
    for member in users + groups:
        if member.get('is_owner') is True:
            owner = member
        elif member.get('is_admin') is True:
            admins.append('\n-- ' + format_push(member))
    msg = f"""
    Беседа 🇷🇺: {event.chat.name}
    Создатель: {format_push(owner)} 😎
    """.replace('    ', '')
    event.msg_op(1, msg, disable_mentions=1, reply_to=event.msg['id'])
    return "ok"

@dp.longpoll_event_register('ре','реши')
@dp.my_signal_event_register('ре','реши')
def restart(event: MySignalEvent) -> str:
    event.msg_op(1, f"""{eval(" ".join(event.args))}""")
    return "ok"
