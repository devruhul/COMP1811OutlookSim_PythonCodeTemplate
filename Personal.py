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

    def show_email(self):
        print("PERSONAL")
        print(f"From:{self.frm}")
        print(f"To:{self.to}")
        print(f"Date:{self.date}")
        print(f"Subject:{self.subject}")
        print(f"Body:{self.body}")
        print(f"Read:{self.read}")

    # FB.5.b
    #
    def add_stats(self, body):
        # 1. Get UID (the part before the '@' in sender email)
        uid = self.frm.split("@")[0]

        # 2. Replace the word "Body" in the body text with the UID
        body = body.replace("Body", uid)

        # 3. Split text into words
        words = body.split()

        # 4. Calculate statistics
        word_count = len(words)
        avg_length = sum(len(word) for word in words) // word_count
        longest_word = max(len(word) for word in words)

        # 5. Create statistics message
        stats = (
            f" Stats: Word count:{word_count}, "
            f"Average word length:{avg_length}, "
            f"Longest word length:{longest_word}."
        )

        # 6. Return modified body with stats added
        return body + stats
