#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
import hipchat


urls = ('/.*','hooks')
app = web.application(urls, globals())

# hipchat data
HIP_CHAT_TOKEN = ''
ROOM_ID  =  1

class hooks:
    def __init__(self):
        self.hipster = hipchat.HipChat(token = HIP_CHAT_TOKEN)

    def POST(self):
        data = json.loads(web.data())
        try:
            # github v3 json
            message = data['comment']['_links']['pull_request']['href']
            self.send(message)

        except:
            try:
                message = data['comment']['html_url']
                self.send(message)
            except:
                pass

        return 'OK'

    def send(self, message):
        self.hipster.method('rooms/message',  method = 'POST',  parameters = {'room_id': ROOM_ID, 'from': 'github',  'message': 'Pull Request diff commented on.' + message})

if __name__ == '__main__':
    app.run()
