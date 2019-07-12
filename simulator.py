# coding=utf-8

import uuid
import random
from user import User
from message import Message

class MessageDeliveryEngine:

    def __init__(self, loss_ratio):
        self.loss_ratio = loss_ratio
        self.user_list = []

    def __call__(self):
        print('Création de la liste des users')
        for n in range(1000):
            name = 'username'+str(n)
            user = User(name)
            self.user_list.append(user)

    def publish(self, message):
        for user in message.recipients:
            loss_received = random.random() < self.loss_ratio
            if loss_received:
                user.add_toinbox(message)
                message.add_received_message(user)
            

    def open(self, message):
        for user in message.received:
            loss_opened = random.random() < self.loss_ratio
            if loss_opened:
                message.add_opened_message(user)

if __name__ == "__main__":
    l_ratio = 0.5
    mde = MessageDeliveryEngine(l_ratio)
    mde()

    print('nombre de user {0}'.format(len(mde.user_list)))
    # Création du message
    message_test = Message("Ceci est un test d'envoi d'un message", mde.user_list)

    # envoyer les messages
    mde.publish(message_test)

    # ouvrir les messages reçus
    mde.open(message_test)

    # stat opened messages
    print('Opened messages: {0}'.format(message_test.get_stat_opened()))

    # stat received messages
    print('Received messages: {0}'.format(message_test.get_stat_received()))

