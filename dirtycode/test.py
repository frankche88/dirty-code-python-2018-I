'''
Created on 29 abr. 2018

@author: Pc
'''
import unittest
from dirtycode.infrastructure import SqlServerRepository
from dirtycode.domain import Speaker, WebBrowser, Session


class Test(unittest.TestCase):


    def setUp(self):        
        self._repository = SqlServerRepository()
        
        pass


    def tearDown(self):
        pass


    
    def test_register_EmptyFirstName_ThrowsArgumentNullException(self):
        speaker = self.getSpeakerThatWouldBeApproved()
        speaker.setFirstName("")
        
        with self.assertRaises(ValueError):
            speaker.register(self._repository)
            

    def test_register_EmptyLastName_ThrowsArgumentNullException(self):
        speaker = self.getSpeakerThatWouldBeApproved();
        speaker.setLastName("");
        with self.assertRaises(ValueError):
            speaker.register(self._repository)
    
    def test_register_EmptyEmail_ThrowsArgumentNullException(self):
        speaker = self.getSpeakerThatWouldBeApproved();
        speaker.setEmail("");
    
        with self.assertRaises(ValueError):
            speaker.register(self._repository)
    
    def test_register_WorksForPrestigiousEmployerButHasRedFlags_ReturnsSpeakerId(self):
        speaker = self.getSpeakerWithRedFlags();
        speaker.setEmployer("Microsoft");

        # act
        speakerId = speaker.register(SqlServerRepository());

        # assert
        self.assertTrue(speakerId);
        
    def test_register_HasBlogButHasRedFlags_ReturnsSpeakerId(self):
        speaker = self.getSpeakerWithRedFlags();

        speakerId = speaker.register(SqlServerRepository());

        self.assertTrue(speakerId);
    
    def test_register_HasCertificationsButHasRedFlags_ReturnsSpeakerId(self):
        speaker = self.getSpeakerWithRedFlags();
        speaker.setCertifications(["cert1", "cert2", "cert3", "cert4"]);

        speakerId = speaker.register(SqlServerRepository());

        self.assertTrue(speakerId)
        
    #### util methds
    
        
    def getSpeakerThatWouldBeApproved(self):
        speaker = Speaker ()

        speaker.setFirstName("First");
        speaker.setLastName("Last");
        speaker.setEmail("example@domain.com");
        speaker.setEmployer("Example Employer");
        speaker.setHasBlog(True);
        speaker.setBrowser(WebBrowser ("test", 1))
        speaker.setExp(1);
        #self._speaker.setCertifications([]);
        speaker.setBlogURL("");
        sessions = []
        sessions.append(Session("test title", "test description"))
        speaker.setSessions(sessions);

        return speaker;
    
    def getSpeakerWithRedFlags(self):
        speaker = self.getSpeakerThatWouldBeApproved();
        speaker.setEmail("tom@aol.com");
        speaker.setBrowser(WebBrowser("IE", 6));
        return speaker;
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()