'''
Author: Mantresh Khurana | Spyxpo
Project Name: Spyxpo Web To App Builder
Project Description: This is a tool which is used to convert a website into an app for iOS, Android, Windows, macOS and Linux.
'''

from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import filedialog
import shutil
import os
import platform

running_on = platform.system()

if running_on == 'Darwin':
    print("Running on macOS")
elif running_on == 'Linux':
    print("Running on Linux")
elif running_on == 'Windows':
    print("Running on Windows")
else:
    print("Platform can't be detected.")            

def clear():
    if running_on == 'Darwin':
        os.system('clear')
    elif running_on == 'Linux':
        os.system('clear')
    elif running_on == 'Windows':
        os.system('cls')
    else:
        pass

clear()

if os.path.exists("assets"):
    pass
else:
    os.mkdir("assets")

if os.path.exists("assets/favicon.png"):
    os.remove("assets/favicon.png")
else:
    pass

if os.path.exists("assets/key.properties"):
    os.remove("assets/key.properties")
else:
    pass

def openBuildfolder():
    if running_on == 'Darwin':
        os.system('open build')
    elif running_on == 'Linux':
        os.system('open build')
    elif running_on == 'Windows':
        os.system('start build')
    else:
        pass

def uploadIconAction(event=None):
    app_name_info = app_name.get()

    if app_name_info == "":
        showinfo("No app name", "No app name, please enter an app name.")
        return False
    else:
        pass

    app_name_info = app_name.get()
    icon = filedialog.askopenfilename(filetypes=[("png files", "*.png")])
    print('Icon image:', icon)
    
    if icon == '':
        pass
    else:
        shutil.copy(str(icon), 'assets/favicon.png')

def uploadKeystoreAction(event=None):
    app_name_info = app_name.get()

    if app_name_info == "":
        showinfo("No app name", "No app name, please enter an app name.")
        return False
    else:
        pass

    app_name_info = app_name.get()
    store_pass_info = store_pass.get()
    key_pass_info = key_pass.get()
    alias_info = alias.get()
    keystore_path = filedialog.askopenfilename(filetypes=[("keystore files", "*.jks")])
    print('Keystore file:', keystore_path)

    key_file = open('assets/key.properties', 'w')
    key_file.write(f'storePassword={store_pass_info}\nkeyPassword={key_pass_info}\nkeyAlias={alias_info}\nstoreFile={keystore_path}')
    key_file.close()

