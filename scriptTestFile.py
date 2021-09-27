import paramiko

host = "142.93.153.136"
port = 22
username = "cloudssh.us-TestSOC"
password = "Test123!"

command = "ls"

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
