from django.shortcuts import render
from jagdambaapp.forms import RegistrationForm
# Create your views here.

def home(request):
    return render(request,"tempapp/home.html")



 def reg(request):
    print("===============1==============")
    rf = RegistrationForm(request.POST)
    if request.method == "POST":
        print("===============3==============")
        if rf.is_valid():
            print("===============4==============")
            rf.save()
           # return redirect('user-otp')
        else:
            return render(request, 'tempapp/regsistration.html', {"form": rf})
    else:
        print("===============2==============")
        return render(request,'tempapp/regsistration.html',{"form":rf})
