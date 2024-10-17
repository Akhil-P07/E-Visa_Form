import mysql.connector as ms
from VisaAPP import visaAPP
database_name = 'summer_project'
mc = ms.connect(host = 'localhost', user = 'root', password = 'root', database = database_name)
if mc.is_connected:
    print("Connected! (◕‿◕✿)")
c = mc.cursor()

def spaces(n):
    if n % 2 == 0:
        n 
    else:
        n = n
    size = int((size - 13)/2)
    return n    


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



#Text Editor
class text:
    def __init__(s, text):
        s.text = text
        s.text_l = len(text)
    def printss1(s): #FOR HEADERS
        print("|" + " "*txt.size + "|")
        print("|" + s.text+ " "*(txt.size - s.text_l)  + "|")
    def printss2(s): #FOR SUBHEADERS
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + s.text+ " "*(txt.size - s.text_l)  + "|")
    def printss3(s): #FOR SUB-SUB HEADERS
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + " "*txt.size + "|")
        print("|" + s.text+ " "*(txt.size - s.text_l)  + "|")
    def printss4(s): #FOR QUERIES
        print("|" + " "*txt.size + "|")
        print("|     " + s.text+ " "*(txt.size - s.text_l - 5)  + "|")
    def printsn_l(s): #FOR INPUT Left aligned
        print("|" + " "*txt.size + "|")
        print("   " + s.text, end ="")
        i = int(input(""))
        return i
    
txt = headertxt(121, "INDIAN E-VISA PORTAL") #101
print("|" + "-"*txt.size + "|")
print("|" + " "*txt.size + "|")
print("|" +" "*txt.spaces + txt.txt + " "*txt.spaces + "|")
print("|" + " "*txt.size  + "|")
print("|" + "-"*txt.size  + "|")

c.execute("create table if not exists visaAPP (passportType varchar(30) NOT NULL, nationality varchar(30) NOT NULL, portOfArrival varchar(30) NOT NULL, portOfexit varchar(30) NOT NULL, DOB date NOT NULL, emailID varchar(50) NOT NULL, dateOfArrival date NOT NULL, surname varchar(30) NOT NULL, passportName varchar(30) NOT NULL,changedName char(1) NOT NULL, gender char(1) NOT NULL, townCityOfBirth varchar(30) NOT NULL, countryOfBirth varchar(30) NOT NULL, citizenshipOrNationalID varchar(30) NOT NULL, relgion varchar(30) NOT NULL, visibleMarks varchar(50) NOT NULL, education varchar(40) NOT NULL, nationalityByBirthOrNaturalization char(1) NOT NULL, Livedfor2yinCountry char(1) NOT NULL, passportNo char(15) NOT NULL, placeOfIssue varchar(30) NOT NULL, dateOfIssue date NOT NULL, dateOfExpire date NOT NULL, houseNo varchar(30) NOT NULL, villageTownCity varchar(30) NOT NULL, country varchar(30) NOT NULL, state varchar(30) NOT NULL, postalOrZip varchar(15) NOT NULL,countryCode1 varchar(5) NOT NULL, phoneNo int(30) NOT NULL, CountryCode2 varchar(5) NOT NULL, mobileNo int NOT NULL, permHouseAddress varchar(100) NOT NULL, permVillageTownCity varchar(30) NOT NULL, permState varchar(30) NOT NULL, fatherName varchar(30) NOT NULL, fatherNationality varchar(30) NOT NULL, fatherFormerNationality varchar(30) NOT NULL, fatherPOB varchar(30) NOT NULL, fatherCountryOfBirth varchar(30) NOT NULL, motherName varchar(30) NOT NULL, motherNationality varchar(30) NOT NULL, motherFormerNationality varchar(30) NOT NULL, motherPOB varchar(30) NOT NULL, motherCountryofBirth varchar(30) NOT NULL, maritialStatus varchar(15) NOT NULL, pakistaniParentsGrandparents char(1) NOT NULL, pakistaniParentsGrandparentsDetails varchar(30) NOT NULL, placesvisited varchar(70) NOT NULL,  bookedRoom char(1) NOT NULL, visaDurationinDays int NOT NULL, visitedIndiaBefore char(1) NOT NULL, prevVisaCities varchar(30) NOT NULL, prevVisaNo varchar(30) NOT NULL, prevVisaType varchar(30) NOT NULL, prevVisaPlaceOfIssue varchar(30) NOT NULL, prevVisadateOfIssue date NOT NULL, prevPermissionVisa char(1) NOT NULL, prevWhoReject varchar(30) NOT NULL, countriesVisitedLast10yrs varchar(100) NOT NULL, vistedSAARC char(1) NOT NULL, refNameInd varchar(30) NOT NULL, refAddressInd varchar(100) NOT NULL, refcountryCodeInd varchar(5) NOT NULL, refPhoneInd varchar(30) NOT NULL, refNameHomeCountry varchar(30) NOT NULL, refaddressHomeCountry varchar (100) NOT NULL,refPhoneHomeCountryCountryCode char(5 )NOT NULL, refPhoneHomeCountry int NOT NULL, q1 char(1) NOT NULL, q2 char(1) NOT NULL, q3 char(1) NOT NULL, q4 char(1) NOT NULL, q5 char(1) NOT NULL, q6 char(1) NOT NULL);")
c.execute(visaAPP())
mc.commit()