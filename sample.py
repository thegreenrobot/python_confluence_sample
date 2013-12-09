from xmlrpclib import Server
from jinja2 import Environment, FileSystemLoader
import json
import fnmatch
import os

class Wiki:
    """ I like writing stuff to the wiki """

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('./templates'))
        self.template = self.env.get_template('wiki.html')
        self.your_name = 'Peter Gibbons'
        self.file_directory = './sample_data/'
        self.list_of_files = []
        self.servers = []

    def find_json_files(self):
        for file in os.listdir(self.file_directory):
            if fnmatch.fnmatch(file, '*.json'):
                self.list_of_files.append(file)

    def generate_content(self):

        self.find_json_files()

        for file_name in self.list_of_files:
            node_data = {}
            json_file = open(self.file_directory + file_name)
            data = json.load(json_file)

            node_data['fqdn'] = data['fqdn']
            node_data['ipaddress_public'] = data['ipaddress_public']
            node_data['ipaddress_private'] = data['ipaddress_private']
            node_data['ipaddress_servicenet'] = data['ipaddress_servicenet']

            self.servers.append(node_data)

        content = self.template.render(your_name=self.your_name, servers=self.servers)
        
        # WIKI URL
        s = Server("https://somecompany.com/rpc/xmlrpc")
        # WIKI Credentials
        token = s.confluence2.login("username", "password")
        # WIKI Space and Page Name
        page = s.confluence2.getPage(token, "~username", "Test Page")
        page["content"] = content
        s.confluence2.storePage(token, page)

if __name__ == "__main__":
    wiki = Wiki()
    wiki.generate_content()
