import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ftplib import FTP
import paramiko

browser = webdriver.Chrome(ChromeDriverManager().install())
siteList = open("sites.txt", "r")

host = "142.93.153.136"
port = 22
username = "cloudssh.us-TestSOC"
password = "Test123!"

command = "ls"

for line in siteList:
  try:
    webURL = line.strip()
    print("Opening " + webURL)
    browser.get(webURL)
    time.sleep(2)
  except:
    print("This site didn't load")

siteList.close()
browser.quit()

print("HTTP requests made, now moving on to FTP connection")
time.sleep(3)
print("Engaging FTP Connection")
try:
  conn = FTP('ftp.us.debian.org')
  conn.login()
  conn.retrlines('LIST')
  time.sleep(2)
  print("Connection to FTP succeeded")
  conn.quit()
except:
  print("No connection made to FTP server, pleas try again later")

print("FTP Connection done, now downloading test file from remote host")

try:
  url = "http://speedtest.tele2.net/10MB.zip"
  resp = requests.get(url)
  print(resp.status_code)
except:
  print("Download failed, continuing script")

print("Download has been completed, we are now moving on to making an SSH connection")

try:
    ssh = paramiko.SSHClient()
    print("Creating connection")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    print("Connection created")
    ssh.close()
except:
    print("Connection failed, moving on")

print("Script finished")




