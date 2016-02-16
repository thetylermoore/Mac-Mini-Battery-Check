import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())



#try:
#    ssh.connect('1.1.1.1', username='admin_user', password='admin_password')
#except paramiko.SSHException:
#    print ("Connection Failed")
#    quit()

#stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

#for line in stdout.readlines():
#    print "Tyler's Macbook Mouse:" + line.strip()
#ssh.close()

try:
    ssh.connect('1.1.1.2', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Retail Lab Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.2', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Retail Lab Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.3', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 1 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.3', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 1 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.4', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 2 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.4', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 2 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.5', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 3 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.5', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 3 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.6', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 4 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.6', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 4 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.7', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 5 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.7', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 5 Keyboard:" + line.strip()
ssh.close()

#try:
#    ssh.connect('1.1.1.8', username='admin_user', password='admin_password')
#except paramiko.SSHException:
#    print ("Connection Failed")
#    quit()

#stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

#for line in stdout.readlines():
#    print "B100 Room 6 Mouse:" + line.strip()
#ssh.close()

#try:
#    ssh.connect('1.1.1.8', username='admin_user', password='admin_password')
#except paramiko.SSHException:
#    print ("Connection Failed")
#    quit()

#stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

#for line in stdout.readlines():
#    print "B100 Room 6 Keyboard:" + line.strip()
#ssh.close()

try:
    ssh.connect('1.1.1.9', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 7 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.9', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 7 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.10', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 8 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.10', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 8 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.11', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 9 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.11', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 9 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.12', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 10 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.12', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 10 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.13', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 11 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.13', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 11 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.14', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 12 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.14', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 12 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.15', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 13 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.15', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 13 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.16', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 14 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.16', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 14 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.17', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 15 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.17', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 15 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.18', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 17 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.18', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 17 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.19', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 18 Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.19', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Room 18 Keyboard:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.20', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c BNBMouseDevice | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Roxy FW Showroom Mouse:" + line.strip()
ssh.close()

try:
    ssh.connect('1.1.1.20', username='admin_user', password='admin_password')
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command("ioreg -c AppleBluetoothHIDKeyboard | grep '\"BatteryPercent\" ='")

for line in stdout.readlines():
    print "B100 Roxy FW Showroom Keyboard:" + line.strip()
ssh.close()
