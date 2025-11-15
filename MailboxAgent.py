#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            Ruhul Amin, SID 001507871                              ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *

class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, m_id):
    #    get all given email id from mailbox
        for mail in self._mailbox:
            if mail.m_id == m_id:
                mail._read = True
                return str(mail)
        return "Email not found."

    # FA.3
    # 
    def del_email(self, m_id):
    # A.3 Delete email with given ID and change current tag to bin then display that email
        for mail in self._mailbox:
            if mail.m_id == m_id:
                mail._tag = 'bin'   # changing the tag to bin
                mail._read = True
                return str(mail)
        return "Email not found."
    
    # FA.4
    # 
    def filter(self, frm):
        # filtering emails with the email address from the mailbox
        filtered_emails = []
        for mail in self._mailbox:
            if mail.frm == frm:
                filtered_emails.append(mail.show_email())  

        if not filtered_emails:
            return "No emails found from the given sender."
        return "\n\n".join(filtered_emails)


    # FA.5
    # 
    def sort_date(self):
        """  """
        pass


# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        # displaying all the attributes in the pretty format
        pretty_emails = ""
        for mail in self._mailbox:
            pretty_emails += mail.show_email() + "\n"
        return pretty_emails.strip()

    # FB.2
    # 
    def mv_email(self, m_id, tag):
        """  """
        pass

    # FB.3
    # 
    def mark(self, m_id, m_type):
        """  """
        pass

    # FB.4
    # 
    def find(self, date):
        """  """
        pass

    # FB.5
    # 
    def sort_from(self):
        """  """
        pass


# FEATURE 6 (Partners A and B)
    # 
    def add_email(self, frm, to, date, subject, tag, body):
        """Create a new email object (Mail / Confidential / Personal) with a unique m_id
        and add it to this MailboxAgent's mailbox. Returns the created Mail object.
        """
        # generate a unique numeric id based on existing numeric m_id values
        existing_nums = []
        for mail in self._mailbox:
            try:
                existing_nums.append(int(mail.m_id))
            except (ValueError, TypeError):
                # skip non-numeric ids
                continue
        new_num = max(existing_nums) + 1 if existing_nums else 0
        new_id = str(new_num)

        # choose class based on tag
        tag_l = tag.lower()
        if tag_l == 'conf':
            added_email = Confidential(new_id, frm, to, date, subject, tag, body)
        elif tag_l == 'prsnl':
            added_email = Personal(new_id, frm, to, date, subject, tag, body)
        else:
            added_email = Mail(new_id, frm, to, date, subject, tag, body)

        # append to this instance's mailbox
        self._mailbox.append(added_email)

        # return the created object (caller can print or ignore)
        return added_email
