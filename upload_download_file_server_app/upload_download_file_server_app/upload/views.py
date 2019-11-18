# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime

def home(request):
    return render(request, 'home.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=settings.MEDIA_URL_UPLOAD)
        filename = fs.save(myfile.name, myfile)
        print(myfile.name)
        return render(request, 'upload_file.html')
    return render(request, 'upload_file.html')

def simple_download(request):
    list_of_files_url = {}
    directory_to_be_download = settings.MEDIA_ROOT
    os.chdir(settings.MEDIA_ROOT)
    list_of_files = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime, reverse=True)
    fs = FileSystemStorage()
    for temp in list_of_files:
        file_location = os.path.join(settings.MEDIA_ROOT, temp)
        file_location_creation_date = os.path.getmtime(file_location)
        created_time = datetime.fromtimestamp(file_location_creation_date).strftime('%Y-%m-%d %H:%M:%S')
        list_of_files_url[fs.url(temp)] = created_time
    return render(request, 'download_file.html', {'list_of_files': list_of_files_url})

