from django.shortcuts import render,redirect
from django.http import HttpResponse
from todoapp.models import Product

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello from request</h1>")
    return redirect('/index')


def contact(request):
    return render(request,'contact.html')
    
def products(request):
    return render(request,'products.html')
def blog(request):
    return render(request,'createblog.html')
def store(request):
    h=request.POST['bhead']
    c=request.POST['bcat']
    d=request.POST['bdes']
    data=h+c+d
    return HttpResponse(data)

def home(request):
    con={}
    con['data1']=69696969
    con['data2']='This is a secret message'
    con['data3']={12:'This is really a secret message'}
    con['seq']=[33,'surya',6.7,[66,77]]
    con['x']=6
    con['y']=50
    return render(request,'index.html',con)




    ''' once i have a view logic ready i need to register this to the project url
 return statment should return a response object not a python str
'''
#Product management views
def dash_product(request):
    if request.method == "POST":
        #Retrieve the data into python variables and store in database
        pname=request.POST['pname']
        pdesc=request.POST['pdesc']
        price=request.POST['price']
        cat=request.POST['category']
        '''print("NAME :",pname)
        print("DESCRIPTION :",pdesc)
        print("PRICE :",price)
        print("CATEGORY :",cat)'''
        p=Product(pname=pname,pdesc=pdesc,price=price,cat=cat,is_deleted='N')
        p.save()
        return redirect('/pdashboard')
    else:
        print("Get section")
        #data=Product.objects.all() #ALL products
        data=Product.objects.filter(is_deleted='N')
        contents={}
        contents['data']=data
        return render(request,'product-dashboard.html',contents)

def edit(request,rid):
    if request.method=='POST':
        upname=request.POST['pname']
        updesc=request.POST['pdesc']
        uprice=request.POST['price']
        ucat=request.POST['category']
        x=Product.objects.filter(id=rid)
        x.update(pname=upname,pdesc=updesc,price=uprice,cat=ucat)
        return redirect('/pdashboard')
    else:
        data=Product.objects.get(id=rid)
        content={}
        content['data']=data
        return render(request,'edit.html',content)



def delete(request,rid):
    '''prod=Product.objects.get(id=rid)
    prod.delete()'''
    x=Product.objects.filter(id=rid)
    x.update(is_deleted='Y')
    return redirect('/pdashboard')