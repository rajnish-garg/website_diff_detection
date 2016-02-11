import urllib
import urllib2
import sys
import pdb
import hashlib
import time
from twilio.rest import TwilioRestClient
import random



URL  = sys.argv[1]

def sendSMS():
 
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = ""
    auth_token  = ""
    client = TwilioRestClient(account_sid, auth_token)
 
    message = client.messages.create(body="http://www.go90sanfrancisco.com/", from_="+16692536505", to="+14086661680") 
    print message.sid


def computeMD5hash(s):

    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def calculateHashOfURL():

    req = urllib2.Request(URL)
    response = urllib2.urlopen(req)
    the_page = response.read()
    #Remove \t and \n 
    the_page = the_page.replace("\t","")
    the_page = the_page.replace("\n","")
    the_page = the_page.replace("\"","")

    #print "Content is "+the_page

    return the_page

def main():

    while True:
        SLEEP = random.randint(15,30)
        time.sleep(SLEEP)

        new_content = calculateHashOfURL()
        if "div class=body grp p0><p>COMING SOON" not in new_content:
            print "Web site updated"
            sendSMS()
            break

if __name__ == "__main__":
    main()