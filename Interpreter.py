#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Interpreter program                                                            ###
###            Used to as the main program that program will manage all OutlookSim operations ###
###            automatically in response to user commands via an interactive command-line     ###
###            interface. The interpreter represents the user interacting with their mailbox. ###
### Partner A:                                                                                ###
###         Ruhul Amin, SID 001507871                                                         ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE FUNCTION NAMES
# replace "pass" with your own code as specified in the CW spec.

from MailboxAgent import *
import random, string


# gen_bdy Generates random text for the email body
# DO NOT MODIFY
def gen_bdy():
    """generates email body message
    :rtype: string"""
    snt = ""
    for i in range(random.randint(1, 10)):
        snt += (
            "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
            + " "
        )
    return f"Body{str(random.randint(0, 140))}. {snt.capitalize()[:-1]}."


# gen_msg generates a string of emails separated by "----"
#    Used to simulate emails in Outlook mailboxes
#    The output is a string of emails that should be used in your code as required in the CW spec.
# DO NOT MODIFY
def gen_emails():
    """generates list of email strings
    :rtype: list"""
    msgs, msg_id = [], 0
    for i in range(40):  # sent 40 email increased 1
        msg = ""
        for j in range(30):  # to 30 destinations each
            msg += f"ID:{str(msg_id)}" + "\n"
            msg += f"From:email{random.randint(0, 15)}@gre.ac.uk\n"
            msg += f"To:email{random.randint(0, 80)}@gre.ac.uk\n"
            msg += f"Date:{random.randint(1, 29)}/{random.randint(0, 12)}/2025\n"
            msg += f"Subject:subject{random.randint(0, 100)}\n"
            msg += f"Tag:tag{random.randint(0, 6)}\n"
            msg += f"Body:{gen_bdy()}\n"
            msg += "Flag:False\n"
            msg += "Read:False\n"
        msgs.append(msg)
        msg_id += 1
    return msgs


# DO NOT MODIFY
def display_command_help():  # DO NOT MODIFY (used in loop function)
    """Displays command line help"""
    print("Interpreter Commands:")
    print(
        "get <m_id> | ",  # A.1&2 Command to get and display email given email ID - e.g. get 10
        "lst | ",  # B.1 Display entire mailbox - e.g. lst
        "mv <m_id> <tag> | ",  # B.2 Move email with given ID to folder indicated in given tag - e.g. mv 10 conf (i.e. change current tag to conf), then display that email
        "del <m_id> | ",  # A.3 Delete email with given ID by moving to bin - e.g. del 10 (i.e. change current tag to bin), then display that email
        "mrkr <m_id> | ",  # B.3 Mark email with given ID as Read then display that email
        "mrkf <m_id> | ",  # B.3 Mark email with given ID as Flagged then display that email
        "flt <frm> | ",  # A.4 Filter and display all emails from a given name/email address - e.g. flt email13
        "fnd <date> | ",  # B.4 Find and display all emails received on a given date - e.g. fnd 12/3/2025
        "add <email>",
    )  # A.5&6 and B.5&6 simulate send email by adding emails to the mailbox
    # example add prompts:
    # add email1223@gre.ac.uk email723@gre.ac.uk 29/5/2025 subject99 conf %%Body99911. Isfeo afwco sxzmp.
    # add email142@gre.ac.uk email788@gre.ac.uk 29/5/2025 subject88 prsnl %%Body11445. Isfffffeo afffwco sxzmp.
    # add email116@gre.ac.uk email142@gre.ac.uk 29/5/2025 subject36 tag1 %%Body:Body68. Wods vmm tskgdrxzrk.


# loop repeatedly asks for command input until 'end' is entered
# DO NOT MODIFY FUNCTION NAME
# - Replace 'pass' with the code necessary to call class/methods relevant for each command
# - Completed as a group
def loop():
    mba = MailboxAgent(
        gen_emails()
    )  # mba is an instance of the MailboxAgent class DO NOT MODIFY
    display_command_help()  # simply display the interpreter command-line commands as help
    line = input(
        "mba > "
    )  # displays a command-line prompter for users to enter command script
    words = line.split(" ")  # separates the command from the script arguments
    command, args = (
        words[0],
        words[1:],
    )  # command is one of the interpreter script commands outlined in the help above
    # args is a list of arguments each command may take.
    while command != "end":
        match command:
            # Partners A and B
            # Replace each pass statement below with a call to the relevant mba methods as described in the CW spec
            # FA/B.6
            case "add":
                # example command prompt:
                # add email1223@gre.ac.uk email723@gre.ac.uk 29/5/2025 subject99 conf %%Body99911. Isfeo afwco sxzmp.
                # add email142@gre.ac.uk email788@gre.ac.uk 29/5/2025 subject88 prsnl %%Body11332. Isfffffeo sxzmp.
                # add email116@gre.ac.uk email142@gre.ac.uk 29/5/2025 subject36 tag1 %%Body:Body68. Wods vmm tskgdrxzrk.
                # Passing all the arguments to create email object and add to mailbox
                frm = args[0]
                to = args[1]
                date = args[2]
                subject = args[3]
                tag = args[4]
                body = " ".join(args[5:])  # from 5th index to end of list
                if body.startswith("%%"):
                    body = body[2:]

                mba.add_email(frm, to, date, subject, tag, body)
                print("Email added to mailbox.")

            case "del":
                # getting the email ID from args list to delete email
                delete_email_id = args[0]
                print(mba.del_email(delete_email_id))

            case "flt":
                # calling filter method from MailboxAgent class to filter emails from given sender
                sender = args[0]
                print(mba.filter(sender))

            case "fnd":
                # finding emails from given date
                date = args[0]
                print(mba.find(date))

            case "get":
                #  displaying email with given ID
                get_email_id = args[0]
                print(mba.get_email(get_email_id))

            case "lst":
                # displaying entire mailbox
                email = mba.show_emails()
                print(email)

            case "mrkr":
                #    marking email with given ID as Read then display that email
                mark_read_email_id = args[0]
                print(mba.mark(mark_read_email_id, "read"))

            case "mrkf":
                #    marking email with given ID as Flagged then display that email
                mark_flag_email_id = args[0]
                print(mba.mark(mark_flag_email_id, "flag"))

            case "mv":
                # moving email with given ID to folder in given tag then display that email
                move_email_id = args[0]
                tag = args[1]
                print(mba.mv_email(move_email_id, tag))

        line = input("mba > ")
        words = line.split(" ")
        command, args = words[0], words[1:]


if __name__ == "__main__":
    loop()
