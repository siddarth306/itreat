# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import subprocess
from itreat.settings import BASE_DIR

def createJob(request):


    if request.method == "POST":
        return render(request, 'JobSchd/jobfinal_form.html', allValues)

    command = "Rscript " + BASE_DIR + "../ModelApplication/0_Main.r" 
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print process.returncode
    return render(request, 'homepage/home.html', {})




