from spydetails import Spy,friends,ChatMessage,spy
from steganography.steganography import Steganography
status_messages_list=["hello , how are you",'hey there ']



def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("Enter image name : ")
    output_path = "image.jpg"
    text = raw_input("Enter text : ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def addfriend():
    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age >=18 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Unable to add friend '

    return len(friends)


def addstatus(currentstatus):
    updated_status=None
    if currentstatus!=None:
        print "Your current status is : "+currentstatus
    else:
        print"You have no status "
    default = raw_input("Do you want to select from older (Y/N) ")
    if default.upper()=='N':
        print "Enter your new status \n "
        new_status=raw_input()
        if len(new_status)>0:
            updated_status=new_status
            status_messages_list.append(updated_status)
    elif default.upper()=='Y':
        pos=1
        for message in status_messages_list:
            print str(pos)+ ". "+message
            pos+=1
        message_selection=int(raw_input("Select your status : "))
        if len(status_messages_list)>=message_selection:
            updated_status=status_messages_list[message_selection-1]

    if updated_status:
        print"Your status is : "+updated_status
    else:
        print "You dont have any updated status "
    return updated_status

def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

def menu():
    flag=1
    currentstatus=None
    while flag:
        choice = int(raw_input("Enter choice \n 1. Status Update \n 2. Add friend \n 3. Send Message  \n 4. Read a message \n 5. Read chat history \n 6.Exit \n"))
        if(choice==1):
            currentstatus=addstatus(currentstatus)
        elif(choice==2):
            number_friends=addfriend()
            print "You have %d friends "%(number_friends)
        elif(choice==3):
            send_message()


        elif choice==4:
            read_message()
        elif choice==5:
            read_chat_history()
        elif choice==6:
            print "Exiting "
            flag=0
ques="Continue as %s %s (Y/N) "%(spy.salutation,spy.name)
existing=raw_input(ques)
if(existing=='y' or existing=='Y'):
    print "Welcome back %s %s "%(spy.salutation,spy.name)
    menu()
elif(existing=='n' or existing=='N'):
    print"Enter the details again \n"
    salutation=raw_input("Enter the salutation : ")
    name=raw_input("Enter spy name : ")
    age=int(raw_input("Enter the spy age : "))
    rating=float(raw_input("Enter the rating of apy : "))
    menu()
