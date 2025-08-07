from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            print(file)
        else:
            print("No file uploaded")
        
        with open("uploads/" + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    return render(request, 'files/home.html')
from django.shortcuts import render
from django.http import FileResponse, Http404
import os

upload_folder = "./uploads"
# Create your views here.
def home(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            print(file)
        else:
            print("No file uploaded")
        
        with open("uploads/" + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    
    items_list = os.listdir(upload_folder)
    items_dict = dict(enumerate(items_list))
    print(items_dict)
    return render(request, 'files/home.html', {'items_dict': items_dict})

def download(request, file_name):
    if file_name:
        file_path = upload_folder + "/" + file_name
        return FileResponse(open(file_path, "rb"), as_attachment = True)
    
    return Http404()
