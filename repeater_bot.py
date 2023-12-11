from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import schedule
import time

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '6874468807:AAF9MEISINpd_vHM-G9lhFum5IK4DJTAz6I'
CHAT_ID = '-4059055124'  # Replace with your group chat ID

def send_repeated_message(context: CallbackContext) -> None:
    context.bot.send_message(chat_id=CHAT_ID, text="Your repeated message here.")

def start_repeated(update: Update, context: CallbackContext) -> None:
    # Schedule the message to be sent every minute
    schedule.every(1).minutes.do(send_repeated_message, context=context)

def main() -> None:
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # Register the command
    dispatcher.add_handler(CommandHandler("start_repeated", start_repeated))

    updater.start_polling()

    # Start the schedule
    schedule.run_continuously()

    updater.idle()

if __name__ == '__main__':
    main()
