adminoptions = [("1.","View Bookings"),
               ("2.","Block Dates"),
                ("3.","Log Out")]
               
weekdays = [("1.","Monday"),
               ("2.","Tuesday"),
               ("3.","Wednesday"),
               ("4.","Thursday"),
               ("5.","Friday"),
               ("6.","Saturday"),
               ("7.","Sunday")]

mondaydates = [("1.","15/05"),
               ("2.","22/05"),
               ("3.","29/05"),
               ("4.","05/06"),
               ("5.","12/06"),
               ("6.","19/06"),
               ("7.","26/06")]

tuesdaydates = [("1.","16/05"),
               ("2.","23/05"),
               ("3.","30/05"),
               ("4.","06/06"),
               ("5.","13/06"),
               ("6.","20/06"),
               ("7.","27/06")]

wednesdaydates = [("1.","17/05"),
               ("2.","24/05"),
               ("3.","31/05"),
               ("4.","07/05"),
               ("5.","14/06"),
               ("6.","21/06"),
               ("7.","28/06")]

thursdaydates = [("1.","18/05"),
               ("2.","25/05"),
               ("3.","01/06"),
               ("4.","08/06"),
               ("5.","15/06"),
               ("6.","22/06"),
               ("7.","29/06")]

fridaydates = [("1.","19/05"),
               ("2.","26/05"),
               ("3.","02/06"),
               ("4.","09/06"),
               ("5.","16/06"),
               ("6.","23/06"),
               ("7.","30/06")]

saturdaydates = [("1.","20/05"),
               ("2.","27/05"),
               ("3.","03/06"),
               ("4.","10/06"),
               ("5.","17/06"),
               ("6.","24/06"),
               ("7.","01/07")]

sundaydates = [("1.","21/05"),
               ("2.","28/05"),
               ("3.","04/06"),
               ("4.","11/06"),
               ("5.","18/06"),
               ("6.","25/06"),
               ("7.","02/07")]

times = [("1.","10:00pm"),
         ("2.","12:30pm"),
         ("3.","13:00pm"),
         ("4.","13:30pm"),
         ("5.","14:00pm"),
         ("6.","14:30pm"),
         ("7.","15:00pm"),
         ("8.","15:30pm"),
         ("9.","16:00pm"),
         ("10.","16:30pm"),
         ("11.","17:00pm"),
         ("12.","17:30pm"),
         ("13.","18:00pm"),
         ("14.","18:30pm"),
         ("15.","19:00pm"),]

bookings = []
booktestlist = []
duplicatelist = []

entertainerlist = [("1.","Dino The Saur"),
                ("2.","Softy The Fluffy"),
                ("3.","Rino The Ceraptor"),
                ("4.","Dash The Scary"),
                ]

                    
