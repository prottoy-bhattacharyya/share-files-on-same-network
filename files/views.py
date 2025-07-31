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