def saveData():

    app_name_info = app_name.get()
    app_description_info = app_description.get()
    app_package_info = app_package_name.get().lower()
    app_version_info = app_version.get()
    app_build_info = app_build_number.get()
    app_web_url = web_url.get().lower()
    key_alias_info = alias.get()
    key_pass_info = key_pass.get()
    store_pass_info = store_pass.get()

    if os.path.exists("projects"):
        pass
    else:
        os.mkdir("projects")

    if os.path.exists(f"build/{app_name_info}_{app_version_info}.apk"):
        os.remove(f"build/{app_name_info}_{app_version_info}.apk")
    else:
        pass

    if os.path.exists(f"build/{app_name_info}_{app_version_info}.aab"):
        os.remove(f"build/{app_name_info}_{app_version_info}.aab")
    else:
        pass

    if app_name_info == "":
        showinfo("No app name", "No app name, please enter an app name.")
        return False
    else:
        pass

    if app_build_info.isnumeric():
        pass
    else:
        showinfo("Build Number", "Build Number must be a number.")
        return False

    if os.path.exists("assets/favicon.png"):
        pass
    else:
        showinfo("No icon selected", "No icon selected, please select an icon for your app.")
        return False
    
    if os.path.exists("assets/key.properties"):
        pass
    else:
        showinfo("No keystore selected", "No keystore selected, please select a keystore for your app.")
        return False    

    if app_description_info == "":
        showinfo("No description", "No description, please enter a description.")
        return False
    elif app_package_info == "":
        showinfo("No package name",
                 "No package name, please enter a package name.")
        return False
    elif app_version_info == "":
        showinfo("No version", "No version, please enter a version.")
        return False
    elif app_build_info == "":
        showinfo("No build number",
                 "No build number, please enter a build number.")
        return False
    elif app_web_url == "":
        showinfo("No web url", "No web url, please enter a web url.")
        return False
    elif os.path.exists(f"projects/{app_name_info}"):
        showinfo("App already exists",
                 "App already exists, please try another name for your app.")
        return False 
    elif key_alias_info == "":
        showinfo("Keystore Alias",
                 "Keystore alias is required.")
        return False
    elif key_pass_info == "":
        showinfo("Keystore Key Password",
                 "Keystore key password is required.")
        return False
    elif store_pass_info == "":
        showinfo("Keystore Password",
                 "Keystore password is required.")
        return False       
    else:
        shutil.copytree("template", f"projects/{app_name_info}")
        

    shutil.copy('assets/favicon.png',
                    f'projects/{app_name_info}/assets/images/favicon.png')    

    shutil.copy('assets/key.properties',
                    f'projects/{app_name_info}/android/key.properties')                        
                
    # add app name in main.dart
    with open(f'projects/{app_name_info}/lib/main.dart')as main_file:
        name = main_file.read().replace("APP_NAME", str(app_name_info), 1)

    with open(f'projects/{app_name_info}/lib/main.dart', "w") as new_main_file:
        new_main_file.write(name)

    # add ios package name in main.dart
    with open(f'projects/{app_name_info}/lib/main.dart')as main_file_ios_package_name:
        ios_package_name = main_file_ios_package_name.read().replace("PACKAGE_NAME", str(app_package_info), 1)

    with open(f'projects/{app_name_info}/lib/main.dart', "w") as new_main_file_ios_package_name:
        new_main_file_ios_package_name.write(ios_package_name)

    # add android package name in main.dart
    with open(f'projects/{app_name_info}/lib/main.dart')as main_file_android_package_name:
        android_package_name = main_file_android_package_name.read().replace("PACKAGE_NAME", str(app_package_info), 1)

    with open(f'projects/{app_name_info}/lib/main.dart', "w") as new_main_file_android_package_name:
        new_main_file_android_package_name.write(android_package_name)

    # add app website url in main.dart
    with open(f'projects/{app_name_info}/lib/main.dart')as home_file:
        website_name = home_file.read().replace("WEBSITE", str(app_web_url), 1)

    with open(f'projects/{app_name_info}/lib/main.dart', "w") as new_home_file:
        new_home_file.write(website_name)

    # add project name in pubspec.yaml
    with open(f'projects/{app_name_info}/pubspec.yaml')as pubspec_file:
        new_app_name_info = app_name_info.replace(" ", "")
        new_name = pubspec_file.read().replace("APP_NAME", str(new_app_name_info), 1)

    with open(f'projects/{app_name_info}/pubspec.yaml', "w") as new_pubspec_file:
        new_pubspec_file.write(new_name)

    # add app description in pubspec.yaml
    with open(f'projects/{app_name_info}/pubspec.yaml')as pubspec_file_description:
        description = pubspec_file_description.read().replace(
            "DESCRIPTION", str(app_description_info), 1)

    with open(f'projects/{app_name_info}/pubspec.yaml', "w") as new_pubspec_file_description:
        new_pubspec_file_description.write(description)

    # add app name in pubspec.yaml
    with open(f'projects/{app_name_info}/pubspec.yaml') as pubspec_file_name:
        new_app_name = pubspec_file_name.read().replace(
            "APP_NAME", f"{app_name_info}", 1)

    with open(f'projects/{app_name_info}/pubspec.yaml', "w") as new_pubspec_file_name:
        new_pubspec_file_name.write(new_app_name)

    pubspec_file = open(f"projects/{app_name_info}/pubspec.yaml", "r")
    list_of_lines = pubspec_file.readlines()
    list_of_lines[5] = f"version: {app_version_info}+{app_build_info}" + "\n"

    pubspec_file = open(f"projects/{app_name_info}/pubspec.yaml", "w")
    pubspec_file.writelines(list_of_lines)
    pubspec_file.close()

    readme_file = open(f"projects/{app_name_info}/README.md", "w")
    readme_file.write(
        f"{app_name_info}\n{app_package_info}\n{app_version_info}\n{app_build_info}")
    readme_file.close()

    os.chdir(f"projects/{app_name_info}/")

    os.system("flutter clean")  # clean the project

    os.system("flutter pub get")  # install plugins
    os.system("flutter pub run flutter_app_name")  # change app name

    os.system("flutter pub get")  # install plugins
    os.system(
        f"flutter pub run change_app_package_name:main {app_package_info}")  # change app package name

    os.system("flutter pub get")  # install plugins
    os.system("flutter pub run flutter_launcher_icons:main")  # change app icon

    os.system("flutter build apk --release")
    os.system("flutter build appbundle --release")

    os.chdir(os.path.dirname(os.getcwd()))
    os.chdir(os.path.dirname(os.getcwd()))
    
    if os.path.exists("build"):
        pass
    else:
        os.mkdir("build")

    if os.path.exists(f"build/{app_name_info}"):
        print('Build already exists.')
        pass
    else:
        os.mkdir(f"build/{app_name_info}")

    original_build_location_apk = (r'projects/' + app_name_info +
                               r'/build/app/outputs/apk/release/app-release.apk')  # original location of your apk
    target_build_location_apk = (r'build/' + app_name_info +
                             r'/' + app_name_info + r'_' + app_version_info + r'.apk')  # new location for apk

    original_build_location_aab = (r'projects/' + app_name_info +
                               r'/build/app/outputs/bundle/release/app-release.aab')  # original location of your aab
    target_build_location_aab = (r'build/' + app_name_info +
                             r'/' + app_name_info + r'_' + app_version_info + r'.aab')  # new location for aab                         

    # copy original app to new location
    shutil.copyfile(original_build_location_apk, target_build_location_apk)

    shutil.copyfile(original_build_location_aab, target_build_location_aab)

    # remove existing project files, updating existing projects coming soon
    shutil.rmtree(f"projects/{app_name_info}/")

    if os.path.exists("assets/favicon.png"):
        os.remove("assets/favicon.png")
    else:
        pass

    if os.path.exists("assets/key.properties"):
        os.remove("assets/key.properties")
    else:
        pass

    clear()

    print(
        f"Your apk is located in \"/build/{app_name_info}/{app_name_info}_{app_version_info}.apk\"\n")
    print(
        f"Your appBundle is located in \"/build/{app_name_info}/{app_name_info}_{app_version_info}.aab\"\n")

    openBuildfolder()

