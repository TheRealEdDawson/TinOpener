import requests
import logging
import datetime
import sys

# Set connecting site details
URL = sys.argv[1]
userName = sys.argv[2]
passWord = sys.argv[3]

# Checking that all the arguments were entered on the command line, exiting with a message if not.
if len(sys.argv) < 3:
    argumentsnotset = '\nError: one or more arguments were not passed. \n\nUsage is like so: \n\nPython tinopener.py SITE-URL USERNAME PASSWORD'
    print argumentsnotset
    sys.exit(1)	

# Set up logging
loggydatestamp = datetime.date.today().strftime("%Y-%m-%d %H:%M")
logfilename = str(datetime.date.today()) + '-TinOpener' + '.log'
print 'Logging to ' + logfilename
logging.basicConfig(filename=logfilename,filemode='w',level=logging.INFO,format='%(asctime)s %(message)s')
initialloggystring = 'New connection started at ' + loggydatestamp
print initialloggystring
logging.info(initialloggystring)

def main():
    #Start a session so we can have persistent cookies
    session = requests.session(config={'verbose': sys.stderr})
    #This is the form data that the page sends when logging in
    login_data = {
        'j_username': userName,
        'j_password': passWord,
        'login': 'Sign In',
    }

# Authenticate
    r = session.post(URL, data=login_data)
    print r.status_code
    logging.info(r.status_code)
    logging.info(r.headers)
    print r.encoding
    logging.info(r.encoding)
    logging.info(r.text)
    logging.info(r.json)
    # Try accessing a page that requires you to be logged in
    r = session.get('https://ninefold.com/portal/portal/home')
    print r.status_code
    logging.info(r.status_code)
    logging.info(r.headers)
    print r.encoding
    logging.info(r.encoding)
    logging.info(r.text)
    logging.info(r.json)

if __name__ == '__main__':
    main()

# Legacy Block
#r = requests.get(siteUrl, auth=(userName, passWord))


endloggystring = "\n*** END PROCESS ***\n"
logging.info(endloggystring)

#http://stackoverflow.com/questions/8316818/login-to-website-using-python