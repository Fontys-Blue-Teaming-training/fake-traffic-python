#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser

import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ftplib import FTP
import paramiko
import threading

# open Globals

browser = webdriver.Chrome(ChromeDriverManager().install())
siteList = open('sites.txt', 'r')

# define Variables

host = '142.93.153.136'
port = 22
username = 'cloudssh.us-TestSOC'
password = 'Test123!'
command = 'ls'


# open Webpages in List

def openWebpage():
    f = open("sites.txt", "r")
    for line in f:
        try:
            url = line.strip()
            print('Opening ' + url)
            browser.get(url)
            time.sleep(2)
        except:
            print ("This site didn't load")
    siteList.close()
    browser.quit()
    print ('HTTP requests made, now moving on to FTP connection')
    time.sleep(3)


# open FTP Connection

def openFTP():
    print ('Engaging FTP Connection')
    try:
        conn = FTP('ftp.us.debian.org')
        conn.login()
        conn.retrlines('LIST')
        time.sleep(2)
        print ('Connection to FTP succeeded')
        conn.quit()
    except:
        print ('No connection made to FTP server, pleas try again later')
        print ('FTP Connection done, now downloading test file from remote host')


# download a file

def downloadFile():
    try:
        url = 'http://speedtest.tele2.net/10MB.zip'
        resp = requests.get(url)
        print (resp.status_code)
    except:
        print ('Download failed, continuing script')
        print ('Download has been completed, we are now moving on to making an SSH connection')


# open SSH Client

def openSSHClient():
    try:
        ssh = paramiko.SSHClient()
        print ('Creating connection')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        print ('Connection created')
        ssh.close()
    except:
        print ('Connection failed, moving on')

# creating and opening threads 2-4
t1 = threading.Thread(target=openWebpage).start()
t2 = threading.Thread(target=openFTP).start()
t3 = threading.Thread(target=downloadFile).start()
t4 = threading.Thread(target=openSSHClient).start()

print ('Script finished')
