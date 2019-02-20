from fbchat import *
from fbchat.models import *

setOpen=codecs.open("set.json", "r", "utf-8")
za=json.load(setOpen)

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        print (thread_type)
        if author_id == self.uid:
            if message_object.text == 'rg':
                for i in range(0, 50):
                    message_object.text = 'hi - ' + str(i)
                    self.send(message_object, thread_id=thread_id, thread_type=thread_type)

pika=EchoBot('arasi27676271@gmail.com', 'arasHi_910801')
pika.listen()