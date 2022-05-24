class Chat:
    def __init__(self) -> None:
        self.commands = []
        self.filters = []

    def add_command(self, command, func):
        self.commands.append({"command": command, "func": func})

    def add_filter(self, filter, func):
        self.filters.append({"filter": filter, "func": func})

    def handler(self, updates):
        for update in updates["result"]:
            print(update)
            if update.get("message"):
                text = None

                if update["message"].get("text"):
                    text = update["message"]["text"]

                    for command in self.commands:
                        if text == command["command"]:
                            command["func"](update)

                if update["message"].get("photo"):
                    for filter in self.filters:
                        if "photo" == filter["filter"]:
                            filter["func"](update)
