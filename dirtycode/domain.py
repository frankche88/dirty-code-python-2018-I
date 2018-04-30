
'''
Created on 29 abr. 2018

@author: Pc
'''
from array import array
from enum import Enum

from exceptions import *

class BrowserName(Enum):
    Unknown = 1
    InternetExplorer = 2
    Firefox = 3
    Chrome = 4
    Opera = 5
    Safari = 6
    Dolphin = 7
    Konqueror = 8
    Linx = 9

class Session(object):
    '''
    classdocs
    '''


    def __init__(self, title, description):
        '''
        Constructor
        '''
        self._approved = True
        self._programLanguage = ['Cobol', 'Punch Cards', 'Commodore', 'VBScript']
        self._title = title
        self._description = description
        
        if(title and description) :
            for languaje in self._programLanguage:
                if(languaje in title or languaje in description):
                    self._approved = False;
                    break
            
        
    def getTitle(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def isApproved(self):
        return self._approved

class WebBrowser(object):
    def __init__(self, name, majorVersion):
        self._name = self.TranslateStringToBrowserName(name)
        self._majorVersion = majorVersion

    def TranslateStringToBrowserName(self, name):
        if "IE" in name:
            return BrowserName.InternetExplorer
        # TODO: Add more logic for properly sniffing for other browsers.
        return BrowserName.Unknown
    
    

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name
    
    def getMajorVersion(self):
        return self._majorVersion

    def setMajorVersion(self, majorVersion):
        self._majorVersion = majorVersion



class Speaker(object):
    '''
    classdocs
    '''


    def __init__(self):
        self._MIN_BROWSER_VERSION = 9
        self._MIN_CERTIFICATES = 3
        self._MIN_YEAR_OF_EXPERIENCE = 10
        self._domains = ("aol.com", "hotmail.com", "prodigy.com", "compuserve.com")
        self._employers = ["Pluralsight", "Microsoft", "Google", "Fog Creek Software", "37Signals", "Telerik"]
        
        self._firstName = ""
        self._lastName = ""
        self._email = ""
        self._experience = 0
        self._hasBlog = False
        self._blogURL = ""
        self._browser = BrowserName.Unknown
        self._certifications = []
        self._employer = ""
        self._registrationFee = 0
        self._sessions = []
        
    def isSessionApproved(self):
        isApproved = True
        for session in self._sessions:
            if(not session.isApproved()):
                isApproved = False;
                break;
        return isApproved;
    
    def isGoodSpeaker(self):
        isGoodSpeaker = False
        haveExperience = self._experience > self._MIN_YEAR_OF_EXPERIENCE
        haveMinCertificates = len(self._certifications) > self._MIN_CERTIFICATES

        isGoodSpeaker = ((haveExperience or self._hasBlog or haveMinCertificates or self._employer in self._employers))
        
        if (not isGoodSpeaker):
            
            splitted = self._email.split("@")
            emailDomain = splitted[splitted.length - 1]

            isValidBrowser = not(self._browser.getName() == WebBrowser.BrowserName.InternetExplorer and self._browser.getMajorVersion() < self._MIN_BROWSER_VERSION);
            
            if (not self._domains.contains(emailDomain) and isValidBrowser):
                isGoodSpeaker = True;
            
        return isGoodSpeaker;
    
    def register(self, repository):
        speakerId = 0;        
        
        if (not self._firstName):
            raise ValueError("First Name is required")
        
        if (not self._lastName):
            raise ValueError("Last name is required.")
        
        if (not self._email):
            raise  ValueError("Email is required.")
                    
        if (not self.isGoodSpeaker()):
            raise SpeakerDoesntMeetRequirementsException("Speaker doesn't meet our abitrary and capricious standards.");
        
        if (len(self._sessions) == 0):
            raise ValueError("Can't register speaker with no sessions to present.");
                        
        if (not self.isSessionApproved()):
            raise NoSessionsApprovedException("No sessions approved.");


        self._registrationFee = repository.getRegistrationFee(self._experience);
        

        speakerId = repository.saveSpeaker(self);


        return speakerId;
    def setFirstName(self, firstName):
        self._firstName = firstName
        
    def setLastName(self, lastName):
        self._lastName = lastName
    
    def setEmail(self, email):
        self._email = email
    
    def setEmployer(self, employer):
        self._employer = employer
    
    def setHasBlog(self, hasBlog):
        self._hasBlog = hasBlog
    
    def setBrowser(self, webBrowser):
        self._browser = webBrowser
    
    def setExp(self, experience):
        self._experience = experience;
    
    def setCertifications(self, certificates):
        self._certifications = certificates
    
    def setBlogURL(self, blogURL):
        self._hasBlog = blogURL
        
    def setSessions(self, sessions):
        self._sessions = sessions