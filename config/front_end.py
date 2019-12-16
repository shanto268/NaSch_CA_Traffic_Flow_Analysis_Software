#important libraries
from tkinter import *
import os
#import sys, simulation.road, simulation.speedLimits, simulation.car, representation, config.case, simulation.trafficGenerators

c1 = True
tot_sim_time = 1500
sim_time_update = 100
arr = [] #stores all info
cmd1 = "cd /Users/ttumuon/muonSC8/sas/Python_new/"
cmd = "ls "
cmd2 = "python nagel.py config.case"


#key down functions:
def click():
    nlanes = float(t1.get())
    ncars = float(t2.get())
    avpercent = float(t3.get())
    if c1 == False:
        nsim = float(t5.get())
        nsim_update = float(t6.get())
    else:
        nsim = tot_sim_time
        nsim_update = sim_time_update
   # arr.append(nlanes, ncars, avpercent, nsim, nsim_update)
    os.chdir(r"/Users/ttumuon/muonSC8/sas/Python_new/")
    os.system(cmd)
    os.system(cmd2)
   # l1 = Label(window, text=str(int(etext1)+int(etext2)),bg="grey", fg="black", font="none 12").grid(row=5,column=0,sticky=W)
                
def close():
    window.destroy()
    exit()

def Select_model(m):
    return m

def density(i):
    window.geometry("680x300")
    text_l = "Enter the total simulation run time: "
    text_r = "Enter the simulation run time after which the density will update: "
    if i == 1:
        c1 = False
        l5 = Label(window, text=text_l, bg="grey", fg="black", font="none 15").grid(row=6,column=0,sticky=W)
        t5 = Entry(window, width=5, bg="white", borderwidth=3)
        t5.grid(row=6, column=2,sticky=NE)
    elif i == 2:
        c1 = False
        l5 = Label(window, text=text_r, bg="grey", fg="black", font="none 15").grid(row=6,column=0,sticky=W)
        t6 = Entry(window, width=5, bg="white", borderwidth=3)
        t6.grid(row=6, column=2,sticky=NE)
        
def scroll_av(s):
  if s=="aware":
    one=Label(window,text="Type Aware",width=12, fg="red")
   # one.grid(column=1,row=4)
  if s=="unaware":
    two=Label(window,text="Type Unware",width=12, fg="blue")
   # two.grid(column=1,row=4)        
  if s=="hv":
    three=Label(window,text="HV Model",width=12, fg="green")
   # three.grid(column=1,row=4)  

#main functions
window = Tk()
window.title("Traffic Analysis Software")
window.configure(background="grey")


#Entering pictures
background_image = PhotoImage(file="/Users/ttumuon/muonSC8/sas/Python_new/paper_draft/draft/fd1.png")

 
#create label
l1 = Label(window, text="Enter the number of lanes: ", bg="grey", fg="black", font="none 15").grid(row=0,column=0,sticky=W)
t1 = Entry(window, width=5, bg="white", borderwidth=3)
t1.grid(row=0, column=2,sticky=NE, columnspan=4)

l2 = Label (window, text="Enter the total number of cars: ", bg="grey", fg="black", font="none 15").grid(row=1,column=0,sticky=W)
t2 = Entry(window, width=5, bg="white", borderwidth=3)
t2.grid(row=1, column=2,sticky=NE)

l3 = Label (window, text="Enter the percentage of AV: ", bg="grey", fg="black", font="none 15").grid(row=2,column=0,sticky=W)
t3 = Entry(window, width=5, bg="white", borderwidth=3)
t3.grid(row=2, column=2,sticky=NE)

l4 = Label (window, text="Select an AV model: ", bg="grey", fg="black", font="none 15").grid(row=3,column=0,sticky=W)
init_opt=StringVar(window)
init_opt.set("Select ...")
av1=OptionMenu(window,init_opt,"aware","unaware","hv",command=scroll_av)
av1.grid(column=2,row=3,sticky=NE)


l5 = Label (window, text="System Density: ", bg="grey", fg="black", font="none 15").grid(row=5,column=0,sticky=W)
o1 = Button(window, text="CONSTANT", width=10, command=lambda i = 1: density(i), fg="red").grid(row=5,column=1,sticky=NE)
o2 = Button(window, text="INCREASING", width=12, command=lambda i = 2: density(i), fg="blue").grid(row=5,column=2,sticky=NE)


Label(window, text="     ", bg="grey", fg="grey").grid(row=7,column=0, columnspan = 3)
Label(window, text="     ", bg="grey", fg="grey").grid(row=8,column=0, columnspan = 3)
Label(window, text="     ", bg="grey", fg="grey").grid(row=11,column=0, columnspan = 3)
Label(window, text="Made by Sadman Ahmed Shanto © 2019", bg="grey", fg="black").grid(row=12,column=0, columnspan = 3)


#buttons
b1 = Button(window, text="EXIT", width=6, command=close, fg="red").grid(row=10,column=0,sticky=NW)
b2 = Button(window, text="RUN", width=10, command=click, fg="green").grid(row=10,column=2,sticky=NE)

#picture insertion
#Label(window, image=var, bg = "grey").grid(row=9, column=2)
 
#run the main loop
window.mainloop()


