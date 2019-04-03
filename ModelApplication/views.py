# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import subprocess
from itreat.settings import BASE_DIR

def createJob(request):


    if request.method == "POST":
        return render(request,"JobSchd/jobfinal_form.html",{})

    command = "Rscript " + BASE_DIR + "/../Model_Application/0_Main.r "
    args = []
    args.append("Project Folder")
    args.append("/home/siddharth/MARG/Model_Application/")
    args.append("Halton File")
    args.append("/home/siddharth/MARG/Halton_R/haltbrat_vfc101.csv")
    args.append("Input Data")
    args.append("/home/siddharth/MARG/Model_Application/az_hhld_vfc_cleaned_final.csv")
    args.append("Output Data")
    args.append("/home/siddharth/MARG/Model_Application/VFC_output.csv")
    args.append("Seed")
    args.append("1")
    args.append("const|DRVRCNT|NUMADLT|RUR|INCOME1|INCOME5|NUMCHILD|WORK0|WORK2|HSIZE4|SF_Own|Retired|Prop_HH_INC5|Prop_SFHH|AUTO10_Q1")
    args.append("13.03|2.01|0.374|0.867|-1.05|1.325|0.517|-1.513|0.829|-0.669|0.570|-0.878|1.362|0.687|-0.293")
    args.append("const|INCOME1|INCOME2|OWN|HSIZE1|WORK0|POPDEN")
    args.append("1.73|2.37|0.82|-1.65|2.12|1.21|0.00011")
    args.append("const|INCOME1|INCOME2|HSIZE1|Prop_MFHH|WORK2")
    args.append("4.27|1.43|0.96|2.22|0.4|-0.86")
    args.append("const|lif_cyc_1|INCOME3|WORK2|INC1")
    args.append("5.31|0.42|-0.21|-0.34|-0.00034")
    args.append("const|OWN|NUMADLT|WORK3|POPDEN|child_pres|lif_cyc_2")
    args.append("1.69|1.0|0.48|1.02|-0.000088|0.38|0.5")
    args.append("const|INCOME5|lif_cyc_2|HSIZE4|WORK2")
    args.append("1.18|0.72|1.63|1.51|-0.7")
    args.append("const")
    args.append("0.0")
    args.append("0 Vehicles|1 Vehicle Type|2 Vehicle Types|3 Vehicle Types|4 Vehicle Types|5+ Vehicle Types")
    args.append("5|6|7|25|1|4")
    args.append("uno|INCOME1|INCOME4|NUMCHILD|WORK3|Prop_HH_INC5|RATE_AUTO10")
    args.append("-4.542|-0.4|0.164|-0.189|0.173|-1.013|-13.833")
    args.append("uno|WORK2|INCOME2")
    args.append("-5.057|-0.157|0.132")
    args.append("uno|INCOME1|Retired|Prop_HH_INC1")
    args.append("-5.846|0.574|0.202|0.574")
    args.append("uno|NUMCHILD|WORK2|TAZ_den_Q1|RATE_AUTO30")
    args.append("-7.479|0.379|-0.388|-0.307|-1.717")
    args.append("uno|NUMCHILD|TAZ_den_Q1|INCOME2")
    args.append("-7.579|0.331|-0.258|0.269")
    args.append("uno|HHSIZE|TAZ_den_Q1|INCOME1")
    args.append("-8.897|0.138|0.676|0.659")
    args.append("uno|INCOME1|WORK2|Retired|Prop_HH_INC1|RATE_AUTO10|TAZ_den_Q3")
    args.append("-5.815|-1.014|0.169|-0.167|-1.475|-17.83|0.267")
    args.append("uno|INCOME3|HSIZE4|SF_Own|AUTO30_Q1")
    args.append("-7.371|0.257|0.333|0.86|-0.301")
    args.append("uno|INCOME4|child_pres|SF|TAZ_den_Q2")
    args.append("-7.030|0.36|0.313|-0.736|-0.361")
    args.append("uno|INCOME5|HSIZE1|RUR|Prop_SFHH")
    args.append("-7.616|0.244|-0.978|0.239|0.74")
    args.append("uno|RUR|Retired|INCOME4|AUTO10_Q1")
    args.append("-6.583|0.153|-0.353|0.164|-0.229")
    args.append("uno|Prop_HH_INC1|INCOME2|child_pres|AUTO10_Q1")
    args.append("-7.177|1.283|0.345|-0.25|-0.335")
    args.append("uno|RUR|SF_Own|HSIZE1")
    args.append("-8.190|0.705|0.752|-0.567")
    args.append("uno|INCOME1|INCOME2|INCOME3")
    args.append("8.072|0.3|-0.35|-0.15")
    args.append("uno|INCOME1")
    args.append("7.732|0.35")
    args.append("uno|INCOME1")
    args.append("7.806|0.2")
    args.append("uno|INCOME1|INCOME2")
    args.append("10.889|1.55|-0.5")
    args.append("uno|INCOME2|INCOME3")
    args.append("9.810|0.5|1.5")
    args.append("uno|INCOME1|INCOME2|INCOME3")
    args.append("10.949|-0.2|-1.0|3.0")
    args.append("uno|INCOME1|INCOME2")
    args.append("9.233|0.35|-0.65")
    args.append("uno")
    args.append("9.024")
    args.append("uno")
    args.append("9.156")
    args.append("uno")
    args.append("10.134")
    args.append("uno")
    args.append("9.001")
    args.append("uno")
    args.append("9.164")
    args.append("uno|INCOME1|INCOME2|INCOME3")
    args.append("7.507|1.0|-1.0|0.5")
    args.append("Tolerance")
    args.append("0.035")
    args.append("Maximum Iteration")
    args.append("5")
    args.append("const|INCOME1|INCOME2|OWN|HSIZE1|WORK0|POPDEN")
    args.append("0.68|2.093|0.608|-1.430|2.109|1.145|0.00011")
    args.append("const|INCOME1|INCOME2|HSIZE1|Prop_MFHH|child_pres")
    args.append("3.672|1.015|0.646|1.995|0.260|-0.333")
    args.append("const|RUR|INCOME4|INCOME5|HSIZE4|OWN")
    args.append("2.956|0.190|0.353|0.230|0.303|0.983")
    args.append("const|OWN|NUMADLT|WORK3|POPDEN|child_pres")
    args.append("0.0|1.418|0.548|0.460|-0.0001|0.364")
    args.append("const")
    args.append("0.0")
    args.append("const|YCAR0_5|YCAR6_11|INCOME2|INCOME5|WORK3|NUMADLT|HSIZE1|HSIZE4|OWN|MU (Threshold)")
    args.append("-4.494|0.955|1.054|-0.105|0.193|0.409|0.473|-0.417|-0.258|0.285|1.450")
    args.append("const|YVAN6_11|YVAN12|INCOME2|vanmile|TAZ_den_Q3|AUTO10_Q1|EMPDEN")
    args.append("-4.620|1.952|2.572|-0.593|0.00006|0.597|0.867|-0.00023")
    args.append("const|YSUV0_5|YSUV12|NUMADLT|INCOME2|INCOME5|suvmile|WORK3|RATE_TRANSIT30")
    args.append("-3.640|0.905|1.496|0.455|-0.535|0.398|0.00004|-0.459|-34.163")
    args.append("const|YPICK0_5|YPICK6_11|pickmile|INCOME5|WORK3|OWN|empden_per_100|TAZ_den_Q3|AUTO30_Q1")
    args.append("-3.946|0.869|1.016|0.000058|-0.287|0.460|0.808|0.0078|0.299|0.268")
    
    args = list(map(lambda x: "\"" + x + "\"",args))
    
    
    final_args = " ".join(args)
    command += " " + final_args + " " 

    print command
    process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
    process.wait()
    for line in process.stdout:
            print line
    print process.returncode
    return render(request,"ModelApplication/base.html",{})




