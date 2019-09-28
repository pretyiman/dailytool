from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from blog.models import Income, Expenses, Contacts, list,catagory,subcatagory,warehouse,rack,item
from blog.forms import Incomeform, Expensesform, ContactForm,listform,RackForm,WarehouseForm,CatagoryForm,SubcatagoryForm,ItemForm
from django.db.models import Sum
import datetime
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView,FormView
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
################ rack #########################

@method_decorator(login_required, name='dispatch')
class rackcreateview(CreateView):
    form_class = RackForm
    template_name = 'blog/rack_form.html'
    success_url = '/racklist/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class racklistview(ListView):
    model= rack
    template_name = 'blog/rack_list.html'

    def get_queryset(self):
        return rack.objects.all()

@method_decorator(login_required, name='dispatch')
class rackdetailview(DetailView):
    model = rack
    template_name = 'blog/rack_detail.html'

@method_decorator(login_required, name='dispatch')
class rackupdateview(UpdateView):
    form_class =RackForm
    template_name = 'blog/rack_form.html'
    success_message = 'Success: Student Profile  was updated.'
    success_url = reverse_lazy('rack-list')

    def get_queryset(self):
        return rack.objects.order_by('Name')

@method_decorator(login_required, name='dispatch')
class rackdeleteview(DeleteView):
    model = rack
    success_url = reverse_lazy('rack-list')


################## item #########################
@method_decorator(login_required, name='dispatch')
class itemcreateview(CreateView):
    form_class = ItemForm
    template_name = 'blog/item_form.html'
    success_url = '/itemlist/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        print(form)

@method_decorator(login_required, name='dispatch')
class itemlistview(ListView):
    model= item
    template_name = 'myapp/item_list.html'

    def get_queryset(self):
        return item.objects.all()

@method_decorator(login_required, name='dispatch')
class itemdetailview(DetailView):
    model = item
    template_name = 'blog/item_detail.html'

@method_decorator(login_required, name='dispatch')
class itemupdateview(UpdateView):
    form_class = ItemForm
    template_name = 'blog/item_form.html'
    success_message = 'Success: Student Profile  was updated.'
    success_url = reverse_lazy('item-list')

    def get_queryset(self):
        return item.objects.order_by('Name')

@method_decorator(login_required, name='dispatch')
class itemdeleteview(DeleteView):
    model = item
    success_url = reverse_lazy('item-list')

####################### sub-catagory #################
@method_decorator(login_required, name='dispatch')
class SubCatagoryFormview(CreateView):
    form_class = SubcatagoryForm
    template_name = 'blog/sub_form.html'
    success_url = '/subcatagorylist'
    success_message = "Catagory created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class SubCatagoryListView(ListView):
    model= subcatagory
    template_name = 'blog/sub_list.html'

    def get_queryset(self):
        return subcatagory.objects.order_by('Name')

@method_decorator(login_required, name='dispatch')
class SubCatagoryUpdateView(UpdateView):
    form_class = SubcatagoryForm
    template_name = 'blog/sub_form.html'
    success_message = 'Success: Student Profile  was updated.'
    success_url = reverse_lazy('subcatagory-list')

    def get_queryset(self):
        return subcatagory.objects.order_by('Name')

@method_decorator(login_required, name='dispatch')
class SubCatagoryDeleteView(DeleteView):
    model = subcatagory
    success_url = reverse_lazy('subcatagory-list')


################## catagory ########################
@method_decorator(login_required, name='dispatch')
class CatagoryFormview(CreateView):
    form_class = CatagoryForm
    template_name = 'blog/catagory_form.html'
    success_url = '/catagorylist'
    success_message = "Catagory created successfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CatagoryListView(ListView):
    model= catagory
    template_name = 'blog/catagory_list.html'

    def get_queryset(self):
        return catagory.objects.order_by('Name')

@method_decorator(login_required, name='dispatch')
class CatagoryUpdateView(UpdateView):
    form_class = CatagoryForm
    template_name = 'blog/catagory_form.html'
    success_message = 'Success: Student Profile  was updated.'
    success_url = reverse_lazy('catagory-list')

    def get_queryset(self):
        return catagory.objects.order_by('Name')

@method_decorator(login_required, name='dispatch')
class CatagoryDeleteView(DeleteView):
    model = catagory
    success_url = reverse_lazy('catagory-list')


