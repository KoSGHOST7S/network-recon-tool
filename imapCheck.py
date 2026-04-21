#!/usr/bin/python3

#add imports
from socket import *
import imaplib

# define IMAP function that checks if IMAP is open
def imapCheck(tgthost):
# trys to connect to to port 443 but if not then jump to except
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgthost,143))
        connSkt.close()
        # if the port can be connected to login
        imap = imaplib.IMAP4(tgthost)
        imap.login('admin','admin')
        # if our login creds work request the mail from imbox
        folders = imap.select('INBOX')
        print('IMAP exists: ' + str(folders[1][0]))
    except:
        print('no connection found...')
    finally:
        connSkt.close()
def main():
        ip = '192.168.1.11'
        imapCheck(ip)

if __name__ == '__main__':
        main()


