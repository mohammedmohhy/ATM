###This program is used to act as an ATM-system with a predefined database which is used to run the program
#	for the first time. 
#
###When the GUI getting closed, it saves all the data changes in a USERs.txt file
#	to avoid data changes getting lost.
#
###if you want to start the program with the basic data delete the USERs.txt file and run the program, 
#	note that a sentence saying this is the first time to run the program will be printed in CMD.
#
'''program describtion:
	1-the system first asks the user to enter his ID.
		*if the user entered a not registered ID the system will print a message 
		the this ID is not registered.
		*if the user pressed enter without entering any value the systems will not crash.
	
	2-if the user entered a valid ID, the system asks for the password.
		*the user has only three trials to enter the right password.
		*if he didn't he will be blocked, even if the program is closed and re-opened.
		*if the user pressed enter without entering any value the systems will not crash.
		*the passwrod entry field is shown as ***.
		
	3-if the user entered the right password, the systems asks for the operation needed.
		3.1-cash withdraw:
				*It asks the user to enter the amount of money to withdraw.
				*If his balance is not enough an error message will be printed and return to the main window.
				*maximum allowed value per transaction is 5000.
				*the allowed values are multiples of 100.
				*If a successful operation done it will print a message and return to the home page.
		
		3.2-Balance inquiry:
				*It prints the User Name and his Balance, then return to the home page.
			
		3.3-Password change:
				*It asks the user to enter the new passwrod twice.
				*the maximum limit of the entry is 4-characters and showed as ****.
				*the password must be 4 characters not less than that.
				*if the user pressed enter without entering any value the systems will not crash.
				*if the user entered not matched passwords, the system will show an error message.
				*If the user changed his password successfully the system returns to the homepage.
			
		3.4-Fawry services:
				*It asks the user to choose an option of the communication companies.
				
				3.4.1-Etisalat:
						*the system asks the user to enter an etisalat number, and the amount of balance.
						*the number entry is limited to 11 numbers.
						*the number must be 11 not less than that.
						*the number must starts with 011.
						*the balance must be enough or an error message will be printed.
						*if a successful operation done the balance is updated.
				3.4.2 , 3.4.3 - Vodafone, etisalat :are the same as etisalat.
				
				3.4.4-We:
						*the system asks the user to enter an home number, and the amount of balance.
						*the number entry is limited to 10 numbers.
						*the number must be 10 not less than that.
						*the number must starts with 02.
						*the balance must be enough or an error message will be printed.
						*if a successful operation done the balance is updated.
'''
import tkinter 
from tkinter import messagebox 
import pickle



#dictionary that holds all the database of the bank
#this implementation is for the first run only, when the system closed and re-opened,
#this data will be overwritten by the USERs.txt file content
USERs = { "1":{"Name":"Ahmed","Password":"1783","Balance":3500166,"Access":"available"},
			"2":{"Name":"Salma","Password":"1390","Balance":520001,"Access":"available"},
			"3":{"Name":"Adel","Password":"1214","Balance":111000,"Access":"available"},
			"4":{"Name":"Saeed","Password":"2001","Balance":1200,"Access":"available"},
			"5":{"Name":"Amir","Password":"8935","Balance":178933,"Access":"available"},
			"6":{"Name":"Adel","Password":"3420","Balance":55000,"Access":"available"},
			"7":{"Name":"Adel","Password":"1179","Balance":18000,"Access":"available"},
			"8":{"Name":"Adel","Password":"1430","Balance":180350,"Access":"available"},
			}


#function to read the database file when program has just been started
def Read_dict():
	global USERs
	Read_file = open("USERs.txt",'rb')
	USERs = pickle.load(Read_file)
#function to write the database file when the program is to be ended
def Write_dict():
	Write_file = open("USERs.txt","wb")
	pickle.dump(USERs,Write_file)
	Write_file.close()

	
#function used to limit the phone number entry size to only 11 digits
def phone_limit_func(*args):
	global entry_text1
	if len(entry_text1.get()) >11:
		entry_text1.set(entry_text1.get()[:11])
		
#function used to limit the home number entry size to only 10 digits
def home_limit_func(*args):
	global entry_text1
	if len(entry_text1.get()) >10:
		entry_text1.set(entry_text1.get()[:10])

		
