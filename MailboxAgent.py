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

    def __init__(self, email_data):  # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(
            email_data
        )  # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):  # DO NOT CHANGE
        """generates mailbox data structure
        :ivar: String
        :rtype: list"""
        mailbox = []
        for e in email_data:
            msg = e.split("\n")
            mailbox.append(
                Mail(
                    msg[0].split(":")[1],
                    msg[1].split(":")[1],
                    msg[2].split(":")[1],
                    msg[3].split(":")[1],
                    msg[4].split(":")[1],
                    msg[5].split(":")[1],
                    msg[6].split(":")[1],
                )
            )
        return mailbox

    # FEATURES A (Partner A)
    # FA.1
    #
    def get_email(self, m_id):
        #    get given email id from mailbox
        for mail in self._mailbox:
            if mail.m_id == m_id:
                mail._read = True
                return str(mail)
        return "Email not found."

    # FA.3
    # A.3 Delete email with given ID and change current tag to bin then display that email
    def del_email(self, m_id):
        for mail in self._mailbox:
            if mail.m_id == m_id:
                mail._tag = "bin"  # changing the tag to bin
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
        """ """
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
        """ """
        pass

    # FB.3
    #
    def mark(self, m_id, m_type):
        """ """
        pass

    # FB.4
    #
    def find(self, date):
        """ """
        pass

    # FB.5
    #
    def sort_from(self):
        """ """
        pass

    # FEATURE 6 (Partners A and B)
    #
    def add_email(self, frm, to, date, subject, tag, body):
        """Create a new email object with unique m_id and add it to mailbox."""

        #  Generate unique numeric m_id
        if len(self._mailbox) == 0:
            m_id = "0"
        else:
            # convert all m_id to int and get max
            ids = [int(mail.m_id) for mail in self._mailbox]
            m_id = str(max(ids) + 1)

        # Create correct email type depending on tag
        tag_lower = tag.lower()

        if tag_lower == "conf":
            # Confidential email object
            new_email = Confidential(m_id, frm, to, date, subject, tag, body)

        elif tag_lower == "prsnl":
            # Personal email object
            new_email = Personal(m_id, frm, to, date, subject, tag, body)

        else:
            # General Mail email object
            new_email = Mail(m_id, frm, to, date, subject, tag, body)

        # Append to mailbox
        self._mailbox.append(new_email)

        return new_email
