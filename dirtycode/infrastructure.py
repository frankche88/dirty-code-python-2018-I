'''
Created on 29 abr. 2018

@author: Pc
'''

class IRepository(object):
    def saveSpeaker(self, speaker):
        pass

    def getRegistrationFee(self, experience):
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

    def getRegistrationFee(self, experience):
        if (experience <= 1):
            return 500;
        
        if (experience >= 2 and experience <= 3):
            return 250;
        
        
        if (experience >= 4 and experience <= 5):
            return 100;
        
        
        if (experience >= 6 and experience <= 9):
            return 50;
        
        
        return 0;