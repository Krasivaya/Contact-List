import unittest # Importing the unittest module
from contact import Contact # Importing the contact class

class TestContact(unittest.TestCase):
    '''
    Test class that desfines test cases for the contact class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_contact = Contact('Carine','I. SEMWAGA','0788206956','semwagacarine@gmail.com')
        # Create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.first_name,'Carine')
        self.assertEqual(self.new_contact.last_name,'I SEMWAGA')
        self.assertEqual(self.new_contact.phone_number,'0788206956')
        self.assertEqual(self.new_contact.email,'semwagacarine@gmail.com')
        
        if __name__ == '__main__':
            unittest.main()
    
