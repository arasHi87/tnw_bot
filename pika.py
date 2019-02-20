from fbchat import Client, log
from fbchat.models import *
from bs4 import BeautifulSoup
import codecs, json, requests

setOpen=codecs.open("set.json", "r+", "utf-8")
za=json.load(setOpen)

def save():
    with open('set.json', 'w') as fp:
        json.dump(za, fp, sort_keys=True, indent=4)

class arasHi(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        if author_id != self.uid:
            cmd = message_object.text
            if cmd == 'register':
                if thread_type == ThreadType.GROUP:
                    if thread_id in za['group']:
                        message_object.text = 'Already registered'
                    else:
                        za['group'].append(thread_id)
                        save()
                        message_object.text = 'Register successfully'
                else:
                    message_object.text = 'Now only can register group!'
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)
            elif cmd == 'unregister':
                if thread_type == ThreadType.GROUP:
                    za['group'].remove(thread_id)
                    message_object.text = 'Remove successfully!'
                    save()
                    self.send(message_object, thread_id=thread_id, thread_type=thread_type)
                else:
                    message_object.text = "You didn't register before!"
            elif cmd == 'glist':
                groups = ''
                for group in za['group']:
                    groups = group + '\n'
                if groups == "":
                    groups = 'No group register'
                message_object.text = groups
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)
            elif cmd.startswith('search'):
                data = cmd.replace('search ', '')
                r = requests.post(za['url'] + "post.php?op=search_result", data = {'keyword': data})
                soup = BeautifulSoup(r.text, 'html.parser')
                title = soup.find_all('h1')[0].string
                message_object.text = title + '\n\n'
                bodys = soup.find_all('tbody')
                for body in bodys:
                    rel = body.find_all('th')[0].find_all('a')[0]
                    url = rel.get('href')
                    tit = rel.string
                    message_object.text = message_object.text + tit + '\n' + za['url'] + url +'\n\n'
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)
pika=arasHi(za['act'], za['pw'])
pika.listen()