#function used to limit the password entries size to only 4 digits
def character_limit_func(*args):
	global entry_text1
	global entry_text2
	if len(entry_text1.get()) > 4:
		entry_text1.set(entry_text1.get()[:4])
	if len(entry_text2.get()) > 4:
		entry_text2.set(entry_text2.get()[:4])

######################################################################################################################
############################################ask before closing window###########################################################
###################################################################################################################
def on_closing():
	#if the user presses ok, the dictionary will be saved in a file and the program exits
	if messagebox.askokcancel("quit","Are you sure ?"):
		Write_dict()
		exit()

		

######################################################################################################################
############################################We window###########################################################
#######################################################################################################################
#function to be called when back button is pressed
def We_window_back():
	global We_window
	We_window.destroy()
	create_Fawry_window()

#function to be called when the enter button is pressed
def Enter_We_func():
	global entered_ID
	global entered_phone
	global entered_amount
	#will be used for destroy
	global We_window
	
	if(entered_amount.get() == ""):
		x=1#do nothing
	#check if the process wil be done
	elif entered_phone.get()[:2]=="02" and len(entered_phone.get())==10 and int(entered_amount.get())<=int(USERs[entered_ID]["Balance"]):
		messagebox.showinfo("message","Balance recharged successfully")
		USERs[entered_ID]["Balance"]-= int(entered_amount.get())
	#check if the users balance is not enough
	elif int(entered_amount.get())>int(USERs[entered_ID]["Balance"]):
		messagebox.showerror("error","No sufficient Balance")
		We_window.destroy()
		create_window()
	#check if the entered home number is wrong
	elif len(entered_phone.get())!=10:
		messagebox.showerror("error","wrong home number")
	#check if the entered phone number is not a home number
	elif entered_phone.get()[:2]!="02":
		messagebox.showerror("error","this home number doesn't start with 02")
	
