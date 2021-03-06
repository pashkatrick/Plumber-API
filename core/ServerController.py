import json
import subprocess


class RemoteServer:

    def __init__(self, host, metadata):
        self.host = host
        self.cmd = './grpcurl'
        self.meta = metadata

    def __send_shell(self, command):
        if self.meta:
            json_meta = json.loads(self.meta)
            rpc_headers = ''
            for header in json_meta:
                rpc_headers += f'-rpc-header {header}:{json_meta[header]} '
            return subprocess.check_output(f'{self.cmd} {rpc_headers}{command}', shell=True)
        else:
            return subprocess.check_output(f'{self.cmd} {command}', shell=True)

    def __get_service_list(self):
        output = self.__send_shell(f'-plaintext {self.host} list')
        service_list = [service for service in output.decode('utf-8').split('\n') if service]
        return dict(services=service_list)

    def __get_message_schema(self, method):
        output = self.__send_shell(f'-plaintext {self.host} describe {method}')
        out = output.decode('utf-8').replace('\n', '',).replace(' ', '').replace(';', '')
        res = out.split('returns')[1].replace('(', '').replace(')', '')
        req = out.split('returns')[0].split('(')[1].replace(')', '')
        schema = dict(request=req, response=res)
        return schema

    def get_method_list(self):
        services = self.__get_service_list()['services']
        result = []
        for service in services:
            output = self.__send_shell(f'-plaintext {self.host} list {service}')
            method_list = [method for method in output.decode('utf-8').split('\n') if method]
            result.append(dict(service=service, methods=method_list))
        return dict(methods=result)

    def get_message_template(self, method):
        request = self.__get_message_schema(method)['request']
        output = self.__send_shell(f'-plaintext -msg-template {self.host} describe {request}')
        message_template = json.loads(output.decode('utf8').split('Message template:')[1].replace('\n', '').replace(' ', ''))
        return message_template

    def send_request(self, request, method):
        output = self.__send_shell(f'-plaintext -d \'{request}\' {self.host} {method}')
        return json.loads(output.decode('utf-8'))

    def view_method_scheme(self, method):
        data = self.__get_message_schema(method)
        output_request = self.__send_shell(f'-plaintext -msg-template {self.host} describe {data["request"]}')
        output_response = self.__send_shell(f'-plaintext -msg-template {self.host} describe {data["response"]}')
        scheme = output_request.decode('utf8') + '\n' + output_response.decode('utf8')
        return scheme