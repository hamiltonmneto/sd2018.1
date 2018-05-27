import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):

    def exposed_line_counter(self, fileobj, function): //exposed_expoe o metodo
        print('Cliente chamou line counter')
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    def exposed_print_name(self, nome, sobrenome):
        return nome + " " + sobrenome

def server():    
    t = ThreadedServer(MyService, port = 18861)
    t.start()
