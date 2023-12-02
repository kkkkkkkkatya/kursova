
class KeeperService():
    keeper: dict = {}

    def push(self, key, value):
        self.keeper[key] = value
        print(f"keeper: {self.keeper}")


    def get(self, key) -> str :
        value = self.keeper.get(key)
        return value

    def pop(self, key) -> str :
        value = self.keeper.get(key)
        self.keeper[key] = ""
        return value


keeper_service = KeeperService()