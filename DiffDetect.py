import urllib
import urllib2
import sys
import pdb
import hashlib
import time
from twilio.rest import TwilioRestClient
import random
from Proxy import Proxy



URL  = sys.argv[1]
DIFF_TAG = "<span style=color: green>Online ticketing will commence in mid March</span>"

def sendSMS():
 
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACb3d20332ed2448170aa2c67323a959fa"
    auth_token  = "5e9bd75169e83de8118f285d63fdc0d3"
    client = TwilioRestClient(account_sid, auth_token)
 
    message = client.messages.create(body=URL, from_="+17795483014", to="+13128886582") 
    print message.sid


def computeMD5hash(s):

    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def requestPage(URL):

    response = None
    try:
        req = urllib2.Request(URL)
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print "Error on URL: " + e.code
        print "Error on URL: " + e.read()

    #If server is throwing error, then we will try using connection from proxy
    #TODO: Look for the error code, then make this request

    if response is None:
        time.sleep(5)
        requestPage(URL)

    return response
	
	

def calculateHashOfURL():

    response = requestPage(URL)

    the_page = response.read()
    #Remove \t and \n 
    the_page = the_page.replace("\t","")
    the_page = the_page.replace("\n","")
    the_page = the_page.replace("\"","")

    #print "Content is "+the_page

    return the_page

def main():


    while True:
        SLEEP = random.randint(1,3)
        time.sleep(SLEEP)

        new_content = calculateHashOfURL()
        
        if DIFF_TAG not in new_content:
            print "Web site updated"
            sendSMS()
            break

if __name__ == "__main__":
    main()
