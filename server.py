from telegram_bot import telegram_bot 
from chatbot import get_answer

Bot = telegram_bot("config.cfg")
update_id = None


while True:
    print("...")
    updates = Bot.get_updates(offset = update_id)
    print(updates)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item['update_id']
            try:
                message = item['message']['text']
                from_ = item['message']['from']['id']
                reply = get_answer(message)
                Bot.send_message(reply, from_)
            except:
                message = None
               