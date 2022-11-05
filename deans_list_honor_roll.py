#Tom Banis
#deans_list_honor_roll
#To test if a student's GPA qualifyes for the Dean's List or Honor Roll



lastName = input("Enter the students last name or enter 'ZZZ' to quit: ")



  
while True:
    if lastName == 'ZZZ':
        break
    firstName = input("Enter students first name: ")
    gpaString = input("Enter the student's GPA: ")
    gpaFloat = float(gpaString)

    if gpaFloat >= 3.5:
        print("{} {} has made the Dean's List!".format(firstName, lastName))
    elif gpaFloat >= 3.25:
        print("{} {} has made the Honor Roll!".format(firstName, lastName))
    else:
        print("{} {} has not made either the Dean's List or Honor Roll".format(firstName, lastName))

    lastName = input("Enter the students last name or enter 'ZZZ' to quit: ")


    

