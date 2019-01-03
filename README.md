# Telegram Slap bot
Slap a random user in a telegram channel or group.

## Installation
Clone this repository (`git clone https://github.com/danilopolani/telegram-slap-bot`) and install deps with `pipenv install`. **Note**: It requires *Python 3.7*.

### Variables

Open `main.py` and replace variables at top.  

To generate `api_id` and `api_hash` please refer to [this tutorial](https://telethon.readthedocs.io/en/stable/extra/basic/creating-a-client.html).  
To generate `bot_token`, please create a bot with *@BotFather* on Telegram.  

Finally, `tg_group` is the group *permalink*. You can find it easily on Telegram Web, for example joining a group the URL will be `https://web.telegram.org/#/im?p=@my_group` and the permalink is the slug after `@` at the end, in this case `my_group`.

## Run

Simply run `python3 main.py` from your terminal and there you go. The bot will work only when the command is running, so I suggest you to use some process manager like Supervisor to keep it alive automatically on a server.

### Screenshot of example

![Example](https://i.imgur.com/vz2DEui.png)