def makeBooking():
    print()
    for Num,Name in entertainerlist: 
        print(Num,Name,)
    print()
    
    validentertainer = False
    while validentertainer == False:
        try:
            entertainerchoice = input("Which entertainer would you like to book? Please choose a number from the list above: ")
            if entertainerchoice == "quit" or entertainerchoice == "Quit" or entertainerchoice == "QUIT":
                return
            elif int(entertainerchoice) < 1 or int(entertainerchoice) > 4:
                 print("This number is not on the list.")
            else:
                entertainer = entertainerlist[int(entertainerchoice) - 1]
                validentertainer = True
        except:
            print("Please enter a valid number.")

            
    print()
    print("Here are the available booking dates")
    print()
    for Num,Day in weekdays: 
        print(Num,Day)
    print()
    
    validday = False
    while validday == False:
        try:
            daychoice = input("Which day is best for you? ")
            if daychoice == "quit" or daychoice == "Quit" or daychoice == "QUIT":
                return
            elif int(daychoice) < 1 or int(daychoice) > 7:
                 print("This number is not on the list.")
            else:
                weekday = weekdays[int(daychoice) - 1]
                validday = True
        except:
            print("Please enter a valid number.")

            
    if str(weekday[1]) == "Monday":
        whichdates = mondaydates
    elif str(weekday[1]) == "Tuesday":
        whichdates = tuesdaydates
    elif str(weekday[1]) == "Wednesday":
        whichdates = wednesdaydates
    elif str(weekday[1]) == "Thursday":
        whichdates = thursdaydates
    elif str(weekday[1]) == "Friday":
        whichdates = fridaydates
    elif str(weekday[1]) == "Saturday":
        whichdates = saturdaydates
    elif str(weekday[1]) == "Sunday":
        whichdates = sundaydates

        
    print()
    print("Here are the dates for " , str(weekday[1]))
    print()
    
    for Num,Day in whichdates: 
        print(Num,Day)
    print()
    
    validdate = False
    while validdate == False:
        try:
            datechoice = input("Which date would suit you best? ")
            if datechoice == "quit" or datechoice == "Quit" or datechoice == "QUIT":
                return
            elif int(datechoice) < 1 or int(datechoice) > 7:
                 print("This number is not on the list.")
            else:
                date = whichdates[int(datechoice) - 1]
                validdate = True
        except:
            print("Please enter a valid number.")

            
    print()
    print("Here are the times for " , str(weekday[1]),"," , str(date[1]))
    print()
    
    for Num,Time in times: 
        print(Num,Time)
    print()
    validtime = False
    while validtime == False:
        try:
            timechoice = input("Which time would you like? ")
            if timechoice == "quit" or timechoice == "Quit" or timechoice == "QUIT":
                return
            elif int(timechoice) < 1 or int(timechoice) > 15:
                 print("This number is not on the list.")
            else:
                time = times[int(timechoice) - 1]
                booktest = (str(date[1]), str(time[1]))
                if booktest in booktestlist:
                    print("Sorry, someone has already taken that time.")
                    validtime = False
                else:
                    validtime = True
        except:
            print("Please enter the number of the time you would like.")    

    validemail = False
    while validemail == False:
        try:
            email = input("Please enter your email address so that I can contact you: ")
            if "@" not in email:
                print("This is not a valid email.")
            else:
                validemail = True
        except:
            print("Please try again.")

    booking = (name , str(entertainer[1]) , str(weekday[1]) , str(date[1]) , str(time[1]) , email)

    confirmedbook = False
    while confirmedbook == False:
        try:
            print("Here is your booking:")
            print(booking)
            confirm = input("Is this booking correct? Please confirm. Y/N ")
            if confirm == "N" or confirm == "n" or confirm == "No" or confirm == "NO" or confirm == "no":
                return
            elif confirm == "Y" or confirm == "y" or confirm == "Yes" or confirm == "YES" or confirm == "yes":
                confirmedbook = True
                booktestlist.append(booktest)
                if booking not in bookings:
                    bookings.append(booking)
                    duplicatelist.append(booking)
                else:
                    print("That seems to be a duplicate.")
            else:
                print("That isn't a valid answer.")
                continue
        except:
            print()

    showBookings()
                    