def create_We_window():
	global entered_phone
	global entered_amount
	global We_window
	###################################create We window#################################################
	We_window = tkinter.Tk()
	We_window.title("Vodafone_window")
	
	b_img= tkinter.PhotoImage(file = "We.png")
	load_img= tkinter.Label(We_window, i=b_img)
	load_img.pack()
	
	We_window.geometry("500x500+300+150")
	We_window.resizable(True,True)
	We_window.configure(background="grey")
	We_window.protocol("WM_DELETE_WINDOW",on_closing)
	#########################################################################################################
	
	########################variable used to limit the entry size by the home_limit_func#####################
	global entry_text1
	entry_text1 = tkinter.StringVar()
	entry_text1.trace("w",home_limit_func)
	##########################################################################################################
	
	######################################labels & buttons & entries###############################################
	label = tkinter.Label(We_window,text="Enter the home number: ", bg="grey",fg="black",)
	label.place(x=0,y=200)

	entered_phone = tkinter.Entry(We_window, width = 40, fg = "red", textvariable = entry_text1)
	entered_phone.place(x=180,y=200)
	
	label2 = tkinter.Label(We_window,text="Enter the amount: ", bg="grey",fg="black")
	label2.place(x=0,y=250)
	entered_amount = tkinter.Entry(We_window, width = 40, fg = "red")
	entered_amount.place(x=180,y=250)
	
	Enter_Btn = tkinter.Button(We_window,text = "Enter", command = Enter_We_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Enter_Btn.place(x=250,y=280)
	
	back_button = tkinter.Button(We_window,text="back",bg="black",fg="red",command=We_window_back)
	back_button.place(x=0,y=0)
	##############################################################################################################
	We_window.mainloop()	
		

		
		
		
		
#######################################################################################################################
############################################Orange window###########################################################
#######################################################################################################################
#function to be called when back button is pressed
def Orange_window_back():
	global Orange_window
	Orange_window.destroy()
	create_Fawry_window()

#function to be called when the enter button is pressed
def Enter_Orange_func():
	global entered_ID
	global entered_phone
	global entered_amount
	#will be used for destroy
	global Orange_window
	
	if(entered_amount.get() == ""):
		x=1#do nothing
	#check if the process wil be done
	elif entered_phone.get()[:3]=="012" and len(entered_phone.get())==11 and int(entered_amount.get())<=int(USERs[entered_ID]["Balance"]):
		messagebox.showinfo("message","Balance recharged successfully")
		USERs[entered_ID]["Balance"]-= int(entered_amount.get())
	#check if the users balance is not enough
	elif int(entered_amount.get())>int(USERs[entered_ID]["Balance"]):
		messagebox.showerror("error","No sufficient Balance")
		Orange_window.destroy()
		create_window()
	#check if the entered phone number is wrong
	elif len(entered_phone.get())!=11:
		messagebox.showerror("error","wrong phone number")
	#check if the entered phone number is not an Orange number
	elif entered_phone.get()[:3]!="012":
		messagebox.showerror("error","this number is not an Orange number")
#function to be called when Orange option is pressed
def create_Orange_window():
	global entered_phone
	global entered_amount
	global Orange_window
	###################################create Orange window#################################################
	Orange_window = tkinter.Tk()
	Orange_window.title("Vodafone_window")
	
	b_img= tkinter.PhotoImage(file = "Orange.png")
	load_img= tkinter.Label(Orange_window, i=b_img)
	load_img.pack()
	
	Orange_window.geometry("500x500+300+150")
	Orange_window.resizable(True,True)
	Orange_window.configure(background="grey")
	Orange_window.protocol("WM_DELETE_WINDOW",on_closing)
	##########################################################################################################
	
	########################variable used to limit the entry size by the phone_limit_func#####################
	global entry_text1
	entry_text1 = tkinter.StringVar()
	entry_text1.trace("w",phone_limit_func)
	###########################################################################################################
	
	######################################labels & buttons & entries############################################
	label = tkinter.Label(Orange_window,text="Enter the phone number: ", bg="grey",fg="black",)
	label.place(x=0,y=200)

	entered_phone = tkinter.Entry(Orange_window, width = 40, fg = "red", textvariable = entry_text1)
	entered_phone.place(x=180,y=200)
	
	label2 = tkinter.Label(Orange_window,text="Enter the amount: ", bg="grey",fg="black")
	label2.place(x=0,y=250)
	entered_amount = tkinter.Entry(Orange_window, width = 40, fg = "red")
	entered_amount.place(x=180,y=250)
	
	Enter_Btn = tkinter.Button(Orange_window,text = "Enter", command = Enter_Orange_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Enter_Btn.place(x=250,y=280)
	
	back_button = tkinter.Button(Orange_window,text="back",bg="black",fg="red",command=Orange_window_back)
	back_button.place(x=0,y=0)
	##############################################################################################################
	Orange_window.mainloop()




#######################################################################################################################
############################################vodafone window###########################################################
#######################################################################################################################
#function to be called when the back button is pressed
def Vodafone_window_back():
	global Vodafone_window
	Vodafone_window.destroy()
	create_Fawry_window()

#function to be called when the enter button is pressed
def Enter_Vodafone_func():
	global entered_ID
	global entered_phone
	global entered_amount
	#will be used for destroy
	global Vodafone_window
	
	if(entered_amount.get() == ""):
		x=1#do nothing
	#check if the process wil be done
	elif entered_phone.get()[:3]=="010" and len(entered_phone.get())==11 and int(entered_amount.get())<=int(USERs[entered_ID]["Balance"]):
		messagebox.showinfo("message","Balance recharged successfully")
		USERs[entered_ID]["Balance"]-= int(entered_amount.get())
	#check if the users balance is not enough
	elif int(entered_amount.get())>int(USERs[entered_ID]["Balance"]):
		messagebox.showerror("error","No sufficient Balance")
		Vodafone_window.destroy()
		create_window()
	#check if the entered phone number is wrong
	elif len(entered_phone.get())!=11:
		messagebox.showerror("error","wrong phone number")
	#check if the entered phone number is not a Vodafone number
	elif entered_phone.get()[:3]!="010":
		messagebox.showerror("error","this number is not a Vodafone number")
	
#function to be called when the Vodafone option is pressed	
def create_Vodafone_window():
	global entered_phone
	global entered_amount
	global Vodafone_window
	###################################create Vodafone window#################################################
	Vodafone_window = tkinter.Tk()
	Vodafone_window.title("Vodafone_window")
	
	b_img= tkinter.PhotoImage(file = "Vodafone.png")
	load_img= tkinter.Label(Vodafone_window, i=b_img)
	load_img.pack()
	
	Vodafone_window.geometry("500x500+300+150")
	Vodafone_window.resizable(True,True)
	Vodafone_window.protocol("WM_DELETE_WINDOW",on_closing)
	#########################################################################################################
	
	########################variable used to limit the entry size by the phone_limit_func#####################
	global entry_text1
	entry_text1 = tkinter.StringVar()
	entry_text1.trace("w",phone_limit_func)
	########################################################################################################
	
	######################################labels & buttons & entries############################################
	label = tkinter.Label(Vodafone_window,text="Enter the phone number: ", bg="grey",fg="black",)
	label.place(x=0,y=200)
	entered_phone = tkinter.Entry(Vodafone_window, width = 40, fg = "red", textvariable = entry_text1)
	entered_phone.place(x=180,y=200)
	
	label2 = tkinter.Label(Vodafone_window,text="Enter the amount: ", bg="grey",fg="black")
	label2.place(x=0,y=250)
	entered_amount = tkinter.Entry(Vodafone_window, width = 40, fg = "red")
	entered_amount.place(x=180,y=250)
	
	Enter_Btn = tkinter.Button(Vodafone_window,text = "Enter", command = Enter_Vodafone_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Enter_Btn.place(x=250,y=280)
	
	back_button = tkinter.Button(Vodafone_window,text="back",bg="black",fg="red",command=Vodafone_window_back)
	back_button.place(x=0,y=0)
	###########################################################################################################
	
	Vodafone_window.mainloop()



#######################################################################################################################
############################################Etisalat window###########################################################
#######################################################################################################################
#function to be called when the back button is pressed
def Etisalat_window_back():
	global Etisalat_window
	Etisalat_window.destroy()
	create_Fawry_window()

#function to be called when the enter button on the window2 is pressed
def Enter_Etisalat_func():
	global entered_ID
	global entered_phone
	global entered_amount
	#will be used for destroy
	global Etisalat_window
	if(entered_amount.get() == ""):
		x=1#do nothing
	#check if the user is process will be done
	elif entered_phone.get()[:3]=="011" and len(entered_phone.get())==11 and int(entered_amount.get())<=int(USERs[entered_ID]["Balance"]):
		messagebox.showinfo("message","Balance recharged successfully")
		USERs[entered_ID]["Balance"]-= int(entered_amount.get())
	#check if the users balance is not enough
	elif int(entered_amount.get())>int(USERs[entered_ID]["Balance"]):
		messagebox.showerror("error","No sufficient Balance")
		Etisalat_window.destroy()
		create_window()
	#check if the entered phone number is wrong
	elif len(entered_phone.get())!=11:
		messagebox.showerror("error","wrong phone number")
	#check if the entered phone number is not an etisalat number
	elif entered_phone.get()[:3]!="011":
		messagebox.showerror("error","this number is not an etisalat number")

#function to be called when the Etisalat option is pressed	
def create_Etisalat_window():
	global entered_phone
	global entered_amount
	global Etisalat_window
	###################################create Etisalat window#################################################
	Etisalat_window = tkinter.Tk()
	Etisalat_window.title("Etisalat_window")
	
	b_img= tkinter.PhotoImage(file = "Etisalat.png")
	load_img= tkinter.Label(Etisalat_window, i=b_img)
	load_img.pack()
	
	Etisalat_window.geometry("500x500+300+150")
	Etisalat_window.resizable(True,True)
	Etisalat_window.configure(background="grey")
	Etisalat_window.protocol("WM_DELETE_WINDOW",on_closing)
	#########################################################################################################
	
	########################variable used to limit the entry size by the phone_limit_func#####################
	global entry_text1
	entry_text1 = tkinter.StringVar()
	entry_text1.trace("w",phone_limit_func)
	#########################################################################################################
	
	######################################labels & buttons & entries############################################
	label = tkinter.Label(Etisalat_window,text="Enter the phone number: ", bg="grey",fg="black",)
	label.place(x=0,y=200)
	entered_phone = tkinter.Entry(Etisalat_window, width = 40, fg = "red", textvariable = entry_text1)
	entered_phone.place(x=180,y=200)
	
	label2 = tkinter.Label(Etisalat_window,text="Enter the amount: ", bg="grey",fg="black")
	label2.place(x=0,y=250)
	entered_amount = tkinter.Entry(Etisalat_window, width = 40, fg = "red")
	entered_amount.place(x=180,y=250)
	
	Enter_Btn = tkinter.Button(Etisalat_window,text = "Enter", command = Enter_Etisalat_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Enter_Btn.place(x=250,y=280)
	
	back_button = tkinter.Button(Etisalat_window,text="back",bg="black",fg="red",command=Etisalat_window_back)
	back_button.place(x=0,y=0)
	############################################################################################################
	
	Etisalat_window.mainloop()
	
	


#######################################################################################################################
################################################Fawry window###########################################################
#######################################################################################################################
#function to be called when back button iis pressed
def Fawry_window_back():
	global Fawry_window
	Fawry_window.destroy()
	create_window3()




#function to be called when the enter button on the window2 is pressed
def services_func():
	global service_chosen
	#used for destroy
	global Fawry_window
	#check if the user is etisalat user
	if service_chosen.get() == 1:
		Fawry_window.destroy()
		create_Etisalat_window()
	#check if the user is vodafone user
	elif service_chosen.get()==2:
		Fawry_window.destroy()
		create_Vodafone_window()
	#check if the user is We user
	elif service_chosen.get()==3:
		Fawry_window.destroy()
		create_Orange_window()
	#check if the user is Orange user
	elif service_chosen.get()==4:
		Fawry_window.destroy()
		create_We_window()


#function to be called when the Fawry services option is pressed
def create_Fawry_window():
	global service_chosen
	#will be used in destroy 
	global Fawry_window
	Fawry_window = tkinter.Tk()
	
	b_img= tkinter.PhotoImage(file = "Fawry.png")
	load_img= tkinter.Label(Fawry_window, i=b_img)
	load_img.pack()
	
	Fawry_window.title("Fawry_window")
	Fawry_window.geometry("500x500+300+150")
	Fawry_window.resizable(True,True)
	Fawry_window.configure(background="grey")
	Fawry_window.protocol("WM_DELETE_WINDOW",on_closing)
	
	###########################################labels & buttons############################################
	label = tkinter.Label(Fawry_window,text="Please select an option", bg="grey",fg="black")
	label.place(x=0,y=70)
	
	#this button defined here as it must be defined while a window is already opened
	service_chosen = tkinter.IntVar()
	
	Etisalat_Btn=tkinter.Radiobutton(Fawry_window,text="Etisalat",value=1, bg="grey",fg="black",variable=service_chosen,command=services_func)
	Vodafone_Btn=tkinter.Radiobutton(Fawry_window,text="Vodafone",value=2, bg="grey",fg="black",variable=service_chosen,command=services_func)
	Orange_Btn=tkinter.Radiobutton(Fawry_window,text="Orange",value=3, bg="grey",fg="black",variable=service_chosen,command=services_func)
	We_Btn=tkinter.Radiobutton(Fawry_window,text="We",value=4, bg="grey",fg="black",variable=service_chosen,command=services_func)
	
	Etisalat_Btn.place(x=0,y=100)
	Vodafone_Btn.place(x=0,y=130)
	Orange_Btn.place(x=0,y=160)
	We_Btn.place(x=0,y=190)
	
	back_button = tkinter.Button(Fawry_window,text="back",bg="black",fg="red",command=Fawry_window_back)
	back_button.place(x=0,y=0)
	#####################################################################################################
	
	window3.mainloop()






#######################################################################################################################
################################################Change password window###########################################################
#######################################################################################################################
#function to be called when the back button is pressed
def Pass_window_back():
	global pass_window
	pass_window.destroy()
	create_window3()

#function to be called when the enter new password button is pressed
def Pass_Btn_func():
	global entered_ID
	global entered_Pass1
	global entered_Pass2
	global pass_window
	#check if the user has enough balance
	if entered_Pass1.get() == entered_Pass2.get() and len(entered_Pass1.get())==4:
		USERs[entered_ID]["Password"] = entered_Pass1.get()
		messagebox.showinfo("message","password changed successfully")
		#close the current window
		pass_window.destroy()
		#back to the home page
		create_window()
	else:
		messagebox.showerror("error","failed to change the password, please enter a password with a length of four and match your two entries")
	
#function to be called when the change password option is pressed
def create_Password_window():
	global entered_Pass1
	global entered_Pass2
	global pass_window
	pass_window = tkinter.Tk()
	
	b_img= tkinter.PhotoImage(file = "Pass.png")
	load_img= tkinter.Label(pass_window, i=b_img)
	load_img.pack()
	
	pass_window.title("pass_window")
	pass_window.geometry("500x500+300+150")
	pass_window.resizable(True,True)
	pass_window.configure(background="grey")
	pass_window.protocol("WM_DELETE_WINDOW",on_closing)
	
	########variables used to limit the entry size by the character_limit function##########
	global entry_text1
	entry_text1 = tkinter.StringVar()
	entry_text1.trace("w",character_limit_func)
	global entry_text2
	entry_text2 = tkinter.StringVar()
	entry_text2.trace("w",character_limit_func)
	##########################################################################################
	
	label = tkinter.Label(pass_window,text="Enter your new password", bg="grey",fg="black",)
	label.place(x=0,y=280)
	entered_Pass1 = tkinter.Entry(pass_window, width = 40, fg = "red", textvariable = entry_text1,show = "*")
	entered_Pass1.place(x=180,y=280)
	
	label2 = tkinter.Label(pass_window,text="Re-enter your new password", bg="grey",fg="black")
	label2.place(x=0,y=310)
	entered_Pass2 = tkinter.Entry(pass_window, width = 40, fg = "red", textvariable = entry_text2,show = "*")
	entered_Pass2.place(x=180,y=310)
	
	Pass_Btn = tkinter.Button(pass_window,text = "Enter", command = Pass_Btn_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Pass_Btn.place(x=200,y=340)
	
	back_button = tkinter.Button(pass_window,text="back",bg="black",fg="red",command=Pass_window_back)
	back_button.place(x=0,y=0)
	
	pass_window.mainloop()






#######################################################################################################################
#############################################Balance inquiry###########################################################
#######################################################################################################################
#function to be called when the Balance inquiry option is pressed
def Balance_message_func():
	messagebox.showinfo("message","Your name is: " +str((USERs[entered_ID]["Name"]))+"\nYour Balance is: "+str((USERs[entered_ID]["Balance"]))+" ")
	#destroy the current window
	window3.destroy()
	#back to the home page
	create_window()
	
	

#######################################################################################################################
################################################Cash withdraw window###########################################################
#######################################################################################################################
#function will be implemented later, responsible for delivering the money to the user
def ATM_Actuator_Out(amount):
	x=1

	#function to be called when the enter amount of cash button is pressed
def Cash_Btn_func():
	global balance_label_pos
	global entered_Cash
	if(entered_Cash.get() == ""):
		x=1#do nothing
	#check if the user has enough balance
	elif USERs[entered_ID]["Balance"] < int(entered_Cash.get()):     
		messagebox.showerror("Error","not enough balance, your current balance is: " +str((USERs[entered_ID]["Balance"]))+" ")
		#close the current window
		cash_window.destroy()
		#back to the home page
		create_window()
	#check if the user has enough balance, the amount of money are less than 5000, the amount of money are multiple of 100 and not negative
	elif USERs[entered_ID]["Balance"] > int(entered_Cash.get()) and int(entered_Cash.get())<=5000 and int(entered_Cash.get())>0 and int(entered_Cash.get())% 100.0 ==0:
		USERs[entered_ID]["Balance"] -= int(entered_Cash.get())
		messagebox.showinfo("message","Done, your current balance is: " +str((USERs[entered_ID]["Balance"]))+" ")
		#close the current window
		cash_window.destroy()
		#back to the home page
		create_window()
	elif int(entered_Cash.get())> 5000:
		messagebox.showerror("Error","You can withdraw a maximum of 5000EGP: ") 
	elif int(entered_Cash.get())% 100.0 !=0:
		messagebox.showerror("Error","You can withdraw multiples of 100 only: ") 
	else:
		messagebox.showwarning("warning","Nothing done: ") 

#function to be called when the back button is pressed	
def Cash_window_back():
	global cash_window
	cash_window.destroy()
	create_window3()
	

#function called if the cash withdraw option pressed
def create_Cash_window():
	global cash_window
	global entered_Cash
	cash_window = tkinter.Tk()
	
	b_img= tkinter.PhotoImage(file = "Money.png")
	load_img= tkinter.Label(cash_window, i=b_img)
	load_img.pack()
	
	cash_window.title("cash_window")
	cash_window.geometry("500x500+300+150")
	cash_window.resizable(True,True)
	cash_window.configure(background="grey")
	cash_window.protocol("WM_DELETE_WINDOW",on_closing)

	
	label = tkinter.Label(cash_window,text="Enter the desired amount of cash to withdraw", bg="grey",fg="black")
	label.place(x=150,y=170)
	
	entered_Cash = tkinter.Entry(cash_window, width = 40, fg = "red")
	entered_Cash.place(x=150,y=200)
	
	Cash_Btn = tkinter.Button(cash_window,text = "Enter", command = Cash_Btn_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Cash_Btn.place(x=250,y=230)
	
	back_button = tkinter.Button(cash_window,text="back",bg="black",fg="red",command=Cash_window_back)
	back_button.place(x=0,y=0)
	
	cash_window.mainloop()





#######################################################################################################################
################################################third window###########################################################
#######################################################################################################################
#function to be called when the back button is pressed
def window3_back():
	global window2
	window3.destroy()
	create_window2()
	


#function to be called when an option is pressed
def options_func():
	global option_chosen
	#will be used for destroy
	global window3
	if option_chosen.get() == 1:
		window3.destroy()
		create_Cash_window()
	elif option_chosen.get()==2:
		Balance_message_func()
	elif option_chosen.get()==3:
		window3.destroy()
		create_Fawry_window()
	elif option_chosen.get()==4:
		window3.destroy()
		create_Password_window()


#function to be called when the second window is done, it creates the third window, asks user to choose an option
def create_window3():
	global option_chosen
	#will be used in destroy 
	global window3
	window3 = tkinter.Tk()
	
	bg_img= tkinter.PhotoImage(file = "ATM.png")
	load_img= tkinter.Label(window3, i=bg_img)
	load_img.pack()
	
	window3.title("window3")
	window3.geometry("500x500+300+150")
	window3.resizable(True,True)
	window3.protocol("WM_DELETE_WINDOW",on_closing)
	
	###########################################labels buttons############################################
	label = tkinter.Label(window3,text="Please select an option: ", bg="grey",fg="black")
	label.place(x=70,y=120)
	
	#this button defined here as it must be defined while a window is already opened
	option_chosen = tkinter.IntVar()
	
	Cash_Btn=tkinter.Radiobutton(window3,text="Cash Withdraw",value=1, bg="grey",fg="black",variable=option_chosen,command=options_func)
	Balance_Btn=tkinter.Radiobutton(window3,text="Balance Inquiry",value=2, bg="grey",fg="black",variable=option_chosen,command=options_func)
	Fawry_Btn=tkinter.Radiobutton(window3,text="Fawry Services",value=3, bg="grey",fg="black",variable=option_chosen,command=options_func)
	Pass_Btn=tkinter.Radiobutton(window3,text="Password Change",value=4, bg="grey",fg="black",variable=option_chosen,command=options_func)
	
	Cash_Btn.place(x=90,y=148)
	Balance_Btn.place(x=90,y=176)
	Fawry_Btn.place(x=90,y=204)
	Pass_Btn.place(x=90,y=232)
	
	back_button = tkinter.Button(window3,text="back",bg="black",fg="red",command=window3_back)
	back_button.place(x=0,y=0)
	#####################################################################################################
	
	window3.mainloop()

	
	
	
	
#######################################################################################################################
################################################second window###########################################################
#######################################################################################################################
#function to be called when the back button is pressed
def window2_back():
	global window2
	window2.destroy()
	create_window()
	
	
#function to be called when the enter button of the password is pressed
#if the user entered his password wrong 3-consecutive times he will be blocked forever
def Btn2_func():
	global wrong_pass
	global window2
	global entered_ID
	global entered_pass
	
	if USERs[entered_ID]["Password"]==entered_pass.get() and USERs[entered_ID]["Access"]=="available":
		#every right entry of the password the counter returns to zero
		wrong_pass=0
		window2.destroy()
		create_window3()
		
	elif USERs[entered_ID]["Password"] != entered_pass.get() and wrong_pass<2 and USERs[entered_ID]["Access"]=="available":
		wrong_pass +=1
		#label = tkinter.Label(window2,text="wrong password, please try again", bg="grey",fg="black")
		#label.place(x=200,y=300)
		messagebox.showwarning("warning","wrong password, please try again")
	else:
		USERs[entered_ID]["Access"]="blocked"
		messagebox.showerror("error","this accound is blockedd please go to the bank branch")

#function to be called when the first window is done, it creates the second window, asks for his password
def create_window2():
	global window2
	global entered_pass
	window2 = tkinter.Tk()
	
	bg_img= tkinter.PhotoImage(file = "ATM.png")
	load_img= tkinter.Label(window2, i=bg_img)
	load_img.pack()
	
	window2.title("window2")
	window2.geometry("500x500+300+150")
	window2.resizable(True,True)
	window2.protocol("WM_DELETE_WINDOW",on_closing)
	
	###########################################labels buttons############################################
	label = tkinter.Label(window2,text="Enter your password", bg="grey",fg="black")
	label.place(x=90,y=140)
	
	entered_pass = tkinter.Entry(window2, width = 40, fg = "red",show="*")
	entered_pass.place(x=90,y=160)
	
	Btn = tkinter.Button(window2,text = "Enter", command = Btn2_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Btn.place(x=150,y=200)
	
	back_button = tkinter.Button(window2,text="back",bg="black",fg="red",command=window2_back)
	back_button.place(x=0,y=0)
	#####################################################################################################
	
	window2.mainloop()

	
	
	
	
#######################################################################################################################
################################################first window###########################################################
#######################################################################################################################
#function to be called when the ID_Enter_button is pressed
def Btn_func():
	global wrong_pass
	global entered_ID
	global main_window
	temp = entered_ID.get()
	if temp in USERs:
		#every right entry of the ID the counter returns to zero
		wrong_pass=0
		entered_ID = entered_ID.get()
		main_window.destroy()
		create_window2()
		
	else:
		#label = tkinter.Label(main_window,text="this user is not recognized", bg="grey",fg="black")
		#label.place(x=200,y=300)
		messagebox.showerror("error","this user is not recognized")

#function that creates the first GUI window, asks the user to enter his ID
def create_window():
	global entered_ID
	global main_window
	###########creating the main window###########
	main_window = tkinter.Tk()
	
	bg_img= tkinter.PhotoImage(file = "ATM.png")
	load_img= tkinter.Label(main_window, i=bg_img)
	load_img.pack()
	
	main_window.title("main window")
	main_window.geometry("500x500+300+150")
	main_window.resizable(True,True)
	#main_window.configure(background="grey")
	main_window.protocol("WM_DELETE_WINDOW",on_closing)
	##############################################	
		
	###########################################labels buttons############################################
	label = tkinter.Label(main_window,text="Enter your account number", bg="grey",fg="black")
	label.place(x=90,y=140)
	
	entered_ID = tkinter.Entry(main_window, width = 40, fg = "red")
	entered_ID.place(x=90,y=160)
	
	Btn = tkinter.Button(main_window,text = "Enter", command = Btn_func, width = 4, height = 2, bg = 'grey', fg = 'black')
	Btn.place(x=150,y=200)
	#####################################################################################################
	
	
	main_window.mainloop()



###########################################application program#########################################
#trying to read the database file
try:
	Read_dict()
#if the file was deleted, the program will run with the basic data in the code
except:
	print("this is the first time to run the program")
#creating the first GUI window
create_window()


