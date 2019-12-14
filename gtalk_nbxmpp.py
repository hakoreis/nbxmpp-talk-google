'''This Script Is A XMPP TEST.'''

__author__ = "Hakan Vergil <hakanvergil@gmail.com>"
__copyright__ = "Copyright (c) 2018 Python"
__license__ = "Apache License, Version 2.0"

import logging

import nbxmpp
from nbxmpp.protocol import JID
from nbxmpp.client_nb import NonBlockingClient
from nbxmpp.auth_nb import NonBlockingNonSASL

logging.basicConfig(level = logging.INFO)
xmpp_trace  = False

def log(self):
    try:
        print('%s says %s' % (self.from_jid, self.message))
        
    except(Exception):
        print('{} says {}'.format(self.from_jid, self.message))
    
class Connection:
    def __init__(self):
        self.jid = input('Username:')
        self.password = input('Password:')
        self.from_jid = input('receive Username:')
        self.handle_from_jid = JID(self.from_jid).getNode()
        self.message = JID(self.from_jid).getBody()
        self.server = 'xmpp.hangouts.google.com'
        self.port = 5222
        self.starttls = True
        self.client_jid = nbxmpp.protocol.JID(self.jid)
        self.sm = nbxmpp.Smacks(self) # Stream Management
        self.client_cert = None
        self.client_trace = False

    def on_auth(self, con, auth):
        if not auth:
            print('could not authenticate!')
            sys.exit()
            
        print('authenticated using ' + auth)
        self.send_message(self.handle_from_jid, text)

    def on_connected(self, con, con_type):
        print('connected with ' + con_type)
        auth = self.client.auth(self.jid.getNode(), self.password, resource=self.jid.getResource(), sasl=1, on_auth=self.on_auth)

    def get_password(self, cb, mech):
        cb(self.password)

    def on_connection_failed(self):
        print('could not connect!')

    def _event_dispatcher(self, realm, event, data):
        pass

    def connect(self):
        self.client = nbxmpp.NonBlockingClient(self.client_jid.getDomain(), self.password, caller=self)
        self.test = self.client.connect(self, con.on_connected, self.on_connection_failed, self.server, self.port,
        None, None, '1.1.1.1',
        ('tls', None, None, None, None, False))
        
        if(self.test is True):
            return(self.client, print('connected to server'))
        
        else:
            return(self.client, print('not connected to server'))

    def send_message(self):
        id_ = self.client.send(nbxmpp.protocol.Message(self.to_jid, self.message, typ='chat'))
        if(id_ is True):
            return(log())
            
        else:
            return(print('message is not sended'))

    def quit(self):
        self.disconnect()
        return('exited')

    def disconnect(self):
        return(exit(), print('disconnected'))
        
    def handler(self):
        if(self.client_trace):
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            logger = logging.getLogger(NonBlockingClient)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            logger.propagate = False
            return(handler, logger, log())
        
        else:
            print('none log')
    
    def run(self):
        try:
            con.connect()
            send_message()
            return(handler())
            
        except(KeyboardInterrupt):
            quit()
            disconnect()
            return(log())


if(__name__ == '__main__'):
    con = Connection()
    con.run()