def adminDays():
    print("Here are the available booking dates")
    print()
    for Num,Day in weekdays: 
        print(Num,Day)
    print()
    validday = False
    while validday == False:
        try:
            daychoice = input("Which day would you like to view dates for? ")
            if daychoice == "quit" or daychoice == "Quit" or daychoice == "QUIT":
                perkHello()
            elif int(daychoice) < 1 or int(daychoice) > 7:
                 print("This number is not on the list.")
            else:
                blockweekday = weekdays[int(daychoice) - 1]
                validday = True
        except ValueError:
            print("Please enter the number of the day you would like to view dates for.")

    if str(blockweekday[1]) == "Monday":
        whichdates = mondaydates
    elif str(blockweekday[1]) == "Tuesday":
        whichdates = tuesdaydates
    elif str(blockweekday[1]) == "Wednesday":
        whichdates = wednesdaydates
    elif str(blockweekday[1]) == "Thursday":
        whichdates = thursdaydates
    elif str(blockweekday[1]) == "Friday":
        whichdates = fridaydates
    elif str(blockweekday[1]) == "Saturday":
        whichdates = saturdaydates
    elif str(blockweekday[1]) == "Sunday":
        whichdates = sundaydates

        
    print()
    print("Here are the dates for " , str(blockweekday[1]))
    print()

    for Num,Day in whichdates: 
        print(Num,Day)
    print()

    validdate = False
    while validdate == False:
        try:
            datechoice = input("Which date would you like to view times for? ")
            if datechoice == "quit" or datechoice == "Quit" or datechoice == "QUIT":
                adminHello()
            if int(datechoice) < 1 or int(datechoice) > 7:
                 print("This number is not on the list.")
            else:
                blockdate = whichdates[int(datechoice) - 1]
                validdate = True
        except ValueError:
            print("Please enter the number of the date you would like to view times for.")
    print()
    print("Here are the times for " , str(blockweekday[1]),"," , str(blockdate[1]))
    print()

    for Num,Time in times: 
        print(Num,Time)
    print()
    validtime = False
    while validtime == False:
        try:
            timechoice = input("Which time would you like to block? ")
            if timechoice == "quit" or timechoice == "Quit" or timechoice == "QUIT":
                adminHello()
            elif int(timechoice) < 1 or int(timechoice) > 15:
                 print("This number is not on the list.")
            else:
                blocktime = times[int(timechoice) - 1]
                print(str(blockweekday[1]) , str(blockdate[1]) , "," , str(blocktime[1]) , "has been blocked.")
                validtime = True
        except ValueError:
            print("Please enter the number of the time you would like.")
            
    booking = ("Admin", "BLOCKED DATE" , str(blockweekday[1]) , str(blockdate[1]) , str(blocktime[1]) , "BLOCKED DATE")
    booktest = (str(blockdate[1]), str(blocktime[1]))

    if booktest in booktestlist:
        print("Sorry, someone has already booked this time. Here are their details; you can either contact them about this, or remove their booking.")
        duplicatelist.append(booking)
        duplicate = [i for i, v in enumerate(duplicatelist) if v[3] == (str(blockdate[1])) or v[4] == str(blocktime[1])]
        print()
        i = 0
        for i in duplicate:
            print(duplicatelist[i])
            i = i + 1
        print()
        ValidRemoval = False
        while ValidRemoval == False:
            try:
                removebooking = input("Would you like to remove this person's booking? Y/N ")
                if removebooking == "N" or removebooking == "n" or removebooking == "No" or removebooking == "NO" or removebooking == "no":
                    ValidRemoval = True
                elif removebooking == "Y" or removebooking == "y" or removebooking == "Yes" or removebooking == "YES" or removebooking == "yes":
                    i = 0
                    for i in duplicate:
                        duplicatelist.remove(duplicatelist[i])
                        bookings.remove(bookings[i])
                        i = i + 1
                        ValidRemoval = True
                else:
                    print("That isn't a valid answer.")
                    continue
            except:
                print()
    else:
        booktestlist.append(booktest)
        if booking not in bookings:
            bookings.append(booking)
            duplicatelist.append(booking)
        else:
            print("You have already blocked this time.")
            
def adminHello():
    print()
    print("Hello, Admin")
    print("Here are the available options")
    print()
    for Num,Opt in adminoptions: 
        print(Num,Opt)
    print()
    adminvalid = False
    while parkvalid == False:
        try:
            adminchoice = int(input("Which option would you like to select? "))
            if adminchoice < 1 or adminchoice > 3:
                print("This number is not on the list.")
            else:
                adminvalid = True
        except ValueError:
            print("Please enter 1 to view bookings, 2 to block dates, or 3 to log out.")
        if adminchoice == 1:
            showBookings()
            adminHello()
        elif adminchoice == 2:
            adminDays()
            adminHello()
        else:
            AdminValidLogin = False
            return
            
def adminBooking():
    AdminValidLogin = False
    while AdminValidLogin == False:      
        try:
            password = input("Enter your password: ")
            if password == adminpass:
                AdminValidLogin = True
                adminHello()
            else:
                print("That's not the right password.")
        except:
            adminDays()
                
    

def endAnswer():
    ValidEndAnswer = False
    while ValidEndAnswer == False:
        endquestion = input("Would you like to make another booking? Y/N ")
        if endquestion == "N" or endquestion == "n" or endquestion == "No" or endquestion == "NO" or endquestion == "no":
            raise SystemExit()
        elif endquestion == "Y" or endquestion == "y" or endquestion == "Yes" or endquestion == "YES" or endquestion == "yes":
            ValidEndAnswer = True
        else:
            print("That isn't a valid answer.")
            continue
            
def showBookings():
    print()
    print("Here are the current bookings:")
    count = 0
    while count < len(bookings):
        print(bookings[count])
        count = count + 1
    if len(bookings) == 0:
        print("No bookings currently set.")
        print()
        



adminname = 'admin'
adminpass = "admin"

while 1==1:
    print()
    print("Welcome to Jurassick Perk booking system! Here you can choose an entertainer, then select a date and time. Say 'quit' at any time to exit the process.")
    print()
    name = input("What is your full name? ")
    if name == "quit" or name == "Quit" or name == "QUIT":
        endAnswer()
    elif name != adminname:
        makeBooking()
        endAnswer()                   
    else:
        adminBooking()
