from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import income ,expense
from . forms import IncomeForms , ExpenseForms
from django.views.generic import TemplateView
def index(request):
    formOne=IncomeForms()
    formTwo=ExpenseForms()
    if request.method=='POST' and 'btn1'in request.POST:
       formOne=IncomeForms(request.POST)
       if formOne.is_valid():
        formOne.save()
        return redirect ('index')
    if request.method=='POST' and 'btn2'in request.POST:
       formTwo=ExpenseForms(request.POST)
       if formTwo.is_valid():
          formTwo.save()
          return redirect ('index')
    a={'formOne':formOne,'formTwo':formTwo}
    return render(request, 'index.html',a)
def dashbord(request):
    labels = []
    data = []
    queryset = income.objects.all()
    for amt in queryset:
        labels.append(amt.iteam)
        data.append(amt.amount)
    queryset1 = expense.objects.all()
    for amt1 in queryset1:
       labels.append(amt1.iteam)
       data.append(amt1.amount)
    # return render (request, 'dashbord.html',{'dict':dict})
#     return render (request, 'dashbord.html',{
#         'labels': labels,
#         'data': data,
#     },{
#         'labels1': labels1,
#         'data1':data1
#     }
# })

   




    






# def handlemultipleforms(request, template="handle/multiple_forms.html"):
#     """
#     Handle Multiple <form></form> elements
#     """
#     if request.method == 'POST':
#         if request.POST.get("form_type") == 'formOne':
#             #Handle Elements from first Form
#         elif request.POST.get("form_type") == 'formTwo':
#             #Handle Elements from second Form