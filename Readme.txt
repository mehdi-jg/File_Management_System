This software will be used to manage all hard files in JGTDSL. 
There will be a guide line for the user to use this software.


Guideline for installing weasyprint (needed for PDF generation feature)

------>

Installing WeasyPrint on Windows requires to follow a few steps that may not be easy. Please read this chapter carefully.

Only Windows 10 64-bit is supported. You can find this information in the Control Panel → System and Security → System.

The first step is to install the latest version of Python from the Microsoft Store.

link: https://www.microsoft.com/en-us/search?q=python



When Python is installed, you have to install GTK. Download the latest GTK3 installer and launch it. If you don’t know what some options mean, you can safely keep the default options selected.

link: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

You can then install WeasyPrint in a virtual environment using pip:

python3 -m venv venv
. venv\scripts\activate
python3 -m pip install weasyprint
python3 -m weasyprint --info
