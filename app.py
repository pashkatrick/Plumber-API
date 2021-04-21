from __future__ import print_function
import zerorpc
from core import ServerController, DBController
from decouple import config
import subprocess
import os
import argparse
import json

from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return Api().test()

@app.route('/list', methods=['POST'])
def method_list():
    return Api().method_list_handler(
        host=request.json['host']
    )

@app.route('/template', methods=['POST'])
def get_template():
    return Api().get_message_template_handler(
        host=request.json['host'],
        method=request.json['method']
    )

@app.route('/send', methods=['POST'])
def send_request():
    return Api().send_request_handler(
        host=request.json['host'],
        method=request.json['method'],
        req=json.dumps(request.json['body'])
    )


class Api(object):

    def test(self):
        return 'Welocome to gRPC world!'

    def method_list_handler(self, host):
        rs = ServerController.RemoteServer(host=host)
        return rs.get_method_list()

    def get_message_template_handler(self, host, method):
        rs = ServerController.RemoteServer(host=host)
        return rs.get_message_template(method=method)

    def send_request_handler(self, host, method, req):
        rs = ServerController.RemoteServer(host=host)
        return rs.send_request(request=req, method=method)

    def view_method_scheme_handler(self, host, method):
        rs = ServerController.RemoteServer(host=host)
        return rs.view_method_scheme(method=method)

    def get_collections_handler(self):
        return db.get_collections()

    def update_collection_handler(self, __object):
        return db.update_collection(__object)

    def add_collection_handler(self, name):
        return db.add_collection(name=name).Id

    def remove_collection_handler(self, id):
        return db.remove_collection(collection_id=id)

    def get_item_handler(self, id):
        return db.get_item(item_id=id)

    def add_item_handler(self, __object):
        return db.add_item(__object).Id

    def update_item_handler(self, __object):
        return db.update_item(__object)

    def remove_item_handler(self, id):
        return db.remove_item(item_id=id)

    def get_items_by_collection_handler(self, id):
        return db.get_items_by_collection(collection_id=id)

    def export_handler(self):
        return db.export_collections()

    def import_handler(self, collections):
        return db.import_collections(content_to_import=collections)
 

def __get_http_port():
    return config('HTTP_PORT')

def __get_port():
    return config('RPC_PORT')

def __get_host():
    return config('RPC_HOST')

def __get_db():
    return config('DB')   

db = DBController.DBController(db=str(__get_db())) 

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--http', action='store_true')
    args = parser.parse_args()

    if args.http:
        app.run(port=__get_http_port(), host=__get_host())

    else:
        addr = 'tcp://' + str(__get_host()) + ':' + str(__get_port())
        s = zerorpc.Server(Api())
        s.bind(addr)
        print('start running on {}'.format(addr))
        s.run()


if __name__ == '__main__':
    main()
