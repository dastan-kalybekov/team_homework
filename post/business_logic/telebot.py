import requests


def telegram_bot_send_text(bot_message, bot_chat_ID):
    bot_token = '6107937292:AAF6sGWwygfT-YunuLvalkRhtJ-w9_RVmb4'
    send_text = ('https://api.telegram.org/bot' + bot_token +
                 '/sendMessage?chat_id=' + bot_chat_ID +
                 '&parse_mode=Markdown&text=' + bot_message)
    response = requests.get(send_text)
    return response.json()
