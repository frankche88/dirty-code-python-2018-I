'''
Created on 29 abr. 2018

@author: Pc
'''

class IRepository(object):
    def saveSpeaker(self, speaker):
        pass

class SqlServerRepository(IRepository):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def saveSpeaker(self, speaker):
        # TODO: Save speaker to SQL Server DB. For now, just assume success and return 1.
        return 1;
