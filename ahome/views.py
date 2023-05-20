from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ahome.models import Abase, Adetail, Pjmanage, Ibju
from django.utils import timezone
from django.db.models import Q


# @login_required(login_url='common:login')
def apply_base(request):
    kw = request.GET.get('kw', '')
    abase = Abase.objects.order_by('-모집공고일')
    if kw:
        abase = abase.filter(
            Q(지역__icontains=kw) |
            Q(건설사__icontains=kw)
        ).distinct()
    context = {'abase': abase, 'kw': kw}
    return render(request, 'ahome/apply_base.html', context)


def apply_detail(request, abase_id):
    abase = Abase.objects.get(id=abase_id)
    details = abase.adetail_set.all()
    context = {
        'abase': abase,
        'details': details
    }
    return render(request, 'ahome/apply_detail.html', context)

def pj_list(request):
    lists = Pjmanage.objects.all()
    context = { 'pjlist' : lists }
    return render(request, 'ahome/pj_manage.html', context)

def ibju_data(request):
    kw = request.GET.get('kw', '')
    ibju_list = Ibju.objects.order_by('입주시기')
    if kw:
        ibju_list = ibju_list.filter(
            Q(구분__icontains=kw) |
            Q(시도__icontains=kw) |
            Q(자치구__icontains=kw) |
            Q(시공사__icontains=kw)
        ).distinct()
    context = { 'ibju_list' : ibju_list, 'kw': kw }

    return render(request, 'ahome/ibju_list.html', context)