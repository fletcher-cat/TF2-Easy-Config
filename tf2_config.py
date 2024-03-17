#import os to allow file path usage
import os
print("The 'default' settings are the ones I use and find best. You may change them if you'd like, but I would recommend against it unless you have a specific reason to. You may press enter on every option and be all set. These settings are based off Aar's video and my preferences. https://www.youtube.com/watch?v=rRxFpr5Javg")

#ask where TF2 install is to create autoexec.cfg in the directory
folder_path = input(r"Where is the TF2 cfg folder located? (Team Fortress 2\tf\cfg) Enter the file path, if you used the defeault location, leave blank. ")

#If the length of the input is zero set the filepath to the default install location
if len(folder_path) == 0 :
    folder_path = "C:/Program Files (x86)Steam/Steamapps/common/Team Fortress 2/tf/cfg"

#time to write the config file
fov_value = input("Enter the FOV you'd like to use. (Default and maximum value is 90, minimum is 70): ")

#if nothing is entered default FOV to 90 degrees
if len(fov_value) == 0 :
    fov_value = "90"

#viewmodel fov 
viewmodel_fov_value = input("Enter the viewmodel FOV you'd like to use. (Default value is 70): ")

#if nothing is entered default viewmodel FOV to 70 degrees
if len(viewmodel_fov_value) == 0 :
    viewmodel_fov_value = "70"

#minimum viewmodels
min_viewmodels = input("Would you like to use minimum viewmodels? This makes it so that the guns on your screen are smaller and you can see more of the action. Enter 'n' for no. (Default = yes): ")
if len(min_viewmodels) == 0 :
    min_viewmodels = "y"

#define file name and combine the name and the directory
filename = "autoexec.cfg"
file_path = os.path.join(folder_path, filename)

#write the autoexec.cfg file
with open(file_path, 'w') as file:
    file.write('//Created by TF2 Easy Config.' + "\n")
    #write networking options
    file.write("cl_interp 0.0325" + "\n" + "cl_interp_ratio 1" + "\n" + "rate 97000" + "\n" + "cl_updaterate 66" + "\n" + "cl_cmdrate 66" + "\n")
    #write minimum viewmodels
    if min_viewmodels == "n" :
        file.write("tf_use_min_viewmodels 0" + "\n")
    else: file.write("tf_use_min_viewmodels 1" + "\n")
    #write viewmodel fov
    file.write("viewmodel_fov " + viewmodel_fov_value + "\n")
    #write general fov
    file.write("fov_desired " + fov_value)

print("Writing settings. Includes optimal network settings.")
print("Done." + "\n" "You may want to check out mastercomfig next, if you'd like to optimize your game. Not required but recommended if you're comfortable doing so. https://comfig.app/app/" + "\n" + "Don't forget to read this in order to not override these settings if you do use mastercomfig. https://docs.comfig.app/latest/setup/install/#custom-configs")
input("Press enter to close...")