countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", 
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", 
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", 
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", 
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", 
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", 
    "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", 
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "Indonesia", "Iran", 
    "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", 
    "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", 
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", 
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", 
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", 
    "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", 
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", 
    "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", 
    "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", 
    "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]
#E-VISA PORTAL HEADER
class headertxt:
    def __init__(self, size, txt):
        self.size = size #only odd values
        self.txt = txt
        txt_l = len(self.txt)
        if txt_l%2 == 0:
            self.txt += " "
            txt_l = len(self.txt)
        self.spaces = int((size - txt_l)/2)
        
txt = headertxt(121, "INDIAN E-VISA PORTAL")
#Text Editor
class text:
    def __init__(s, text):
        s.text = text
        s.text_l = len(text)
    def printss1(s): #FOR HEADERS
        print("|" + " "*txt.size + "|")
        print("|" + s.text.title() + " "*(txt.size - s.text_l)  + "|")
    def printss2(s): #FOR SUBHEADERS
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + s.text.title() + " "*(txt.size - s.text_l)  + "|")
    def printss3(s): #FOR SUB-SUB HEADERS
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + s.text+ " "*(txt.size - s.text_l)  + "|")
    def printss4(s): #FOR QUERIES OPTIONS
        print("|" + " "*txt.size + "|")
        print("|     " + s.text+ " "*(txt.size - s.text_l - 5)  + "|")
    def printsnl(s): #FOR INPUT Left aligned Numeric
        print("|" + " "*txt.size + "|")
        print("   " + s.text, end ="")
        i = int(input(""))
        return i
    def printssl(s): #FOR INPUT Left aligned Alphabetic
        print("|" + " "*txt.size + "|")
        print("   " + s.text, end ="")
        i = input("").title().rstrip().lstrip()
        return i
    def printssy_n(s): #FOR INPUT YES OR NO
        i = -1
        while i != "Y" and i != "N":  
            print("|" + " "*txt.size + "|")
            print("|     " + "Yes -> Enter Y"+ " "*(txt.size - len("Yes -> Enter Y") - 5)  + "|")
            print("|" + " "*txt.size + "|")
            print("|     " + "No -> Enter N"+ " "*(txt.size - len("No -> Enter N")- 5)  + "|")
            print("|" + " "*txt.size + "|")
            print("   " + s.text, end ="")
            i = input("").title().rstrip().lstrip()
        return i