# version details
version_info = open('version.info', 'r')
version = version_info.read()

# tkinter ui
root = tk.Tk()
icon = PhotoImage(file = 'images/logo.png')
root.iconphoto(False, icon)
root.title('Spyxpo Web To App Builder | ' + version)
root.geometry('500x755')
root.resizable(0, 0)

app_name_label = Label(root, text="App Name")
app_name_label.pack()
app_name = StringVar()
app_name_info = app_name.get()
Entry(root, textvariable=app_name, width=35).pack()

description_label = Label(root, text="Description (Keep it short)")
description_label.pack()
app_description = StringVar()
Entry(root, textvariable=app_description, width=35).pack()

package_name_label = Label(
    root, text="Package Name (e.g. com.companyname.appname)")
package_name_label.pack()
app_package_name = StringVar()
Entry(root, textvariable=app_package_name, width=35).pack()

version_label = Label(root, text="Version (e.g. 1.0.0)")
version_label.pack()
app_version = StringVar()
Entry(root, textvariable=app_version, width=35).pack()

build_number_label = Label(root, text="Build Number (e.g. 1)")
build_number_label.pack()
app_build_number = StringVar()
Entry(root, textvariable=app_build_number, width=35).pack()

web_url_label = Label(root, text="Website URL (www.website.com)")
web_url_label.pack()
web_url = StringVar()
Entry(root, textvariable=web_url, width=35).pack()

