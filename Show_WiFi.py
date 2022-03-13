# Import subprocess so we can use system commands.
import subprocess

# Import the re module so we can make use of regular expressions. 
import re

print()
print("******************************************************************")
print("                       __________     _______                     ")
print("                      |___    ___|   |   ____|                    ")
print("                          |  |       |  |                         ")
print("                       _  |  |       |  |                         ")
print("                      | |_|  |  _    |  |____                     ")
print("                      |______| (_)   |_______|                    ")
print("******************************************************************")
print("------------------------------------------------------------------")
print("                  SHOW PASSWORDS OF WIFIS                         ")
print("------------------------------------------------------------------")
print()

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()


profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

# Creamos una lista para optener los passwords
wifi_list = []


if len(profile_names) != 0:
    for name in profile_names:
       
        wifi_profile = { }
       
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
     
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
        
            wifi_profile["User_Wifi"] = name
            
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
          
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
         
            if password == None:
                wifi_profile["Password"] = None
            else:
            
                wifi_profile["Password"] = password[1]
           
            wifi_list.append(wifi_profile) 
print("------------------------------------------------------------------")
for x in range(len(wifi_list)):

    print(wifi_list[x]) 

print("------------------------------------------------------------------")