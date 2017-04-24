from pprint import pprint
from echobot import bot


response = bot.getUpdates()
pprint(response)
[{'message': {'chat': {'first_name': 'Nick',
                       'id': 45543,
                       'type': 'private'},
                }}]