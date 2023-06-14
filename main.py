import PySimpleGUI as sg
import urllib.request
import os

# Dropdown menu options with download links
options = [
    "++Fortnite+Release-4.1-CL-4053532-Windows",
    "++Fortnite+Release-7.40-CL-5046157-Windows",
    "++Fortnite+Release-8.40-CL-6005771-Windows",
    "++Fortnite+Release-8.51-CL-6058028-Windows",
    "++Fortnite+Release-9.00-CL-6337466-Windows",
    "++Fortnite+Release-9.10-CL-6639283-Windows",
    "++Fortnite+Release-9.41-CL-7609292-Windows",
    "++Fortnite+Release-10.00-CL-7658179-Windows",
    "++Fortnite+Release-10.40-CL-9380822-Windows",
    "++Fortnite+Release-11.31-CL-10800459-Windows",
    "++Fortnite+Release-12.00-CL-11586896-Windows",
    "++Fortnite+Release-12.21-CL-12236980-Windows",
    "++Fortnite+Release-12.41-CL-12905909-Windows",
    "++Fortnite+Release-12.50-CL-13193885-Windows",
    "++Fortnite+Release-12.61-CL-13498980-Windows",
    "++Fortnite+Release-14.40-CL-14550713-Windows",
    "++Fortnite+Release-14.60-CL-14786821-Windows",
    "++Fortnite+Release-15.30-CL-15341163-Windows",
    "++Fortnite+Release-16.40-CL-16218553-Windows",
    "++Fortnite+Release-17.30-CL-17004569-Windows"
]

# Download links corresponding to the options
download_links = [
    "https://cdn.fnbuilds.services/4.1.zip",
    "https://cdn.fnbuilds.services/7.40.rar",
    "https://cdn.fnbuilds.services/8.40.zip",
    "https://cdn.fnbuilds.services/8.51.rar",
    "https://cdn.fnbuilds.services/9.00.zip",
    "https://cdn.fnbuilds.services/9.10.rar",
    "https://cdn.fnbuilds.services/9.41.rar",
    "https://cdn.fnbuilds.services/10.00.zip",
    "https://cdn.fnbuilds.services/10.40.rar",
    "https://cdn.fnbuilds.services/11.31.rar",
    "https://cdn.fnbuilds.services/12.00.rar",
    "https://cdn.fnbuilds.services/12.21.zip",
    "https://cdn.fnbuilds.services/12.41.rar",
    "https://cdn.fnbuilds.services/12.50.zip",
    "https://cdn.fnbuilds.services/12.61.zip",
    "https://cdn.fnbuilds.services/14.40.rar",
    "https://cdn.fnbuilds.services/14.60.rar",
    "https://cdn.fnbuilds.services/15.30.rar",
    "https://cdn.fnbuilds.services/16.40.rar",
    "https://cdn.fnbuilds.services/17.30.zip"
]

# Function to download the selected file
def download_file():
    selected_option = values["-OPTIONS-"]
    if selected_option:
        index = options.index(selected_option)
        download_link = download_links[index]
        save_location = sg.popup_get_folder("Select a folder to save the file:")
        if save_location:
            file_name = download_link.split("/")[-1]
            save_path = os.path.join(save_location, file_name)
            urllib.request.urlretrieve(download_link, save_path)
            sg.popup("Download complete!", "File saved at: " + save_path)

# Create the layout
layout = [
    [sg.Text("Select a build to download:")],
    [sg.Combo(options, key="-OPTIONS-", size=(50, 1))],
    [sg.Button("Download")]
]

# Create the window
window = sg.Window("EasyInstaller", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Download":
        download_file()

# Close the window
window.close()
