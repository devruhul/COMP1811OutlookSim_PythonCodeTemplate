#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.


# FB.5.a
from Mail import Mail


class Personal(Mail):
    def __init__(self, m_id, frm, to, date, subject, tag, body):
        super().__init__(m_id, frm, to, date, subject, tag, body)
        self._body = self.add_stats(self._body)

    # defining show_email method for pretty-printing personal emails
    def show_email(self):
        return (
            "PERSONAL\n"
            f"From: {self.frm}\n"
            f"Date: {self.date}\n"
            f"Subject: {self.subject}\n"
            f"Body:{self.body}\n"
            f"Read " + ("Yes" if self._read else "No") + "\n"
            "------------------------------"
        )

    # FB.5.b
    # defining add_stats method for adding statistics to personal email body
    def add_stats(self, body):

        uid = self.frm.split("@")[0]
        body = body.replace("Body", uid)
        words = body.split()
        word_count = len(words)
        avg_length = sum(len(word) for word in words) // word_count
        longest_word = max(len(word) for word in words)

        stats = (
            f" Stats: Word count:{word_count}, "
            f"Average word length:{avg_length}, "
            f"Longest word length:{longest_word}."
        )

        return body + stats
