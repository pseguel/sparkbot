from __future__ import print_function
from builtins import object

import json
import web
import requests

from ciscosparkapi import CiscoSparkAPI, Webhook

# Global variables
urls = ('/sparkwebhook', 'webhook', '/', 'index')
app = web.application(urls, globals())
api = CiscoSparkAPI()

class index:
    def GET(self):
        return "Hello, world!"

class webhook(object):

        def POST(self):
            #atiende al POST de Spark
            json_data = web.data()

            webhook_obj = Webhook(json_data)
            room = api.rooms.get(webhook_obj.data.roomId)
            message = api.messages.get(webhook_obj.data.id)
            person = api.people.get(message.personId)

            # para no responderme a mi mismo
            me = api.people.me()
            if message.personId == me.id:
                return 'OK'
            else:
                if 'hola' in message.text:
                    answer = 'hola amigo'
                    response_message = api.messages.create(room.id,
                                                           text=answer)
            return 'OK'

if __name__ == '__main__':
    app.run()
