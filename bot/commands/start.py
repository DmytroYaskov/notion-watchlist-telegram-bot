from ..lib.BotController import TelegramBotController

# Chech user on start
# + Deep link key
# - - Read key from message
# - - Check if available in key chain
# - - + available
# - - - - Remove Key
# - - - - Add to users list as allowed user
# - - + not available
# - - - - Add this user to users list as not allowed
# - - - - Warn a user about ignored messages
# + No key
# - - check if user is in users list
# - - + is in list
# - - - - Notify that user has used this bot before
# - - + is`t in list
# - - - - Add this user to users list as not allowed
# - - - - Notify that user`s messages will be ignored
# - - - - Generate invite code to be passed by another user to grant access

class cmd():

    description = "start function"

    deep_description = """
    """

    def execute(parrent_obj: TelegramBotController, arguments=""):
        print("start function executed")

        