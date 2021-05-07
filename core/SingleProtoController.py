import json
import subprocess


class SingleProtoController:

    def __init__(self, host, path):
        self.host = host
        self.file = path.split('/')[-1]
        self.folder = path.split(self.file)[0]
        self.cmd = './grpcurl'        
        self.meta = metadata

    def __send_shell(self, command):
        return subprocess.check_output(f'{self.cmd} -import-path {self.folder} -proto {self.file} -H \'{self.meta}\' {command}', shell=True)        

    def __get_service_list(self):
        output = self.__send_shell('list')
        service_list = [service for service in output.decode('utf-8').split('\n') if service]
        return dict(services=service_list)        

    def get_method_list(self):
        services = self.__get_service_list()['services']
        result = []
        for service in services:
            output = self.__send_shell(f'list {service}')
            method_list = [method for method in output.decode('utf-8').split('\n') if method]
            result.append(dict(service=service, methods=method_list))
        return dict(methods=result)

    def __get_message_schema(self, method):
        output = self.__send_shell(f'describe {method}')
        out = output.decode('utf-8').replace('\n', '',).replace(' ', '').replace(';', '')
        res = out.split('returns')[1].replace('(', '').replace(')', '')
        req = out.split('returns')[0].split('(')[1].replace(')', '')
        schema = dict(request=req, response=res)
        return schema        

    def get_message_template(self, method):
        request = self.__get_message_schema(method)['request']
        output = self.__send_shell(f'-msg-template describe {request}')
        message_template = json.loads(output.decode('utf8').split('Message template:')[1].replace('\n', '').replace(' ', ''))
        return message_template        

    def view_method_scheme(self, method):
        data = self.__get_message_schema(method)
        output_request = self.__send_shell(f'-msg-template describe {data["request"]}')
        output_response = self.__send_shell(f'-msg-template describe {data["response"]}')
        scheme = output_request.decode('utf8') + '\n' + output_response.decode('utf8')
        return scheme
