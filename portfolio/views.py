from django.shortcuts import render



def HomePage(request):
    return render(request,"Main.html")
def Resume(request):
    return render(request,"resume.html")
def Projects(request):
    return render(request,"Projects.html")