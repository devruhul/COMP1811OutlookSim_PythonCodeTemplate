#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            Ruhul Amin, SID 001507871                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FA.5.a
class Confidential(Mail):
    """Confidential email type — encrypts body on creation."""

    def __init__(self, m_id, frm, to, date, subject, tag, body):
        # do not change the attributes defined in Mail
        super().__init__(m_id, frm, to, date, subject, tag, body)
        # encrypt the body immediately (as per spec)
        self.encrypt()
        
    def show_email(self):
        """Pretty-print ONLY for confidential emails."""
        return (
            "----- CONFIDENTIAL EMAIL -----\n"
            f"From: {self.frm}\n"
            f"Date: {self.date}\n"
            f"Subject: {self.subject}\n\n"
            "Encrypted Body:\n"
            f"{self.body}\n"
            # later will add flag and read status
            f"Read: {'Yes' if self._read else 'No'}\n"
            f"Flagged: " + ('Yes' if self._flag else 'No') + "\n"
            "------------------------------"
        )
        

    def encrypt(self):
        body = self._body
        # Count words; keep empty strings out
        words = [w for w in body.split(' ') if w != '']
        num_words = len(words)

        encrypted = []
        for ch in body:
            if ch == '.':
                encrypted.append('.')
            elif ch == ' ':
                encrypted.append(' ')
            elif ch.isdigit():
                encrypted.append(chr(ord('a') + int(ch)))  # 0->a, 1->b, ...
            elif ch.isalpha():
                pos = ord(ch.lower()) - ord('a') + 1
                encrypted.append(str(pos * num_words))
            else:
                # preserve any other chars (colon, percent signs etc.)
                encrypted.append(ch)

        self._body = ''.join(encrypted)