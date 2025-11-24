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
    # defining get_email method to retrieve email by ID and mark it as read
    def get_email(self, m_id):
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
    # filtering emails with the email address from the mailbox
    def filter(self, frm):
        filtered_emails = []
        for mail in self._mailbox:
            if mail.frm == frm:
                filtered_emails.append(mail.show_email())

        if not filtered_emails:
            return "No emails found from the given sender."
        return "\n\n".join(filtered_emails)

    # FA.5
    # sorting emails based on the sender's email address
    def sort_date(self):
        """ """
        pass

    # FEATURES B (Partner B)

    # FB.1
    # displaying all the attributes in the pretty format
    def show_emails(self):
        pretty_emails = ""
        for mail in self._mailbox:
            pretty_emails += mail.show_email() + "\n"
        return pretty_emails.strip()

    # FB.2
    # Move email to a new folder by changing its tag and converting type if needed.
    def mv_email(self, m_id, tag):
        index = 0  # manual index counter

        for mail in self._mailbox:
            if mail.m_id == m_id:
                # If moving to confidential
                if tag.lower() == "conf":
                    new_mail = Confidential(
                        mail.m_id,
                        mail.frm,
                        mail.to,
                        mail.date,
                        mail.subject,
                        tag,
                        mail.body,
                    )

                # If moving to personal
                elif tag.lower() == "prsnl":
                    new_mail = Personal(
                        mail.m_id,
                        mail.frm,
                        mail.to,
                        mail.date,
                        mail.subject,
                        tag,
                        mail.body,
                    )

                # Any other tag → general Mail
                else:
                    new_mail = Mail(
                        mail.m_id,
                        mail.frm,
                        mail.to,
                        mail.date,
                        mail.subject,
                        tag,
                        mail.body,
                    )

                # Replace the old email object in the SAME index
                self._mailbox[index] = new_mail

                return str(new_mail)

            index += 1  # move to next position

        return "Email not found."

    # FB.3
    # Mark email as Read or Flagged based on m_type.
    def mark(self, m_id, m_type):
        for mail in self._mailbox:
            if mail.m_id == m_id:
                if m_type.lower() == "read":
                    mail._read = True
                elif m_type.lower() == "flag":
                    mail._flag = True
                return str(mail)
        return "Email not found."

    # FB.4
    # Find and return all emails received on the given date.
    def find(self, date):

        found = []

        for mail in self._mailbox:
            if mail.date == date:
                found.append(mail.show_email())

        if not found:
            return "No emails found on that date."

        return "\n\n".join(found)

    # FB.5
    #
    def sort_from(self):
        """ """
        pass

    # FEATURE 6 (Partners A and B)
    # Creating a new email object with unique m_id and add it to mailbox.
    def add_email(self, frm, to, date, subject, tag, body):

        # Generate unique numeric m_id
        global new_email
        if len(self._mailbox) == 0:
            m_id = "0"
        else:
            ids = [int(mail.m_id) for mail in self._mailbox]
            m_id = str(max(ids) + 1)

        # Determine email type based on tag
        match tag.lower():
            # FA.6 - Confidential email
            case "conf":
                new_email = Confidential(m_id, frm, to, date, subject, tag, body)

            # FB.6 - Personal email
            case "prsnl":
                new_email = Personal(m_id, frm, to, date, subject, tag, body)

            # FA&B.6 - General email
            case _:
                new_email = Mail(m_id, frm, to, date, subject, tag, body)

        # Add the new email to the mailbox
        self._mailbox.append(new_email)

        return new_email
