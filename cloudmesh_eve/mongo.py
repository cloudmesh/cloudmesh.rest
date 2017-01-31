# TODO: complete
# for executing shell commands please do not reinvent the whele but use

# https://github.com/cloudmesh/client/blob/master/cloudmesh_client/common/Shell.py
# if commands are missing or are not working we can fix that in cloudmesh_client

from __future__ import print_function

from cloudmesh_client.common.Shell import Shell
from cloudmesh_client.common.util import grep


def log_print(msg):
    # temporarily used till we switch to real logger
    print('mongod:' + msg)


class Mongo(object):
    def __init__(self, port=5000):
        self.parameters = {}
        self.parameters['port'] = port
        self.parameters['dbpath'] = "~/.cloudmesh/data/db"
        self.parameters['bind_ip'] = "127.0.0.1"
        print(self.parameters)

    def start(self):
        """starts the mongo service."""
        r = Shell.execute(
            'mongod --port {port} -dbpath {dbpath} -bind_ip {bind_ip} start'.format(**self.parameters).split(' '))
        print(r)
        log_print('started')
        self.status()

    def stop(self):
        """stops the mongo service."""
        r = Shell.execute('mongod stop'.split(' '))
        print(r)
        # subprocess.call(mongod --shutdown)
        log_print('stopped')

    def status(self, format=None):
        """returns the status of the service. if no parameter. if format
        is specified its returned in that fomat. txt, json, XML,
        allowed
        """
        output = Shell.ps = ('-A')
        print (output)
        if 'mongod' in output:
            log_print('running')
        else:
            log_print('stopped')

    def reset(self):
        """stops the service and deletes the database, restarts the service."""
        r = Shell.execute('mongod stop'.split(' '))
        print (r)
        log_print('stopped')

        # print("not yet implemented")
        pass

    def delete(self):
        """just deletes all data in the database"""
        raise NotImplementedError
        pass

    def pid(self):
        """returns the pid of the mongo db servier"""
        output = Shell.ps=('-A')
        print (output)
        pid = grep("mongod").strip().split(' ')[0]
        return pid

    def log(self, path):
        """sets the log file to the given path"""
        raise NotImplementedError
        pass

# TODO: define test programs with nosetest