################ warehouse #########################
@method_decorator(login_required, name='dispatch')
class warehousecreateview(CreateView):
    form_class = WarehouseForm
    template_name = 'blog/warehouse_form.html'
    success_url = '/warehouselist/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class warehouselistview(ListView):
    model= warehouse
    template_name = 'blog/warehouse_list.html'

    def get_queryset(self):
        return warehouse.objects.all()

@method_decorator(login_required, name='dispatch')
class warehousedetailview(DetailView):
    model = warehouse
    template_name = 'blog/warehouse_detail.html'

@method_decorator(login_required, name='dispatch')
class warehouseupdateview(UpdateView):
    form_class = WarehouseForm
    template_name = 'blog/warehouse_form.html'
    success_message = 'Success: Student Profile  was updated.'
    success_url = reverse_lazy('warehouse-list')

    def get_queryset(self):
        return warehouse.objects.order_by('Name')

@method_decorator(login_required, name='dispatch')
class warehousedeleteview(DeleteView):
    model = warehouse
    success_url = reverse_lazy('warehouse-list')




########## expences related fuctions ##########
def error_404_view(request, exception):
    return render(request,'blog/page404.html')


@login_required(login_url='/login/')
def Expensesforminput (request):
    if request.method =="POST":
        form = Expensesform (request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,('Record has been updated'))
                return redirect("/todayexpensesreport")
            except:
                pass
    else:
        form = Expensesform()
        return render (request, "blog/Expences_entry.html", {'form':form})

@login_required(login_url='/login/')
def DailyExpReport(request):
    today_date = datetime.date.today()
    total = 0
    myexpenses = Expenses.objects.filter(reg_date = datetime.date.today())
    total = Income.objects.filter(reg_date = datetime.date.today()).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date = datetime.date.today()).aggregate( Sum('expenses_value'))
    incometotal = total.get("income_value__sum")
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/expenses_report.html', { 'formurl':"expnesesreport", 'Expenses':myexpenses, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})

@login_required(login_url='/login/')
def yesterdayExp(request):
    today = datetime.date.today()
    tdalta =datetime.timedelta(days = 1)
    yesterday = today - tdalta
    total = 0
    myexpenses = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today)
    total = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('expenses_value'))
    incometotal = total.get('income_value__sum')
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/expenses_report.html', {'formurl':"expnesesreport", 'Expenses':myexpenses, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})

@login_required(login_url='/login/')
def LSD_expenses(request):
    today = datetime.date.today()
    tdalta =datetime.timedelta(days=7)
    yesterday = today - tdalta
    total = 0
    myexpenses = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today)
    total = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('expenses_value'))
    incometotal = total.get('income_value__sum')
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/expenses_report.html', {'formurl':"expnesesreport", 'Expenses':myexpenses, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})

@login_required(login_url='/login/')
def LTD_expenses(request):
    today = datetime.date.today()
    tdalta =datetime.timedelta(days=29)
    yesterday = today - tdalta
    total = 0
    myexpenses = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today)
    total = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('expenses_value'))
    incometotal = total.get('income_value__sum')
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/expenses_report.html', {'formurl':"expnesesreport", 'Expenses':myexpenses, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})

@login_required(login_url='/login/')
def CDR_expenses(request):
    if request.method == 'GET':
        return render(request, 'blog/expenses_report.html')

    elif request.method == 'POST':
          start_date = request.POST.get("htmldate","")
          end_date = request.POST.get("htmldate1","")
          total = 0
          myexpenses = Expenses.objects.filter(reg_date__gte = start_date, reg_date__lte=end_date)
          if myexpenses is not None:
              total = Income.objects.filter(reg_date__gte = start_date, reg_date__lte=end_date).aggregate( Sum('income_value'))
              totalexp = Expenses.objects.filter(reg_date__gte = start_date, reg_date__lte=end_date).aggregate( Sum('expenses_value'))
              incometotal = total.get('income_value__sum')
              exp_total = totalexp.get('expenses_value__sum')
              if exp_total is None:
                  exp_total = 0
              if incometotal is None:
                  incometotal = 0
              netcash = incometotal - exp_total
          return render(request, 'blog/expenses_report.html', {'formurl':"expnesesreport", 'Expenses':myexpenses, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})
    else:
        return render(request, 'blog/expenses_report')


