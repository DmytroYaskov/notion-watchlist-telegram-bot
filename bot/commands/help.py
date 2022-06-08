class cmd():

    description = "list commads, or its entire description by passing it as argument"

    usage = """Usage:
    help [<command-name>]
    """

    def execute(parrent_obj: object, arguments=""):
        if len(arguments) == 0:
            for cmd_name in parrent_obj.commands:
                print( "/" + cmd_name + " - " + parrent_obj.commands[cmd_name].description)
        else:
            if arguments in parrent_obj.commands:
                print(parrent_obj.commands[arguments].usage)
            else:
                print("unknown command")

    
