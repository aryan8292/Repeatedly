from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace '6874468807:AAF9MEISINpd_vHM-G9lhFum5IK4DJTAz6I' with your actual bot token
TOKEN = '6874468807:AAF9MEISINpd_vHM-G9lhFum5IK4DJTAz6I'
CHAT_ID = '-1004059055124'  # Replace with your chat ID

def send_repeated_message(context: CallbackContext) -> None:
    try:
        context.bot.send_message(chat_id=CHAT_ID, text="Your repeated message here.")
    except Exception as e:
        error_handler(context, e)

def start_repeated(update: Update, context: CallbackContext) -> None:
    # Schedule the message to be sent every minute
    schedule.every(1).minutes.do(send_repeated_message, context=context)

def error_handler(context: CallbackContext, error: Exception) -> None:
    """Log errors."""
    context.error(f"Error: {error}")

def main() -> None:
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # Register the error handler
    dispatcher.add_error_handler(error_handler)

    # Register the command
    dispatcher.add_handler(CommandHandler("start_repeated", start_repeated))

    updater.start_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)

    updater.idle()

if __name__ == '__main__':
    main()
