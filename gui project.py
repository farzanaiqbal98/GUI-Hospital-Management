## Background vector - www.freepik.com
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk


l1=list()

def setid():
    c=0
    try:
        handle=open("Patient.txt",'r')
        for line in handle:
            l1=line.split()
            if len(l1)>2:
                c+=1
        idno=c+1       
        rid="TK00"+str(idno)
    except:
        rid="TK001"
    return rid

def about():
    w3=Toplevel()
    w3.title("ABOUT-TAKE CARE HOSPITAL")
    w3.geometry('1000x1000')
    Label_1=Label(w3,text="ABOUT",font=("Times",25))
    Label_1.pack()
    Label2 = Label(w3,text="TAKE CARE Hospital was founded.........",font=("Times",14)) #ivda fill cheytho
    Label2.place(x=90,y=90)
    


def appointment():
    w2= Toplevel()
    w2.title("APOOINTMENTS-TAKE CARE HOSPITAL")
    w2.geometry('1000x1000')
    image = Image.open("3.jpg")
    image=image.resize((1000,1000))
    photo = ImageTk.PhotoImage(image)
    lb1=Label(w2,image=photo)
    lb1.pack()
    Label_1=Label(w2,text="BOOK AN APPOINTMENT",font=("Times",25),bg="white")
    Label_1.place(x=320,y=0)
    L1 = Label(w2, text="ARE YOU A REGISTERED PATIENT?",font=("Times",15))
    L1.place(x=340,y=80)
    
                
    def check():
        def found():
            def docfind():
                def timeslot():
                    def show():
                        def dstry():
                            w2.destroy()
                        text1=("Your appoinment with "+ dc1.get()+" is confirmed at "+dc2.get()+".")
                        L3 = Label(w2, text=text1,font=("Times",15))
                        L3.place(x=200,y=650)
                        b=Button(w2, text="Go back to Home Page",font=("Times",12),relief="solid",command=dstry)
                        b.place(x=430,y=690)
                        
                    L1 = Label(w2, text="Select time slot :",font=("Times",15))
                    L1.place(x=320,y=550)
                    if dc.get()==' ENT' or dc.get()==" Orthopaedic":
                        dc2 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                        dc2['value'] = ('9 AM-10 AM',  
                                     '12 PM-1 PM',
                                     '3 PM-4 PM'
                                     )
                        dc2.place(x=470,y=550)
                        b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=show)
                        b.place(x=470,y=600)
                    elif dc.get()==' General Medicine' or dc.get()==' Surgery':
                        dc2 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                        dc2['value'] = ('10 AM-11 AM',  
                                     '12 PM-1 PM',
                                     '3 PM-4 PM'
                                     )
                        dc2.place(x=470,y=550)
                        b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=show)
                        b.place(x=470,y=600)
                    elif dc.get()==' Gynaecology' or dc.get()==" Pediatrician":
                        dc2 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                        dc2['value'] = ('10 AM-11 AM',  
                                     '1 PM-2 PM',
                                     '3 PM-4 PM',
                                     '4 PM- 5 PM'
                                     )
                        dc2.place(x=470,y=550)
                        b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=show)
                        b.place(x=470,y=600)
                    
                if dc.get()==" ENT" :
                    L1 = Label(w2, text="Select Doctor :",font=("Times",15))
                    L1.place(x=320,y=458)
                    dc1 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                    dc1['value'] = ('Shreya P - MBBS,MD',  
                                     'Uday Krishna - MBBS,DLO', 
                                     )
                    dc1.place(x=470,y=460)
                    b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=timeslot)
                    b.place(x=470,y=510)

                elif dc.get()==" General Medicine":
                    L1 = Label(w2, text="Select Doctor :",font=("Times",15))
                    L1.place(x=320,y=458)
                    dc1 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                    dc1['value'] = ('Sharukh S - MBBS, MD','Athira madhusoodhanan - MBBS, MD','Sheetal S - MBBS, MD')
                    dc1.place(x=470,y=460)
                    b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=timeslot)
                    b.place(x=470,y=510)
                elif dc.get()==" Gynaecology":
                    L1 = Label(w2, text="Select Doctor :",font=("Times",15))
                    L1.place(x=320,y=458)
                    dc1 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                    dc1['value'] = (' Dr.Subadhra Kumari - MBBS,MD,OBG','Dr. Praveen Babu -MBBS, DGO')
                    dc1.place(x=470,y=460)
                    b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=timeslot)
                    b.place(x=470,y=510)
                elif dc.get()==" Pediatrician":
                    L1 = Label(w2, text="Select Doctor :",font=("Times",15))
                    L1.place(x=320,y=458)
                    dc1 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                    dc1['value'] = (' Shankar Raj- MBBS,MD','Babu P S - MBBS,MD')
                    dc1.place(x=470,y=460)
                    b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=timeslot)
                    b.place(x=470,y=510)
                elif dc.get()==" Orthopaedic":
                    L1 = Label(w2, text="Select Doctor :",font=("Times",15))
                    L1.place(x=320,y=458)
                    dc1 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                    dc1['value'] = ('  Sooryanarayanan Varma - MBBS  MS ortho','Alphonse P - MBBS MS ortho')
                    dc1.place(x=470,y=460)
                    b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=timeslot)
                    b.place(x=470,y=510)
                elif dc.get()==" Surgery":
                    L1 = Label(w2, text="Select Doctor :",font=("Times",15))
                    L1.place(x=320,y=458)
                    dc1 = ttk.Combobox(w2, width = 27,font=("Times",14)) 
                    dc1['value'] = ('  Praveen Shankar - MBBS MS','Meera Krishna -MBBS DNB surgery')
                    dc1.place(x=470,y=460)
                    b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=timeslot)
                    b.place(x=470,y=510)

            fl=1
            handle = open("Patient.txt",'r')
            for line in handle:
                l1=line.split()
                if len(l1)>6:
                    idf=l1[0]
                    name="Patient name: "+l1[1]+" "+l1[2]+"\nPatient age :"+l1[3]+"\nPatient Gender: "+l1[5]
                    if idf==E7.get():
                        L1 = Label(w2, text="Patient Found!",font=("Times",15))
                        messagebox.showinfo( "Patient Details",name,parent=w2)
                        L1.place(x=430,y=320)
                        fl=0
            if fl==1:
                messagebox.showwarning( "Appointment","Patient NOT Found! Kindly Register",parent=w2)
            if fl==0:
                n = StringVar()
                L1 = Label(w2, text="Select Department :",font=("Times",15))
                L1.place(x=320,y=360)
                dc = ttk.Combobox(w2, width = 27, textvariable = n,font=("Times",14)) 
                dc['values'] = (' ENT',  
                                ' General Medicine', 
                                ' Gynaecology', 
                                ' Orthopaedic', 
                                ' Pediatrician',
                                ' Surgery') 
                dc.place(x=490,y=360)
                b=Button(w2, text="Check for Doctors",font=("Times",12),relief="solid",command=docfind)
                b.place(x=450,y=410)
                        


        if var1.get()==1:
            print("HI")
            L2 = Label(w2, text="ENTER YOUR REGISTRATION ID",font=("Times",15))
            L2.place(x=380,y=190)
            E7 = Entry(w2, bd =5,width=40,relief="groove")
            E7.place(x=400,y=230)
            b=Button(w2, text="Enter",font=("Times",12),relief="solid",command=found)
            b.place(x=470,y=270)
        elif var2.get()==1:
            registration()
        
    var1 = IntVar()
    c1=Checkbutton(w2, text="Yes",font=("Times",15), variable=var1,command=check)
    var2 = IntVar()
    c2=Checkbutton(w2, text="No",font=("Times",15), variable=var2,command=check)
    c1.place(x=480,y=120)
    c2.place(x=480,y=150)
    w2.mainloop()
    
    

