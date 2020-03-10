"""
      ===== KOSTGEN BOT CONFIG =====
      Copyright (C) 2020 IU7OG Team.

      Настройки и константы для бота.
"""


import os

KOST_TOKEN = os.environ['KOST_TOKEN']
PROXY_USER = os.environ['PROXY_USER']
PROXY_PASS = os.environ['PROXY_PASSWORD']
PROXY_IP = os.environ['PROXY_IP']

PROXY = 'socks5://' + PROXY_USER + ':' + PROXY_PASS + '@' + PROXY_IP + ':1080'


HATE_MESSAGES = [
    "Ваши права будут урезаны, Вам запрещено заливать что-либо до следующей пятницы.",
    "Жалко, что студенты - не интернет, экзамен принимать стало бы намного проще.",
    "Аватарочку смените, а то меня мама спрашивает, что за друзья у меня такие."
]

HELP_MESSAGE = '"Сашок-полтишок, мне тут лень тесты писать, чё там, норм, посмтришь?"'

START_MESSAGE = \
    "🙌🏻 "
