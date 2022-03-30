from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        StuName= request.POST['sName']
        StuMob = request.POST['sMob']
        StuEmail = request.POST['sEmail']
        branch = request.POST['course']
        Aviavle=Student.objects.all()

        
        if(StuName==""or StuMob==""or StuEmail=="" or branch=="" or branch=="Course"):
            pass
        else:
            if Aviavle.filter(stuMob=StuMob) or Aviavle.filter(stuEmail=StuEmail):
                # msg="Wrong deteil."
                # return render(request,"Index.html",{"msg":msg})
                pass
            else:
                print(StuName,StuMob,StuEmail,branch)
                register=Student(stuName=StuName,stuMob=StuMob,stuEmail=StuEmail,bran=branch)
                register.save()
            pass

    Bcastu=Student.objects.filter(bran="BCA").count()
    B_tech=Student.objects.filter(bran="B.tech").count()
    BSC=Student.objects.filter(bran="BSC").count()
    Poly=Student.objects.filter(bran="PolyTech").count()
    MBA=Student.objects.filter(bran="MBA").count()
    data=Student.objects.all()
    return render(request,"Index.html",{"data":data,"Bcastu":Bcastu,"B_tech":B_tech,"BSC":BSC,"Poly":Poly,"MBA":MBA})

def BcaStu(request):
    BcaTotal=Student.objects.filter(bran="BCA").count()
    data = Student.objects.filter(bran="BCA")
    return render(request,"BcaStu.html",{"BcaTotal":BcaTotal,"data":data})
