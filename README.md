###This program is used to act as an ATM-system with a predefined database which is used to run the program
##	for the first time. 
##
###When the GUI getting closed, it saves all the data changes in a USERs.txt file
##	to avoid data changes getting lost.
##
###if you want to start the program with the basic data delete the USERs.txt file and run the program, 
##	note that a sentence saying this is the first time to run the program will be printed in CMD.
##
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