def visaAPP():
    user = list()
    choice = 0

    ptypes = ["1. Ordinary Passport", "2. Official Passport", "3. Diplomatic Passport","4. Service Passport", "5. Special Passport"]
    for i in ptypes:
        text1 = text(i)
        text1.printss4()
    while choice not in range(1,6):
        text1 = text("Choose passport type number: ")
        choice = text1.printsnl()
    user.append(ptypes[choice-1][3:])
    choice = 0 
    while choice not in countries:
        text1 = text("Enter your Nationality: ")
        choice = text1.printssl().title()
        print(choice)
        if choice == "India":
            print("Visa not required")
        elif choice not in countries:
            print("Country not found")
        

    user.append(choice)
    text1 = text("Enter your Port of arrival: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Enter your Port of exit: ")
    choice = text1.printssl()
    user.append(choice)
    
    text1 = text("Enter your Date of Birth(DD/MM/YYYY): ")
    choice = text1.printssl()
    user.append(choice[-4:] + "/" + choice[3:5] + "/" + choice[0:2])

    text1 = text("Enter your Email ID: ")
    choice = text1.printssl()
    user.append(choice.lower())
    
    text1 = text("Enter your expected Date of Arrival(DD/MM/YYYY):")
    choice = text1.printssl()
    user.append(choice[-4:] + "/" + choice[3:5] + "/" + choice[0:2])

    text1 = text("Applicant Details")
    text1.printss2()

    text1 = text("Enter your Surname (exactly as in your passport): ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Enter your Given Name/s (exactly as in your passport): ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Have you ever changed your name?: ")
    choice = text1.printssy_n()
    user.append(choice)

    choice = 0
    while choice != "M" and choice != "F" and choice != "N" :
        text1 = text('Male -> Enter M')
        text1.printss4()

        text1 = text('Female -> Enter F')
        text1.printss4()

        text1 = text('None of the above -> Enter N')
        text1.printss4()
        
        
        text1 = text("Enter your Gender: ")
        choice = text1.printssl()
    user.append(choice)
    for i in ["Enter City of Birth: ", "Enter Country of Birth: ", "Enter Citizenship/National ID no.: ", 
              "Enter your religion: ","Enter visible identification marks(Enter N/A if no identification marks present): ",
              "Enter your Educational Qualification(if multiple then separate them with comma(,)): ",
               ]:
        text1 = text(i)
        choice = text1.printssl()

        if i == "Enter Country of Birth: ":
            while choice not in countries:
                text1 = text(i)
                choice = text1.printssl().title()
        user.append(choice)
        
    text1 = text("Nationality: " + user[1])
    text1.printss2()

    text1 = text('By birth -> Enter B')
    text1.printss4()

    text1 = text('By naturalization -> Enter N')
    text1.printss4()

    text1 = text("Did you aquire nationality by birth or by naturalization?: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Have you lived for atleast two years in the country where you are applying visa?: ")
    choice = text1.printssy_n()
    user.append(choice)
    
    text1 = text("Passport Details")
    text1.printss2()
    
    text1 = text("Passport Number: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Place of Issue: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Date of Issue: ")
    choice = text1.printssl()
    user.append(choice[-4:] + "/" + choice[3:5] + "/" + choice[0:2])

    text1 = text("Date of Expiry of Issue: ")
    choice = text1.printssl()
    user.append(choice[-4:] + "/" + choice[3:5] + "/" + choice[0:2])

    text1 = text("Applicant's Address Details")
    text1.printss2()
    
    text1 = text("Present address")
    text1.printss3()

    for i in ["House No./Street: ", "Village/Town/City: ",  #10,9,8
              "State/Province/District: ", "Country: ", "Postal/ZipCode: ", 
              "Enter Phone no. Country Code: "]:
        text1 = text(i)
        choice = text1.printssl()
        user.append(choice)
        text1 = text("Enter Phone no.: ")
    choice = text1.printsnl()
    user.append(choice)

    text1 = text("Enter Mobile no. Country Code: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Enter Mobile no.: ") 
    choice = text1.printsnl()
    user.append(choice)

    text1 = text("Enter Email Address: ")
    choice = text1.printssl()
    user.append(choice)
    
    text1 = text("Is your Permanent Address same as your Present Address:")
    choice = text1.printssy_n()
    if choice == "Y":
        user.append(user[-10])
        user.append(user[-9])
        user.append(user[-8])
    else:
        text1 = text("Permanent address")
        text1.printss3()
        for i in ["House No./Street: ", "Village/Town/City: ",
              "State/Province/District: "]:
            text1 = text(i)
            choice = text1.printssl()
            user.append(choice)
            

    text1 = text("Family Details")
    text1.printss2()
    
    text1 = text("Father's Details")
    text1.printss3()

    for i in ["Name: ", "Nationality: ", "Previous Nationality(Enter N/A if not applicable): ", 
              "Place of Birth: ", "Country of Birth: "]:
        if i == "Country of Birth: ":
            while choice not in countries:
                text1 = text(i)
                choice = text1.printssl()
                if choice not in countries:
                    print("Country not found")
        else:
            text1 = text(i)
            choice = text1.printssl()
            user.append(choice)
        
    text1 = text("Mother's Details")
    text1.printss3()

    for i in ["Name: ", "Nationality: ", "Previous Nationality(Enter N/A if not applicable): ", 
              "Place of Birth: ", "Country of Birth: "]:
        if i == "Country of Birth: ":
            while choice not in countries:
                text1 = text(i)
                choice = text1.printssl()
                if choice not in countries:
                    print("Country not found")
        else:
            text1 = text(i)
            choice = text1.printssl()
            user.append(choice)
        

    choice = 0
    while choice not in ["Divorced", "Married", "Single", "Widowed"]:
        for i in ["Divorced", "Married", "Single", "Widowed"]:
            text1 = text(i)
            text1.printss4()
        text1 = text("Applicant's Maritial Status: ")
        choice = text1.printssl()
        if choice not in ["Divorced", "Married", "Single", "Widowed"]:
            print("Choose one the given choices")
    user.append(choice)

    text1 = text("Were your Parents/Grandparents(Paternal or Maternal) Pakistan National or Belong to Pakistan Held area.: ")
    choice = text1.printssy_n()
    user.append(choice)
    
    text1 = text("If yes then give details(Else Enter N/A): ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Details of Visa Sought")
    text1.printss2()

    text1 = text("Type of Visa: e-Visa")
    text1.printss1()

    text1 = text("Visa Service: eTourist Visa")
    text1.printss1()

    text1 = text("Places to be Visited(if multiple then separate with commas eg. Raipur, Jaipur): ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Have you booked any room in Hotel/Resort etc. through any Tour Operator?: ")
    choice = text1.printssy_n()
    user.append(choice)

    text1 = text("Visa Duration: 365 days")
    text1.printss1()
    user.append(365)

    text1 = text("No. of Entries: Multiple")
    text1.printss1()

    text1 = text("Port of Arrival in India: %s"%(user[2]))
    text1.printss1()

    text1 = text("Expected Port of Exit from India: %s"%(user[3]))
    text1.printss1()

    text1 = text("Previous Visa/Currently valid Visa Details")
    text1.printss2()

    text1 = text("Have your ever visited india before?: ")
    choice = text1.printssy_n()
    user.append(choice)
    if choice == "Y":
        for i in ["Address of stay during last visit: ", "Cities previously visited in india: ",
                   "Last indian Visa No./ Currently Valid Indian Visa No.: ", "Type of visa: ", "Place of issue: ", 
                   "Date of issue: "]:
            text1 = text(i)
            choice = text1.printssl()
            user.append(choice)
        text1 = text("Has permission to visit or to extend stay in India previously been refused?: ")
        choice = text1.printssy_n()
        user.append(choice)
        text1 = text("If so, when and by whom (Mention Control No. and date also: ")
        choice = text1.printssl()
        user.append(choice)
    else: 
        for i in range(8):
            user.append("N/A")

    text1 = text("Other Information")
    text1.printss2()

    text1 = text("Countries visited in the Last 10 years: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("SAARC Country Visit Details: ")
    text1.printss2()

    text1 = text("Have you visited SAARC countries (except your own country) during last 3 years?")
    choice = text1.printssy_n()
    user.append(choice)

    text1 = text("Reference")
    text1.printss2()

    text1 = text("Reference Name in India: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Address: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Phone no. Country code: ")
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Phone no.: ")
    choice = text1.printsnl()
    user.append(choice)

    text1 = text("Reference name in %s: "%(user[1]))
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Address in %s: "%(user[1]))
    choice = text1.printssl()
    user.append(choice)


    text1 = text("Phone no. Country code in %s: "%(user[1]))
    choice = text1.printssl()
    user.append(choice)

    text1 = text("Phone no. in %s: "%(user[1]))
    choice = text1.printsnl()
    user.append(choice)

    text1 = text("Additional Question Details")
    text1.printss1()
    for i in ["Have you ever been arrested/ prosecuted/ convicted by the Court of Law of any country?: ",
              "Have you ever been refused entry/ deported by any country including india?: ",
              "Have you ever been engaged in Cyber crime/ Terrorist activities/ Sabotage/ Espionage/ Genocide/ Political killing/ Other acts of violence?: ",
              "Have you ever by any means or medium, expressed views that justify or glorify terrorist violence or that may encourage others to terrorist acts or other serious criminal acts: ",
              "Have you sought asylum(Political or otherwise) in any country?: "]:
        text1 = text(i)
        choice = text1.printssy_n()
        user.append(choice)
    insertStatement = "INSERT INTO visaAPP Values("
    for i in user:
        if isinstance(i, str):
            insertStatement += '"'+str(i) + '"' + ", "
        elif isinstance(i, int):
            insertStatement += str(i) + ", "
    insertStatement = insertStatement[:-2] + ");"
    return insertStatement
