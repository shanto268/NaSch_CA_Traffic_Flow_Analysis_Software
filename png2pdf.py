# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:14:07 2019

@author: Owner
"""
from fpdf import FPDF
import glob

def png2pdf(nm):
    drt = "/Users/sshanto/techmrt/Python_new/draft_2/experiment_1/figures/" + nm + "/"
    ext = "experiment_1_combined_plots_" + drt.split("/")[6] + ".pdf"    
    #print(ext)

    l = glob.glob(drt+"*.png")
    print(drt+"*.png\n")
    
    pdf = FPDF()
    
    imagelist= l
    x = 0
    y = -5
    w = 220
    h = 180
    
    for image in imagelist:
        print(image)
        pdf.add_page()
        pdf.image(image,x,y,w,h)
    drt =  str(nm)+ "/"
    pdf.output(drt+ext, "F")
    #print(drt+ext)
    #print("Done!\n")


f = glob.glob("/Users/sshanto/techmrt/Python_new/draft_2/experiment_1/figures/*")

for i in f:
    t = i.split("\\")[0]
   # print(t)
    png2pdf(t)

g = glob.glob("draft_2/experiment_2/figures/*") 
#print(g)

def exp_2_png2pdf(nm):
    drt = "draft_2/experiment_2/figures/" + nm + "/"
    ext = "experiment_2_combined_plots_" + drt.split("/")[3] + ".pdf"    
    print(ext)
    
    l = glob.glob(drt+"*.png")
    
    
    pdf = FPDF()
    
    imagelist= l
    x = 0
    y = -5
    w = 220
    h = 180
    
    for image in imagelist:
       # print(image)
        pdf.add_page()
        pdf.image(image,x,y,w,h)
    drt = "draft_2/experiment_2/figures/" + str(nm)+ "/"
    pdf.output(drt+ext, "F")
    print("Done!\n")
    
"""
for i in g:
   t = i.split("\\")[1]
   exp_2_png2pdf(t)
"""