icon_label = Label(root, text="Icon (Choose .png image only)")
icon_label.pack()
Button(tk.Button(root, text='Choose an Icon', command=uploadIconAction).pack())

if running_on == 'Darwin':
    device_label = Label(root, text="Running on macOS", fg='yellow')
    device_label.pack()
    device_label = Label(root, text="Check target device for apps you can create.", fg='green')
    device_label.pack()
    
elif running_on == 'Windows':
    device_label = Label(root, text="Running on Windows", fg='yellow')
    device_label.pack()
    device_label = Label(root, text="Check target device for apps you can create.", fg='green')
    device_label.pack()

elif running_on == 'Linux':
    device_label = Label(root, text="Running on Linux", fg='yellow')
    device_label.pack()
    device_label = Label(root, text="Check target device for apps you can create.", fg='green')
    device_label.pack()
    
else:
    pass

# this feature is under development
# def display_selected(choice):
#     choice = variable.get()
#     print('Target Device: ' + choice)
#     if choice == 'Android':
#         print('Android build')
#         variable.trace('w', lambda *args: build_button.pack_forget())
#     elif choice == 'iOS':
#         print('iOS build')
#     elif choice == 'macOS':
#         print('macOS build')
#     elif choice == 'Windows':
#         print('Windows build')
#     elif choice == 'Linux':
#         print('Linux build')
#     else:
#         print('Unknown choice: ' + choice)
#         pass

# if running_on == 'Darwin':
#     device_label = Label(root, text="Target Device")
#     device_label.pack()
#     options = ['Android']
#     variable = StringVar(root)
#     variable.set(options[0])
#     device_dropdown = OptionMenu(root, variable, *options, command=display_selected)
#     device_dropdown.pack()
    
# elif running_on == 'Windows':
#     device_label = Label(root, text="Target Device")
#     device_label.pack()
#     options = ['Android']
#     variable = StringVar(root)
#     variable.set(options[0])
#     device_dropdown = OptionMenu(root, variable, *options, command=display_selected)
#     device_dropdown.pack() 

# elif running_on == 'Linux':
#     device_label = Label(root, text="Target Device")
#     device_label.pack()
#     options = ['Android']
#     variable = StringVar(root)
#     variable.set(options[0])
#     device_dropdown = OptionMenu(root, variable, *options, command=display_selected)
#     device_dropdown.pack() 

# else:
#     pass

keystore_label = Label(root, text="Keystore (Choose .jks file only)")
keystore_label.pack()
Button(tk.Button(root, text='Choose a Keystore', command=uploadKeystoreAction).pack())

keystore_label = Label(root, text="-Keystore file information-")
keystore_label.pack()

alias_label = Label(root, text="Key Alias")
alias_label.pack()
alias = StringVar()
Entry(root, textvariable=alias, width=35).pack()

store_pass_label = Label(root, text="Store Password")
store_pass_label.pack()
store_pass = StringVar()
Entry(root, textvariable=store_pass, width=35, show="\u2022").pack()

key_pass_label = Label(root, text="Key Password")
key_pass_label.pack()
key_pass = StringVar()
Entry(root, textvariable=key_pass, width=35, show="\u2022").pack()

blank_label = Label(root, text="\nVerify the details before building")
blank_label.pack()

building_apk_aab = Label(root, text="Building \'.apk\' and '.aab',\n\'appBundle\' is Play Store ready.", fg="green")
building_apk_aab.pack()

open_button = Button(root, text='Open Build Folder', command=lambda: openBuildfolder())
open_button.pack()

build_button = Button(root, text='Build', command=lambda: saveData())
build_button.pack()

root.mainloop()