@login_required(login_url='/login/')
def exp_total():
    total = Expenses.objects.aggregate(Sum('expenses_value'))
    return render (request, "blog/expenses_report.html",{'total':myexpenses})

@login_required(login_url='/login/')
def expedit(request,exp_id):
    myexpenses = Expenses.objects.get(exp_id=exp_id)
    return render (request, "blog/edit.html",{'myexpenses':myexpenses})

@login_required(login_url='/login/')
def expupdate(request, exp_id):
    myexpenses = Expenses.objects.get(exp_id= exp_id)
    form = Expensesform(request.POST, instance = myexpenses)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('/todayexpensesreport')
    return render(request, "blog/edit.html", {'Expenses':myexpenses})

@login_required(login_url='/login/')
def expdelete(request, exp_id):
    myexpenses = Expenses.objects.get(exp_id=exp_id)
    myexpenses.delete()
    return redirect('/todayexpensesreport')

##################### income related fucntions ################
@login_required(login_url='/login/')
def incomeforminput (request):
    if request.method =="POST":
        form = Incomeform (request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, ('Record has been updated'))
                return redirect("/todaysincomereport")
            except:
                pass
    else:
        form = Incomeform()
        return render (request, "blog/income_entry.html", {'form':form})

@login_required(login_url='/login/')
def DailyincomeReport(request):
    today_date = datetime.date.today()
    total = 0
    myincome = Income.objects.filter(reg_date = datetime.date.today())
    total = Income.objects.filter(reg_date = datetime.date.today()).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date = datetime.date.today()).aggregate( Sum('expenses_value'))
    incometotal = total.get('income_value__sum')
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/income_report.html', {'Income':myincome, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash, 'formurl' : "/incomerepoting"})

@login_required(login_url='/login/')
def yesterdayincomeReport(request):
    today = datetime.date.today()
    tdalta =datetime.timedelta(days = 1)
    yesterday = today - tdalta
    total = 0
    myincome = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today)
    total = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('expenses_value'))
    incometotal = total.get('income_value__sum')
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/income_report.html', {'Income':myincome, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash, 'formurl' : "/incomerepoting" })

@login_required(login_url='/login/')
def LSDincomeReport(request):
    today = datetime.date.today()
    tdalta =datetime.timedelta(days=7)
    yesterday = today - tdalta
    total = 0
    myincome = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today)
    total = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('expenses_value'))
    incometotal = total.get('income_value__sum')
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/income_report.html', {'formurl' : "/incomerepoting", 'Income':myincome, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})

@login_required(login_url='/login/')
def LTDincomeReport(request):
    today = datetime.date.today()
    tdalta =datetime.timedelta(days=29)
    yesterday = today - tdalta
    total = 0
    myincome = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today)
    total = Income.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('income_value'))
    totalexp = Expenses.objects.filter(reg_date__gte = yesterday, reg_date__lte=today).aggregate( Sum('expenses_value'))
    incometotal = total.get('income_value__sum')
    exp_total = totalexp.get('expenses_value__sum')
    if exp_total is None:
        exp_total = 0
    if incometotal is None:
        incometotal = 0
    netcash = incometotal - exp_total
    return render(request, 'blog/income_report.html', {'formurl' : "/incomerepoting", 'Income':myincome, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})

@login_required(login_url='/login/')
def CDR_income(request):
    if request.method == 'GET':
        return render(request, 'blog/income_report.html')

    elif request.method == 'POST':

      start_date = request.POST.get("htmldate","")
      end_date = request.POST.get("htmldate1","")
      total = 0
      myincome = Income.objects.filter(reg_date__gte = start_date, reg_date__lte=end_date)
      total = Income.objects.filter(reg_date__gte = start_date, reg_date__lte=end_date).aggregate( Sum('income_value'))
      totalexp = Expenses.objects.filter(reg_date__gte = start_date, reg_date__lte=end_date).aggregate( Sum('expenses_value'))
      incometotal = total.get('income_value__sum')
      exp_total = totalexp.get('expenses_value__sum')
      if exp_total is None:
          exp_total = 0
      if incometotal is None:
          incometotal = 0
      netcash = incometotal - exp_total
      print(netcash)
      return render(request, 'blog/income_report.html', {'formurl' : "/incomerepoting",  'Income':myincome, 'total': total, 'totalexp' : totalexp, 'netcash' : netcash})

    else:
        return render(request, 'blog/customdatereport')

