from tkinter import *
from tkinter import messagebox
import random,os
from Dbconn import *

mydb = pymysql.connect(host="localhost",user="root",password="",database="BillingSys_Customer")
mycursor = mydb.cursor()

#THIS STATEMENT WILL CREATE FOLDER IF DOES NOT EXISTS

if  not os.path.exists('Sysbills'):
    os.mkdir('Sysbills')
class Bill_App:
        def __init__(self,root):
                self.root =root
                self.root.geometry("1290x705")
                self.root.title("Billing Software")
                bg_color = "#074463"
                self.title=Label(self.root,text="Software Billing System",font=("times new roman",20,"bold"),bg=bg_color,fg = 'white',bd=12,relief=GROOVE,pady=2).pack(fill=X)
        #------------------------------VARIABLES..............
        #------------------------------CUSTOMER DETAILS..............

                self.c_name = StringVar()
                self.c_phone = StringVar()
                self.bill_no = StringVar()
                r = random.randint(100,2000)
                self.bill_no.set(str(r))
                self.find_bill = StringVar()
        
        #------------------------------COSMETICS..............
                self.soap= IntVar()
                self.face = IntVar()
                self.facewash = IntVar()
                self.hairspray = IntVar()
                self.bodylotion = IntVar()
        #------------------------------GROCERY..............
                self.rice = IntVar()
                self.foodoil = IntVar()
                self.daal = IntVar()
                self.wheat = IntVar()
                self.sugar = IntVar()
        #------------------------------OTHERS..............
                self.maza = IntVar()
                self.coke = IntVar()
                self.frooti = IntVar()
                self.nimkos = IntVar()
                self.biscuits = IntVar()
        #------------------------------TOTAL PRODUCT PRICE & TAX...............
                self.cosmetic_price = StringVar()
                self.grocery_price = StringVar()
                self.others_price = StringVar()

                self.cosmetic_tax = StringVar()
                self.grocery_tax = StringVar()
                self.others_tax = StringVar()
        #------------------------------CUSTOMER FRAME..............
                customerlabframe = LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg='gold',bg=bg_color)
                customerlabframe.place(x=0,y=65,relwidth=1)

                customername = Label(customerlabframe,text="Customer Name",font=("times new roman",15,'bold'),fg='white',bg=bg_color)
                customername.grid(row=0,column=0,padx=16,pady=5 )
                nameEntry = Entry(customerlabframe,textvariable=self.c_name,font=('arial',15),bd=5,relief=SUNKEN,width=20)
                nameEntry.grid(row=0,column=1,padx=16,pady=5)

        #------------------------------Customer Phone Number............
                customerphone = Label(customerlabframe,text="Phone No.",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                customerphone.grid(row=0,column=2,padx=16,pady=5)
                phoneEntry = Entry(customerlabframe,textvariable=self.c_phone,font=('arial',15),bd=5,width=20)
                phoneEntry.grid(row=0,column=3,padx=16,pady=5)

        #------------------------------Bill No............
                customerbill = Label(customerlabframe,text="Bill No.",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                customerbill.grid(row=0,column=4,padx=16,pady=5)
                billEntry = Entry(customerlabframe,textvariable=self.find_bill,font=('arial',15),bd=5,width=15)
                billEntry.grid(row=0,column=5,padx=16,pady=5)

                customerenter = Button(customerlabframe,text="Enter",font=('arial',12,'bold'),bd=5,width=8,command=self.bill_search)
                customerenter.grid(row=0,column=6,padx=16,pady=10)
        #-------------------------------PRODUCT FRAME------------------
        #------------------------------COSMETIC FRAME............       
                cosmeticslabframe = LabelFrame(self.root,text="Cosmetics",font=("times new roman",15,"bold"),fg='gold',bg=bg_color,bd=5,relief=GROOVE)
                cosmeticslabframe.place(x=10,y=160,width=290,height=350) 

                bathsoap = Label(cosmeticslabframe,text="Bath Soap",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                bathsoap.grid(row=0,column=0,padx=15,sticky='w')
                bathEntry = Entry(cosmeticslabframe,textvariable=self.soap,font=('arial',15),width=8,bd=5)
                bathEntry.grid(row=0,column=1,padx=20,pady=15)
                

                facecream= Label(cosmeticslabframe,text="Face Cream",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                facecream.grid(row=1,column=0,padx=15,sticky='w')
                faceEntry = Entry(cosmeticslabframe,textvariable=self.face,font=('arial',15),width=8,bd=5)
                faceEntry.grid(row=1,column=1,padx=20,pady=15)
                

                facewash = Label(cosmeticslabframe,text="Face Wash",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                facewash.grid(row=2,column=0,padx=15,sticky='w')
                facewashEntry = Entry(cosmeticslabframe,textvariable=self.facewash,font=('arial',15),width=8,bd=5)
                facewashEntry.grid(row=2,column=1,padx=20,pady=15)
                

                hairspray = Label(cosmeticslabframe,text="Hair Spray",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                hairspray.grid(row=3,column=0,padx=15,sticky='w')
                hairsprayEntry = Entry(cosmeticslabframe,textvariable=self.hairspray,font=('arial',15),width=8,bd=5)
                hairsprayEntry.grid(row=3,column=1,padx=20,pady=15)
                

                bodylotion = Label(cosmeticslabframe,text="Body Lotion",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                bodylotion.grid(row=4,column=0,padx=15,sticky='w')
                lotionEntry = Entry(cosmeticslabframe,textvariable=self.bodylotion,font=('arial',15),width=8,bd=5)
                lotionEntry.grid(row=4,column=1,padx=20,pady=15)
                
        #------------------------------GROCERY FRAME............
                grocerylabframe = LabelFrame(self.root,text="Grocery",font=("times new roman",15,"bold"),bd=5,relief=GROOVE,bg=bg_color,fg='gold')
                grocerylabframe.place(x=310,y=160,width=290,height=350)
                
                
                rice = Label(grocerylabframe,text="Rice",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                rice.grid(row=0,column=0,padx=20,sticky='w')
                riceEntry = Entry(grocerylabframe,textvariable=self.rice,font=('arial',15),width=8,bd=5)
                riceEntry.grid(row=0,column=1,padx=20,pady=15)
                

                foodoil = Label(grocerylabframe,text="Food Oil",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                foodoil.grid(row=1,column=0,padx=20,sticky='w')
                foodoilEntry = Entry(grocerylabframe,textvariable=self.foodoil,font=('arial',15),width=8,bd=5)
                foodoilEntry.grid(row=1,column=1,padx=20,pady=15)
                

                daal = Label(grocerylabframe,text="Daal",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                daal.grid(row=2,column=0,padx=20,sticky='w')
                daalEntry = Entry(grocerylabframe,textvariable=self.daal,font=('arial',15),width=8,bd=5)
                daalEntry.grid(row=2,column=1,padx=20,pady=15)
                

                wheat = Label(grocerylabframe,text="Wheat",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                wheat.grid(row=3,column=0,padx=20,sticky='w')
                wheatEntry = Entry(grocerylabframe,textvariable=self.wheat,font=('arial',15),width=8,bd=5)
                wheatEntry.grid(row=3,column=1,padx=20,pady=15)
                

                sugar = Label(grocerylabframe,text="Sugar",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                sugar.grid(row=4,column=0,padx=20,sticky='w')
                sugarEntry = Entry(grocerylabframe,textvariable=self.sugar,font=('arial',15),width=8,bd=5)
                sugarEntry.grid(row=4,column=1,padx=20,pady=15)
                
        #------------------------------OTHERS............

                otherslabframe = LabelFrame(self.root,text="Others",font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg='gold',bg=bg_color)
                otherslabframe.place(x=610,y=160,width=290,height=350)

                maza = Label(otherslabframe,text="Maza",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                maza.grid(row=0,column=0,padx=25,sticky='w')
                mazaEntry = Entry(otherslabframe,textvariable=self.maza,font=('arial',15),width=8,bd=5)
                mazaEntry.grid(row=0,column=1,padx=20,pady=15)
                

                coke = Label(otherslabframe,text="Coke",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                coke.grid(row=1,column=0,padx=25,sticky='w')
                cokeEntry = Entry(otherslabframe,textvariable=self.coke,font=('arial',15),width=8,bd=5)
                cokeEntry.grid(row=1,column=1,padx=20,pady=15)
                

                frooti = Label(otherslabframe,text="Frooti",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                frooti.grid(row=2,column=0,padx=25,sticky='w')
                frootiEntry = Entry(otherslabframe,textvariable=self.frooti,font=('arial',15),width=8,bd=5)
                frootiEntry.grid(row=2,column=1,padx=20,pady=15)
                

                nimkos = Label(otherslabframe,text="Nimkos",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                nimkos.grid(row=3,column=0,padx=25,sticky='w')
                nimkosEntry = Entry(otherslabframe,textvariable=self.nimkos,font=('arial',15),width=8,bd=5)
                nimkosEntry.grid(row=3,column=1,padx=20,pady=15)
                

                biscuits = Label(otherslabframe,text="Biscuits",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                biscuits.grid(row=4,column=0,padx=25,sticky='w')
                biscuitsEntry = Entry(otherslabframe,textvariable=self.biscuits,font=('arial',15),width=8,bd=5)
                biscuitsEntry.grid(row=4,column=1,padx=20,pady=15)
                

        #------------------------------Bill AREA FRAME............
                Billareaframe = Frame(self.root,bd=10,relief=GROOVE)
                Billareaframe.place(x=925,y=160,width=370,height=350)

                billlab = Label(Billareaframe,text="Bill Area",font=("arial",15,'bold'),bd=5,relief=GROOVE)
                billlab.pack(fill=X)

                scrolling = Scrollbar(Billareaframe,orient=VERTICAL)
                self.txtarea=Text(Billareaframe,yscrollcommand=scrolling.set)
                scrolling.pack(side=RIGHT,fill=Y)
                scrolling.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)
        #------------------------------TOTAL ENTRY & TAX............

                Billmenuframe = LabelFrame(root,text="Bill Menu",font=("times new roman",15,'bold'),bg=bg_color,fg='gold',bd=5,relief=GROOVE)
                Billmenuframe.place(x=5,y=515,relwidth=1,height=190)

                totalcosmetics = Label(Billmenuframe,text="Total Cosmetics",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                totalcosmetics.grid(row=0,column=0,padx=20,pady=10,sticky='w')

                totalcosmeticsEntry = Entry(Billmenuframe,textvariable=self.cosmetic_price,font=('arial',15),width=8,bd=5)
                totalcosmeticsEntry.grid(row=0,column=1,padx=20,pady=10)

                totalgrocery = Label(Billmenuframe,text="Total Grocery",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                totalgrocery.grid(row=1,column=0,padx=20,pady=10,sticky='w')

                totalgroceryEntry = Entry(Billmenuframe,font=('arial',15),textvariable=self.grocery_price,width=8,bd=5)
                totalgroceryEntry.grid(row=1,column=1,padx=20,pady=10)


                totalothers = Label(Billmenuframe,text="Others Total",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                totalothers.grid(row=2,column=0,padx=20,pady=10,sticky='w')

                totalothersEntry = Entry(Billmenuframe,font=('arial',15),textvariable=self.others_price,width=8,bd=5)
                totalothersEntry.grid(row=2,column=1,padx=20,pady=10)
                
                
                cosmeticstax = Label(Billmenuframe,text="Cosmetics Tax",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                cosmeticstax.grid(row=0,column=2,padx=20,pady=10,sticky='w')

                cosmeticstaxEntry = Entry(Billmenuframe,font=('arial',15),textvariable=self.cosmetic_tax,width=8,bd=5)
                cosmeticstaxEntry.grid(row=0,column=3,padx=20,pady=10)

                grocerytax = Label(Billmenuframe,text="Grocery Tax",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                grocerytax.grid(row=1,column=2,padx=20,pady=10,sticky='w')

                grocerytaxEntry = Entry(Billmenuframe,font=('arial',15),textvariable=self.grocery_tax,width=8,bd=5)
                grocerytaxEntry.grid(row=1,column=3,padx=20,pady=10)


                otherstax = Label(Billmenuframe,text="Others Tax",font=("times new roman",15,'bold'),bg=bg_color,fg='white')
                otherstax.grid(row=2,column=2,padx=20,pady=10,sticky='w')

                otherstaxEntry = Entry(Billmenuframe,font=('arial',15),textvariable=self.others_tax,width=8,bd=5)
                otherstaxEntry.grid(row=2,column=3,padx=20,pady=10)
        #------------------------------BUTTONS............        

                buttonframe = Frame(Billmenuframe,bd=5,relief=RIDGE)
                buttonframe.place(x=650,y=25,width=650,height=110)

                totalbutton = Button(buttonframe,text="Total",font=('arial',12,'bold'),bd=8,width=10,bg=bg_color,fg='white',pady=10,command=self.total)
                totalbutton.grid(row=0,column=0,padx=20,pady=20)

                Billgenerate = Button(buttonframe,text="Generate Bill",font=('arial',12,'bold'),bd=8,width=10,bg=bg_color,fg='white',pady=10,command=self.Billgenerate_fun)
                Billgenerate.grid(row=0,column=1,padx=20,pady=20)

                Billclear = Button(buttonframe,text="Clear",font=('arial',12,'bold'),bd=8,width=10,bg=bg_color,fg='white',pady=10,command=self.Clear)
                Billclear.grid(row=0,column=3,padx=20,pady=20)

                def exit():
                        #this function will close the app if user have selected exit using destroy method
                        exityn=messagebox.askyesno('Sure?',"Do you want to exit??")
                        if exityn:
                                root.destroy()

                Billexit = Button(buttonframe,text="Exit",font=('arial',12,'bold'),bd=8,width=10,bg=bg_color,fg='white',pady=10,command=exit)
                Billexit.grid(row=0,column=4,padx=15,pady=20)
                self.Generate_bill()
#-----------------------------------------FUNCTIONS------------------------------------------------------------------------------                

#TOTAL FUNCTION TO GET TOTAL OF ENTERD VALUE OF ITEMS
        def total(self):
                self.soapprice = self.soap.get()*25
                self.faceprice =  self.face.get()*40
                self.facewashprice = self.facewash.get()*50
                self.hairsprayprice = self.hairspray.get()*80
                self.bodylotionprice = self.bodylotion.get()*75
                self.cosmetic_total =( 
                                        self.soapprice + 
                                        self.faceprice +
                                        self.facewashprice +
                                        self.hairsprayprice +
                                        self.bodylotionprice 
                                        )
                self.cosmetic_price.set("Rs."+str(self.cosmetic_total))
                self.c_tax=round((self.cosmetic_total*0.12),2)
                self.cosmetic_tax.set("Rs."+str(self.c_tax))

                self.riceprice = self.rice.get()*100
                self.foodoilprice = self.foodoil.get()*150
                self.daalprice = self.daal.get()*50
                self.wheatprice = self.wheat.get()*250
                self.sugarprice = self.sugar.get()*80
                self.grocery_total = (
                        
                        
                                        self.riceprice +
                                        self.foodoilprice +
                                        self.daalprice +
                                        self.wheatprice +
                                        self.sugarprice 
                                         
                

                                        )
                self.grocery_price.set("Rs."+str(self.grocery_total))
                self.g_tax = round((self.grocery_total*0.05),2)
                self.grocery_tax.set("Rs."+str(self.g_tax))

                self.mazaprice = self.maza.get()*45
                self.cokeprice = self.coke.get()*40
                self.frootiprice = self.frooti.get()*40
                self.nimkosprice = self.nimkos.get()*50
                self.biscuitsprice = self.biscuits.get()*30
                self.others_total = (
                
                                        self.mazaprice +
                                        self.cokeprice +
                                        self.frootiprice +
                                        self.nimkosprice +
                                        self.biscuitsprice 
                                        )
                self.others_price.set("Rs."+str(self.others_total))
                self.o_tax = round((self.others_total*0.08),2)
                self.others_tax.set("Rs."+str(self.o_tax))

                self.Total_Bill = self.cosmetic_total+self.grocery_total+self.others_total+self.c_tax+self.g_tax+self.o_tax

#----------------------------GENERATE FUNCTION IS FOR STATIC DESIGN OF BILL
        def Generate_bill(self):
                self.txtarea.config(state='normal')
                
                self.txtarea.delete(1.0,END)
                self.txtarea.insert(END,"          ***Welcome To Store***\n")
                self.txtarea.insert(END,f"\n Bill No. : {self.bill_no.get()}")
                self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
                self.txtarea.insert(END,f"\n Customer Ph.No. : {self.c_phone.get()}")
                self.txtarea.insert(END,"\n-----------------------------------------")
                self.txtarea.insert(END,"\n Product\t\t\t Qty\t Price")
                self.txtarea.insert(END,"\n-----------------------------------------")
#USED CONFIG ON TEXTAREA SO USER CAN'T INSERT OR DELETE VALUE USING STATE VALUE NORMAL TO DISABLED
                self.txtarea.config(state='disabled')

#THIS FUNCTION WILL GENERATE A BILL, AND IF ANY REQUIRED FIELD IS NOT ENTERED, IT WILL SHOW AN ERROR BOX. FOR EXAMPLE, IN THE NAME ENTRY AND PHONE ENTRY, ETC.

        def Billgenerate_fun(self):
                self.Generate_bill()
                self.txtarea.config(state='disabled')
                if self.c_name.get() == '' or self.c_phone.get() == '':
                        messagebox.showerror('Error',"Customer Details are Required")
                elif self.grocery_price.get() =='' and self.cosmetic_price.get()=='' and self.others_price.get()=='':
                        messagebox.showerror('Error',"Purchase of the item Required")
                elif self.grocery_price.get()=='Rs.0' and self.cosmetic_price.get()=='Rs.0' and self.others_price.get()=='Rs.0':
                        messagebox.showerror('Error',"Purchase of the item Required") 
#HERE ONLY THOSE VALUE WILL BE INSERTED INTO BILL AREA WHICE ARE NOT 0                 
                else:
                        self.txtarea.config(state='normal')
        #Cosmetics
                        if self.soap.get()!=0:
                                self.txtarea.insert(END,f"\nBath Soap\t\t\t {self.soap.get()}\t {self.soapprice}")
                        if self.face.get()!=0:
                                self.txtarea.insert(END,f"\nFace Cream\t\t\t {self.face.get()}\t {self.faceprice}")
                        if self.facewash.get()!=0:
                                self.txtarea.insert(END,f"\nFace Wash\t\t\t {self.facewash.get()}\t {self.facewashprice}")
                        if self.hairspray.get()!=0:
                                self.txtarea.insert(END,f"\nHair Spray\t\t\t {self.hairspray.get()}\t {self.hairsprayprice}")
                        if self.bodylotion.get()!=0:
                                self.txtarea.insert(END,f"\nBody Lotion\t\t\t {self.bodylotion.get()}\t {self.bodylotionprice}")
        #Gorcery
                        if self.rice.get()!=0:
                                self.txtarea.insert(END,f"\nRice \t\t\t {self.rice.get()}\t {self.riceprice}")
                        if self.foodoil.get()!=0:
                                self.txtarea.insert(END,f"\nFood Oil \t\t\t {self.foodoil.get()}\t {self.foodoilprice}")
                        if self.daal.get()!=0:
                                self.txtarea.insert(END,f"\nDaal \t\t\t {self.daal.get()}\t {self.daalprice}")    
                        if self.wheat.get()!=0:
                                self.txtarea.insert(END,f"\nWheat \t\t\t {self.wheat.get()}\t {self.wheatprice}")
                        if self.sugar.get()!=0:
                                self.txtarea.insert(END,f"\nSugar \t\t\t {self.sugar.get()}\t {self.sugarprice}")
        #Others    
                        if self.maza.get()!=0:
                                self.txtarea.insert(END,f"\nMaza \t\t\t {self.soap.get()}\t {self.mazaprice}")
                        if self.coke.get()!=0:
                                self.txtarea.insert(END,f"\nCoke \t\t\t {self.coke.get()}\t {self.cokeprice}")
                        if self.frooti.get()!=0:
                                self.txtarea.insert(END,f"\nFrooti \t\t\t {self.frooti.get()}\t {self.frootiprice}")
                        if self.nimkos.get()!=0:
                                self.txtarea.insert(END,f"\nNimkos \t\t\t {self.nimkos.get()}\t {self.nimkosprice}")
                        if self.biscuits.get()!=0:
                                self.txtarea.insert(END,f"\nBiscuits \t\t\t {self.biscuits.get()}\t {self.biscuitsprice}")
                        self.txtarea.insert(END,"\n-----------------------------------------")
                        if self.cosmetic_tax.get()!= "Rs.0.0":
                                self.txtarea.insert(END,f"\n Cosmetics Tax\t\t\t {self.cosmetic_tax.get()}")
                        if self.grocery_tax.get()!= "Rs.0.0":
                                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t {self.grocery_tax.get()}")
                        if self.others_tax.get()!= "Rs.0.0":
                                self.txtarea.insert(END,f"\n Others Tax\t\t\t {self.others_tax.get()}")
                        self.txtarea.insert(END,"\n-----------------------------------------")
                        
                        
                        self.txtarea.insert(END,f"\nTotal Bill\t\t\t\t {self.Total_Bill} ")
                        
                        self.txtarea.insert(END,"\n-----------------------------------------")

                        self.txtarea.insert(END,"\n\t\t\tThank You\n")
                        self.txtarea.config(state='disabled')
                        
                        self.save_bill()
            

#if all required field are completed user will get asked if he/she wants to save or not
        def save_bill(self):
                
                ask = messagebox.askyesno("Save?",f"Do you want to save this {self.bill_no.get()} Bill?")
                if ask:
                        self.bill_data = self.txtarea.get('1.0',END)
                        file = open("Sysbills/"+str(self.bill_no.get())+".txt","w")
                        file.write(self.bill_data)
                        file.close()
                        messagebox.showinfo("Done",f"Bill {self.bill_no.get()} has been Saved")
                        query = "INSERT INTO Customer_Details(Name,Phone_no,Bill_No,Total_bill) values(%s,%s,%s,%s)"
                        args = (self.c_name.get(),self.c_phone.get(),self.bill_no.get(),self.Total_Bill)
                        mycursor.execute(query,args)
                        mydb.commit()
                else:
                        return
#THIS FUNCTION IS USED TO FIND BILL FROM FOLDER IF EXISTS ELSE POP-UP OF ERROR WILL GET

        def bill_search(self):
                self.txtarea.config(state='normal')
                present = "no"
                for i in os.listdir('Sysbills'):
                        if i.split('.')[0] == self.find_bill.get():
                                Userfile = open(f"Sysbills/{i}",'r')
                                self.txtarea.delete('1.0',END)
                                for d in Userfile:
                                        self.txtarea.insert(END,d)
                                Userfile.close()
                                present = "Yes"
                                self.txtarea.config(state='disabled')
                if present=="no":
                        messagebox.showerror("ERROR","INVALID BILL NO!!!")
                        
                        
#THIS FUNCTION WILL CLEAR ALL FIELDS IF ENTERD BUT BEFORE THAT USER WILL GET ASKED TO CONFIRM
        def Clear(self):
                yesno=messagebox.askyesno('Sure?','Do you want to clear?')

        #------------------------------CUSTOMER DETAILS..............
                if yesno:
                        self.c_name .set("")
                        self.c_phone .set("")
                        self.bill_no .set("")
                        r = random.randint(100,2000)
                        self.bill_no.set(str(r))
                        self.find_bill .set("")
                
                #------------------------------COSMETICS..............
                        self.soap.set(0)
                        self.face .set(0)
                        self.facewash .set(0)
                        self.hairspray .set(0)
                        self.bodylotion .set(0)
                #------------------------------GROCERY..............
                        self.rice .set(0)
                        self.foodoil .set(0)
                        self.daal .set(0)
                        self.wheat .set(0)
                        self.sugar .set(0)
                #------------------------------OTHERS..............
                        self.maza .set(0)
                        self.coke .set(0)
                        self.frooti .set(0)
                        self.nimkos .set(0)
                        self.biscuits .set(0)
                #------------------------------TOTAL PRODUCT PRICE & TAX...............
                        self.cosmetic_price .set("")
                        self.grocery_price .set("")
                        self.others_price .set("")

                        self.cosmetic_tax .set("")
                        self.grocery_tax .set("")
                        self.others_tax .set("")
                        self.txtarea.config(state='normal')
                        self.Generate_bill()
                else:
                        return
                                        
root=Tk()
obj = Bill_App(root)
root.mainloop()