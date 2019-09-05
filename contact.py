import pyperclip # Importing pyperclip module

class Contact:
    """
    Class that generates new instances of contacts
    """

    
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    contact_list = [] # Empty contact list
    # Init method up here 
    def save_contact(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        Contact.contact_list.append(self)
    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''
        Contact.contact_list.remove(self)
    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact that matches that number.
        Args:
            number: phone number to search for
        Returns:
            contact of person that matches the nnumber.
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    @classmethod
    def contact_exists(cls, number):
        '''
        Method that checks if a contact exists from the contact list.
        Args: 
            nnumber: phone number to search if it exitst
        Returns:
            Boolean: True or False depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True
        return False
    @classmethod
    def display_contacts(cls):
        '''
        Method that returns the contact list
        '''
        return cls.contact_list
    @classmethod
    def copy_email(cls, number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)