@login_required(login_url='/login/')
def income_total():
    total = Income.objects.aggregate(Sum('income_value'))
    return render (request, "blog/income_report.html",{'total':myincome})

@login_required(login_url='/login/')
def incomeedit(request,income_id):
    myincome = Income.objects.get(income_id=income_id)
    return render (request, "blog/income_edit.html",{'myincome':myincome})

@login_required(login_url='/login/')
def incomeeditform(request,income_id):
    form = Incomeform(request.GET)
    myincome = Income.objects.get(income_id=income_id)
    return render (request, "blog/income_edit.html",{'myincome':myincome})

@login_required(login_url='/login/')
def incomeupdate(request, income_id):
    myincome = Income.objects.get(income_id= income_id)
    form = Incomeform(request.POST, instance = myincome)
    if form.is_valid():
        form.save()
        return redirect('/todaysincomereport')
    return render(request, "blog/income_edit.html", {'myincome':myincome})

@login_required(login_url='/login/')
def incomedelete(request, income_id):
    myeincome = Income.objects.get(income_id=income_id)
    myeincome.delete()
    return redirect('/todaysincomereport')


##### contacts related functions #######

@login_required(login_url='/login/')
def ContacFormEntry(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Mobile = form.cleaned_data['Mobile']
            Address = form.cleaned_data['Address']
            form.save()
            return redirect("/contactlist")
    else:
        form=ContactForm()
        return render (request, "blog/Contact_form.html", {'form':form})

@login_required(login_url='/login/')
def contactlist(request):
    total = 0
    total= Contacts.objects.count()
    contaclist= Contacts.objects.all().order_by('Name')
    return render (request, "blog/Contact_list.html",{'Contacts':contaclist, 'total': total})

@login_required(login_url='/login/')
def editContact(request,contact_ID):
    mycontact = Contacts.objects.get(contact_ID=contact_ID)
    return render (request, "blog/edit_contact.html",{'mycontact':mycontact})

@login_required(login_url='/login/')
def contactupdate(request, contact_ID):
    mycontact = Contacts.objects.get(contact_ID = contact_ID)
    form = ContactForm(request.POST, instance = mycontact)
    if form.is_valid():
        form.save()
        return redirect('/contactlist')
    return render(request, "blog/edit_contact.html", {'mycontact':mycontact})

@login_required(login_url='/login/')
def deletecontact(request, contact_ID):
    mycontact = Contacts.objects.get(contact_ID=contact_ID)
    mycontact.delete()
    return redirect('/contactlist/')

@login_required(login_url='/login/')
def searchview(request):
    if request.method=='POST':
        try:
            srch = request.POST['srh']
        except MultiValueDictKeyError:
            srch = False
        if srch:
            match = Contacts.objects.filter(Q(Name__icontains=srch)|Q(Mobile__icontains=srch))

            if match:
                return render (request,'blog/search.html', {'sr':match})
            else:
                messages.error(request,"No result found")
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'blog/search.html')

##################### todo list ##################

@login_required(login_url='/login/')
def todo(request):
    if request.method=='POST':
        form=listform(request.POST or None) ##removed "or none"

        if form.is_valid():
            item = form.cleaned_data['item']
            form.save()
            all_item=list.objects.all()
            messages.success(request, ('Task has been added'))
            return render(request, 'blog/todolist.html',{'all_item':all_item})

    else:
        all_item = list.objects.all()
        return render(request, 'blog/todolist.html',{'all_item':all_item})

@login_required(login_url='/login/')
def deletetodo(request,list_id):
    item=list.objects.get(pk=list_id)
    item.delete()
    return redirect('/todo/')

@login_required(login_url='/login/')
def cross_off(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('/todo/')

@login_required(login_url='/login/')
def uncross(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('/todo/')



##########log in window######
@login_required(login_url='/login/')
def home_page(request):
    return render (request,'blog/index.html')

@login_required(login_url='/login/')
def welcome(request):
    return render (request,'blog/welcome.html')

@login_required(login_url='/login/')
def inventory(request):
    return render (request,'blog/inventory.html')

@login_required(login_url='/login/')
def dailyfinance(request):
    return render (request,'blog/innerbase.html')
