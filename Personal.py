#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                                 ###
###            <describe the purpose and overall functionality of the class defined here>      ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES

from Mail import Mail

# FB.5.a
class Personal(Mail):
    """Personal Email class"""

    def __init__(self, m_id, frm, to, date, subject, tag, body):
        super().__init__(m_id, frm, to, date, subject, tag, body)
        

    # FB.5.b
    def add_stats(self):
        """Optional: implement if needed by coursework spec"""
        pass
