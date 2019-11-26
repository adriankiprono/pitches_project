import unittest
from app.models import User,Pitch
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the pitch class
    '''

    def setUp(self):
        '''
        set up method that will run before every method
        '''
        self.user_Christine = User(username = 'Christine',password = 'kingkong', email= 'christine@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='test',pitch_content='This is a sample pitch',category="interview",user = self.user_Christine,likes=0,dislikes=0)


    def tearDown(self):
        '''
        method to clear after testcase
        '''

        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        '''
        method to check existance of the variables
        '''
        self.assertEquals(self.new_pitch.pitch_title,'test')
        self.assertEquals(self.new_pitch.pitch_content,'This is a sample pitch')
        self.assertEquals(self.new_pitch.category,"interview")
        self.assertEquals(self.new_pitch.user,self.user_Christine)

    def test_save_pitch(self):
        '''
        method to check if the save function works
        '''
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        '''
        method to check if the find function works
        '''
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)


    