def registration():
    w1 = Toplevel()
    w1.title("REGISTRATION-TAKE CARE HOSPITAL")
    w1.geometry('1000x1000')
    image = Image.open("2.jpg")
    image=image.resize((990,1000))
    photo = ImageTk.PhotoImage(image)
    lb1=Label(w1,image=photo)
    lb1.pack()
    Label_1=Label(w1,text="NEW REGISTRATION",font=("Times",25),bg="white")
    Label_1.place(x=320,y=0)
    L1 = Label(w1, text="First Name",font=("Times",15))
    L1.place(x=270,y=80)
    gender="nil"
   
    def save1():
        handle = open("Patient.txt",'a')
        if var1.get()==1:
            gender="Male"
        elif var2.get()==1:
            gender="Female"
        rid=setid()
        L = ["\n",rid,"  ",E1.get(), " ", E2.get()," ",E3.get()," ",E4.get()," ",gender," ",T1.get("1.0","end")," ",E5.get()," ",E6.get(),"\n"]
        handle.writelines(L)
        Label(w1, text="Successfully Registered and Your REGISTRATION ID is",font=("Times",15),fg='red').place(x=280,y=500)
        Label(w1 ,text=rid,font=("Times",15),fg='red').place(x=740,y=500)
        Label(w1 ,text="Do you want to take an Appointment?",font=("Times",15)).place(x=410,y=540)
        def see():
            if var3.get()==1:
                appointment()
            elif var4.get()==1:
                w1.destroy()
        var3 = IntVar()
        c3=Checkbutton(w1, text="Yes",font=("Times",15), variable=var3,command=see)
        var4 = IntVar()
        c4=Checkbutton(w1, text="No",font=("Times",15), variable=var4,command=see)
        c3.place(x=490,y=570)
        c4.place(x=570,y=570)
        
    E1 = Entry(w1, bd =5,width=40,relief="groove")
    E1.place(x=530,y=80)
    L1 = Label(w1, text="Last Name",font=("Times",15))
    L1.place(x=270,y=110)
    E1.focus()
    E2 = Entry(w1, bd =5,width=40,relief="groove")
    E2.place(x=530,y=110)
    L1 = Label(w1, text="Age",font=("Times",15))
    L1.place(x=270,y=140)
    E3 = Entry(w1, bd =5,width=40,relief="groove")
    E3.place(x=530,y=140)
    L1 = Label(w1, text="Date of Birth in(dd/mm/yyyy)",font=("Times",15))
    L1.place(x=270,y=170)
    E4 = Entry(w1, bd =5,width=40,relief="groove")
    E4.place(x=530,y=170)
    L1 = Label(w1, text="Gender",font=("Times",15))
    L1.place(x=270,y=230)
    var1 = IntVar()
    c1=Checkbutton(w1, text="Male",font=("Times",15), variable=var1)
    var2 = IntVar()
    c2=Checkbutton(w1, text="Female",font=("Times",15), variable=var2)
    c1.place(x=530,y=230)
    c2.place(x=600,y=230)
    L1 = Label(w1, text="Address",font=("Times",15))
    L1.place(x=270,y=270)
    T1= Text(w1,bd=2,width=50,height=3,relief="groove")
    T1.place(x=530,y=270)
    L1 = Label(w1, text="Phone/Mobile No.",font=("Times",15))
    L1.place(x=270,y=330)
    E5 = Entry(w1, bd =5,width=40,relief="groove")
    E5.place(x=530,y=330)
    L1 = Label(w1, text="Blood Group",font=("Times",15))
    L1.place(x=270,y=380)
    E6 = Entry(w1, bd =5,width=40,relief="groove")
    E6.place(x=530,y=380)
    Button(w1, text='Register and Save',font=("Times",15),relief="raised",command=save1).place(x=450,y=450)
    w1.mainloop()
    
window=Tk()
window.title("TAKE CARE HOSPITAL")
window.geometry('2000x2000')
image = Image.open("3568984.jpg")
image = image.resize((2000,1000))
photo = ImageTk.PhotoImage(image)
lb1=Label(window,image=photo)
lb1.pack()
frame = Frame(window, relief='raised', borderwidth=2)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
Label(frame,text="Welcome to TAKE CARE HOSPITAL\nStay safe!\nStay home!",bg="white",font=("Times",30)).pack()
btn=Button(window, text="NEW REGISTRATION",bg="white",font=("Times",10),width=20,height=2,command=registration)
btn.place(x=500, y=560)
btn=Button(window, text="APPOINTMENT",bg="white",font=("Times",10),width=20,height=2,command=appointment)
btn.place(x=700, y=560)
btn=Button(window, text="ABOUT", bg="white",font=("Times",10),width=20,height=2,command=about)
btn.place(x=880, y=560)
window.mainloop()
