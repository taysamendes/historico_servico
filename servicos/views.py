# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Servico
from django.utils import timezone
from django.shortcuts import render

# Create your views here.
def servicos(request):
    servico=Servico.objects.filter(dataServico__lte=timezone.now()).order_by('dataServico')
    return render(request,'servicos/servicos.html',{'servicos':servico})

