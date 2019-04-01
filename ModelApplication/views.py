# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def createJob(request):


    if request.method == "POST":
        return render(request, 'JobSchd/jobfinal_form.html', allValues)

    return render(request, 'JobSchd/jobfinal_form.html', allValues)




