import os,shutil,subprocess,time

#C:\Users\root\AppData\Local
#USER LOGS#
print ("I WILL GET YOUR LOGS SO YOU CAN SEND THEM TO RIOT")
print ("IF THE APP TAKES TOO LONG, CLICK ON THE WINDOW AND PRESS A RANDOM KEYBOARD KEY")
print ("THIS APP IS MADE BY @FPSHEAVEN_ AND @FREQUENCYCS")
print ("STARTING IN 5")
time.sleep(5)
usr_name=os.getlogin()
vlros_path = os.path.expandvars("%localappdata%\\VALORANT\\saved\\Logs")
desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop");os.chdir(desktop_dir)
os.mkdir("VALORANT_LOGS")
os.chdir(desktop_dir+"\\VALORANT_LOGS")
os.mkdir("VLR_LOGS")
vrl_dsk_path=os.chdir(desktop_dir+"\\VALORANT_LOGS"+"\\VLR_LOGS")
vrl_dsk_path=str(vrl_dsk_path)
print(os.getcwd())
src_folder = vlros_path
dest_folder = vrl_dsk_path
shutil.copytree(src_folder, dest_folder)

#PROCESS LISTS#
print ("GETTING YOUR PROCCESSES")
os.system('tasklist /v > "%USERPROFILE%\\desktop\\VALORANT_LOGS\\Process.txt"')

print ("GETTING YOUR NETWORKING INFO")
time.sleep(3)
#NETWORKINFO LOGS#
output_file = r"%USERPROFILE%\desktop\VALORANT_LOGS\NetworkInfo.txt"
command = "ipconfig /all & ping www.google.com & netsh firewall show config & netsh interface ipv4 show subinterfaces & netsh interface ipv4 show ipstats"
full_command = f"{command} > {output_file}"
subprocess.run(full_command, shell=True)

print ("GETTING YOUR PC INFO")
time.sleep(3)
#DXDIAG
output_file = r"%USERPROFILE%\desktop\VALORANT_LOGS\dxdiag.txt"
command = f"dxdiag /t {output_file}"
subprocess.run(command, shell=True)

#RIOT CLIENT LOGS
print ("GETTING YOUR RIOT CLIENT LOGS")
time.sleep(3)
riot_client_logs_os = os.path.expandvars("%localappdata%\Riot Games\Riot Client\\Logs")
os.chdir(desktop_dir+"\\VALORANT_LOGS")
os.mkdir("RIOT_CLIENT_LOGS");RIOT_CLIENT_LOGS_DSK_DIR=os.chdir(desktop_dir+"\\VALORANT_LOGS"+"\\RIOT_CLIENT_LOGS")
RIOT_CLIENT_LOGS_DSK_DIR=str(RIOT_CLIENT_LOGS_DSK_DIR)

src_folder = riot_client_logs_os
dest_folder =RIOT_CLIENT_LOGS_DSK_DIR
shutil.copytree(src_folder, dest_folder)

#VANGUARD LOGS
print ("GETTING YOUR VANGUARD LOGS")
time.sleep(3)
vgc_logs_os=r"C:\Program Files\Riot Vanguard\logs"
os.chdir(desktop_dir+"\\VALORANT_LOGS")
os.mkdir("VGC_LOGS");vgc_logs=os.chdir(desktop_dir+"\\VALORANT_LOGS"+"\\VGC_LOGS")
vgc_logs=str(vgc_logs)


src_folder = vgc_logs_os
dest_folder =vgc_logs
shutil.copytree(src_folder, dest_folder)


#MAKE ARCHIVE
print ("MAKING IT AN ARCHIVE ON YOUT DESKTOP")
time.sleep(3)
desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
folder_path = os.path.join(desktop_folder, "VALORANT_LOGS")
output_path = os.path.join(desktop_folder, f"{usr_name}_VALORANT_LOGS.zip")

shutil.make_archive(output_path, "zip", folder_path)
os.chdir(desktop_dir)
shutil.rmtree("VALORANT_LOGS")
print("DONE. I AM LEAVING I LOVE YOU :) ")
time.sleep(2)
quit()
