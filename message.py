# coding=utf-8

import uuid
from datetime import datetime
class Message:
    def __init__(self, message, recipients):
        self.messageId = uuid.uuid4().hex
        self.message = message
        self.recipients = recipients
        self.date = datetime.now()
        self.received = []
        self.opened = []
        print('message créé...')
        print('{0} destinataires'.format(len(self.recipients)))

    def add_received_message(self, recipient):
        self.received.append(recipient)

    def add_opened_message(self, recipient):
        self.opened.append(recipient)

    def get_stat_received(self):
        return len(self.received)

    def get_stat_opened(self):
        return len(self.opened)