#!/Users/fabric/projects/fabric/bin/python

import random
from os import system
from splinter import Browser
from time import sleep
from datetime import datetime


def randomize_mac():
    new_mac = "52:54:00:{:02x}:{:02x}:{:02x}".format(*[random.randint(0, 255) for _ in xrange(3)])
    set_mac(new_mac)
    return new_mac

def restart_wifi():
    system("networksetup -setairportpower en0 off; networksetup -setairportpower en0 on")
    sleep(5)

def set_mac(mac):
    system("ifconfig en0 ether {}".format(mac))

def fill_out_form():
    browser.select('rateplanid', 'spn'); sleep(0.5)
    browser.fill('spn_postal', ''.join(random.sample("0123456789", 5))); sleep(0.5)
    email = ''.join(
        random.sample('aaaaabbcdeeeeefghiiiiijklmnooooopprstuuuuuvwyz', random.randint(4, 8))
    ) + '@gmail.com'
    browser.fill('spn_email', email); sleep(0.5)
    with open('emails.log', 'a') as l: l.write('{}: {}'.format(datetime.now(), email))
    browser.check('spn_terms'); sleep(0.5)
    browser.find_by_value('submit').first.click()
    sleep(10)

""" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  MAIN: ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ """
mac = randomize_mac()
restart_wifi()
browser = Browser('firefox')
try:
    browser.visit('https://xfinity.nnu.com/xfinitywifi/?client-mac={}'.format(mac))
except Exception as e:
    print '\nFirst Error:    ', str(e)[:80], '...'
    restart_wifi()
    set_mac(mac)
    restart_wifi()
    try:
        browser.visit('https://xfinity.nnu.com/xfinitywifi/?client-mac={}'.format(mac))
    except Exception as f:
        print '\nSecond Error:   ', str(f)[:80], '...'
        browser.quit()
        restart_wifi()
        exit()
fill_out_form()
browser.quit()
print '<3'

