# IDM - Iris Duty Manager

## Содержание
1. [Вступление](https://github.com/dutydev/IDM#Вступление)
2. [Как установить](https://github.com/dutydev/IDM#Как-установить)
3. [Как обновить](https://github.com/dutydev/IDM#Как-обновить)
4. [Сигналы](https://github.com/dutydev/IDM#Сигналы)

## Вступление

Этот проект есть ни что иное как Дежурный для [Iris | Чат-менеджер](https://vk.com/iris_cm).

С помощью Iris Callback API вы можете получать сигналы из бесед, на которые вы подписались. Это поможет вам обрабатывать информацию способом, который удобен для вас без каких-либо ограничений.

Для этого необходимо создать свой сервер, который будет принимать запросы от серверов Iris.

## Как установить
Для установки мы будем использовать сайт [pythonanywhere.com](https://www.pythonanywhere.com/)

И так переходим по ссылке [pythonanywhere.com](https://www.pythonanywhere.com/registration/register/beginner/) заомлняем форму и нажимаем *Register*

Даллее кликаем на кнопку *Web*
Кликаем на *Add a new web app*
В появившемся окошке *next*  -> *Flask* -> *Python3.7*
В путь вводим /home/`имя аккаунта`/IDM/routes.py

Переходим по ссылке [pythonanywhere.com/consoles/](https://www.pythonanywhere.com/consoles/)
Ищем блок *Start a new console*, в нем выбираем *Bash*

После загрузки консоли набираем в консоли
```bash
rm -r IDM
git clone https://github.com/dutydev/IDM.git
```
Далее переходим во вкладку *Web* и нажимаем *Reload * `имя аккаунта`.pythonanywhere.com


Переходим по ссылке `имя аккаунта`.pythonanywhere.com/install вводим данные, нажимаем сохранить.

Заходим на тот аккаунт с который будет дежурным и переходим по ссылке [https://vk.me/-174105461](https://vk.me/-174105461)

Пишем команду
```
+api [ваш секретный код дежурного] https://[ваше имя аккаунта].pythonanywhere.com/callback
```
в ответ получаем 

[![](https://sun9-66.userapi.com/c200716/v200716076/5e9fa/Zn7Gk5YpZbk.jpg)](https://sun9-66.userapi.com/c200716/v200716076/5e9fa/Zn7Gk5YpZbk.jpg)

Осталось в нужном чате написать `+api` и все дежурный готов и работает.

### Как создать приложение ВК
Далее переходим по ссылке [https://vk.com/editapp?act=create](https://vk.com/editapp?act=create "https://vk.com/editapp?act=create"), в поле платформа выбираем *сайт*

Адрес сайта и базовый домен `https://{имя вашего аккаунта}.pythonanywhere.com`

[![](https://sun9-35.userapi.com/c854028/v854028210/1f14ef/nivEJzpzMZ4.jpg)](https://sun9-35.userapi.com/c854028/v854028210/1f14ef/nivEJzpzMZ4.jpg)`

Кликаем на *подключить сайт*.

## Как обновить

Открываем консоль, набираем:

```bash
cp IDM/database.json database.json
rm -rf IDM
git clone https://github.com/dutydev/IDM.git
cp database.json IDM/database.json
```

Перезапускаем приложение в вкладке *Web*

## Сигналы
### Доступные в любом чате с Iris

|Команда|Описание|
|---|---|
|!с пинг / пиу / кинг |Отправляется смс с временем задержки|
|!с инфо / инфа / -i / info |Отправляется смс с информацией о дежурном и чате|
|!с -смс / dsm |Удаляет все сообщения за последнии 24 часа в чате|
|!с +др / +друг [+ответ на сообщение] |Отправляется запрос на добавление в друзья|
|!с -др / -друг [+ответ на сообщение] |Отправляется запрос на удаление из друзей|
|!с +адвд / +друзья |Включает автодобавление в друзья|
|!с -адвд / -друзья |Отключает автодобавление в друзья|
|!с адвд / друзья |Проверяет, включено ли автодобавление в друзья|
|!с +онлайн |Включает вечный онлайн |
|!с -онлайн |Отключает вечный онлайн |
|!с онлайн |Проверяет, включен ли вечный онлайн |
|!с +шаб имя шаблона[новая строка]Данные | Добавляет новый шаблон |
|!с -шаб имя шаблона | Удаляет шаблон |
|!с шабы | Выводит список шаблонов |
|!с шаб имя шаблона | Редактирует смс на шаблон |
|!с +дов [+ответ на сообщение] | Добавляет пользователя в список доверенных |
|!с -дов [+ответ на сообщение] | Исключает пользователя из списока доверенных |
|!с довы | Выводит список доверенных пользоваетелей |

### Доступные когда вы дежурный в чате
|Команда|Описание|
|---|---|
|!д пинг / пиу / кинг | Отправляется смс с временем задержки|
|!д инфо / инфа / -i / info |Отправляется смс с информацией о дежурном и чате|
|!д повтори[новая строка]Текст| Дежурный повторит текст (только для доверенных пользователей) |

Так же обрабатываются все стандартные сигналы, кроме `hereApi` и `ignoreMessages`. О стандартных сигналах Вы можете узнать в [статье](https://vk.com/@iris_cm-api2).


## Благодарности

Спасибо за помощь в тестировании:

[Ридэль Яумбаев](https://vk.com/ss_20)

[Влад Богданов](https://vk.com/gamtz)

[Владислав Джениа](https://vk.com/klubnishhhka)

[Димитрий Ким](https://vk.com/iris_wolf)


