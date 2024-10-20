from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from .models import user,info
from django.db import DatabaseError
from .helper import calc

    
@csrf_exempt
def index2(request):
    from lava.datas.chatbot import predict_class ,get_response,intents
    if request.method=="POST":
        try:
            msg=request.POST.get('title')
            ints = predict_class(msg)
            res = get_response(ints,intents)
            return JsonResponse ({"success":res})
        except:
            return JsonResponse({"error":"sorry unable to connect to the server"})
    else:
        return render(request,'lel.html')
        
def index(request):
    return render(request,'index.html')

def sign(request):
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['password']
        name=request.POST['name']
        if email=="" or pas=="" or name=="":
            return HttpResponse("All fields are mandatory")
        elif user.objects.filter(email=email):
            return HttpResponse("email already associated to a account")
        else:
            use=user.objects.create(email=email,name=name,password=pas)
            try:
                use.save()
                return HttpResponse("Account Created Succesfully")
            except:
                return HttpResponse("unable to create user right now!")
    else:
        return render(request,'SignUp.html')
    
def log(request):
    if request.method=="POST":
        email=request.POST['ema']
        pas=request.POST['pas']
        use = user.objects.filter(email=email,password=pas)
        if use:
            if user.objects.filter(email=email,info=True):
                request.session['email2']=email
                return render(request,'main1.html')
            else:
                name=user.objects.get(email=email).name
                request.session['email2']=email
                return render(request,'Main.html',{'name':name,'email':email})
        else:
            return HttpResponse("Invalid Credentials")
    else:
        return render(request,'Login.html')

def infoo(request):
    if request.method=="POST":
        email=request.session['email2']
        name=user.objects.get(email=email).name
        date=request.POST['date']
        lan=request.POST['language']
        place=request.POST['birth_place']
        state=request.POST['state']
        city=request.POST['city']
        gen=request.POST['gender']
        mob=request.POST['mobile']
        edu=request.POST['education']
        pa=request.POST.getlist('pan')
        PAN,LIC,PASS,VOT=calc(pa)
        try:
            str1=info.objects.create(email=email,name=name,DOB=date,state=state,city=city,gender=gen,mobile=mob,Education=edu,language=lan,b_place=place,pan=PAN,d_license=LIC,passport=PASS,voter=VOT)
        except DatabaseError as e:
            return JsonResponse({'error':'data already updated'})
        if str1:
            user.objects.filter(email=email).update(info=True)
            return JsonResponse({'success':"your details updated successfully",'pan':PAN,'lic':LIC,'pas':PASS,'vot':VOT})
        else:
            return JsonResponse({'error':"Sorry unable to update your info please try later"})
    return JsonResponse({'error':'unauthorized'})

@csrf_exempt
def process(request):
    if request.method=="POST":
        try:
            email=request.session['email2']
            str1= user.objects.filter(email=email,info=True)
            if str1:
                PAN=info.objects.get(email=email).pan
                VOT=info.objects.get(email=email).voter
                LIC=info.objects.get(email=email).d_license
                PASS=info.objects.get(email=email).passport
                return JsonResponse({'success':'Success','vot':VOT,'pan':PAN,'lic':LIC,'pas':PASS})
        except:
            return JsonResponse({'error':"update your details to get guidance"})
    else:
        return render(request,'main1.html')
