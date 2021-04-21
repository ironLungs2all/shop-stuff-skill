from mycroft import MycroftSkill, intent_file_handler


class ShopStuff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('stuff.shop.intent')
    def handle_stuff_shop(self, message):
        self.speak_dialog('stuff.shop')


def create_skill():
    return ShopStuff()

