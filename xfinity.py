#!/Users/fabric/projects/fabric/bin/python

import random
from os import system
from splinter import Browser
from time import sleep
from datetime import datetime


def print_mac():
   # print current mac address (extract it from ifconfig)
   system("sudo ifconfig en0 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'")

def change_mac():
   # tell user the old mac address
   print 'old mac address:'
   print_mac()
   # calculate new random mac address and tell the user
   new_mac = "52:54:00:{:02x}:{:02x}:{:02x}".format(*[random.randint(0, 255) for _ in xrange(3)])
   print 'new mac address:'; print new_mac
   # set new mac address and tell user
   system('sudo ifconfig en0 ether {}'.format(new_mac)); sleep(1)
   print 'actual new mac address:'; print_mac()
   return new_mac

def makesure(mac):
   # restart wifi
   system("networksetup -setairportpower en0 off; networksetup -setairportpower en0 on")
   # re-assign new mac address just to make sure
   system("sudo ifconfig en0 ether {}".format(mac)); sleep(1)

def fill_signup_form():
   # choose $0.00 free plan
   browser.select("rateplanid", "spn"); sleep(1)
   # enter random zipcode
   browser.fill('spn_postal', ''.join(random.sample("0123456789", 5))); sleep(1)
   # enter random email
   email = ''.join(
      random.sample('aaaaabbcdeeeeefghiiiiijklmnooooopprstuuuuuvwyz', random.randint(4, 8))
   ) + '@gmail.com'
   browser.fill('spn_email', email); sleep(1)
   system("echo {}: {} >> funny_emails.log".format(datetime.now(), email))
   # agree to terms of service ;)
   browser.check('spn_terms'); sleep(1)
   # submit form!
   browser.find_by_value('submit').first.click(); sleep(8)

""" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  MAIN: ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ """
# change mac address
mac = change_mac()
# open browser and try to go to sign up site, if failure try to do some tweaks and try again or quit
browser = Browser('firefox')
try:
   browser.visit('https://xfinity.nnu.com/xfinitywifi/?client-mac={}'.format(mac)); sleep(1)
except Exception as e:
   print 'Error: ' + str(e)
   makesure(mac)
   sleep(8)
   try:
      browser.visit('https://xfinity.nnu.com/xfinitywifi/?client-mac={}'.format(mac)); sleep(1)
   except Exception as e:
      print 'Error: ' + str(e)
      browser.quit()
      makesure(mac)
      exit()
# fill out sign up form
fill_signup_form()
# quit firefox when done
browser.quit()
print '<3'
