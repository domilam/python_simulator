# coding=utf-8

import uuid

class User:
    def __init__(self, name):
        self.id = uuid.uuid4().hex
        self.name = name
        self.inbox = []

    def add_toinbox(self, message):
        self.inbox.append(message)