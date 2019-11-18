# Django - webapps - Download and upload server
# Deploying the djangon download-upload web app using virtualenv
- [Introduction](#Introduction)
- [Pre-requisites](#pre-requisites)
- [Installation and configuration](#Installation-and-configuration)

# Introduction
we will install the download-upload web app using virutalenv and start the django in gunicorn using the python 

# Pre-requisites
Before we get started using the script. 
* Ensure you have installed python.
* virtualenv need to be installed.

# Installation and configuration
Clone the project locally to your linux machine.

1. Use the below command to create the virutal environment with python and in background it will install gunicorn and django 
```
./django_app.py --install 
```

2. Below command helps to stop and stop the gunicorn
```
./django_app.py --start/stop 
```

Once you have started the app, you can access the page in http://localhost:8800

Everything is simple configure please feel free to change in the python script

Django download-upload web application is used as remote upload and download server and it will be accessible inside the network.