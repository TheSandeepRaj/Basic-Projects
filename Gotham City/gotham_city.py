'''You are a police officer, and you get a report of criminal activity! Should you go on your own,
or should you call a superhero to help you fight the crime? If there are less than 5,
you can handle this on your own, if there are 5-10, you will want to go with Batman for backup,
and if there are more than 10, you should stay where it is safe and let Batman handle this on his own!'''

criminal_report = input('Enter total number of criminals : ')

if criminal_report < 5:
    print('Okay! I got this.')

elif 5 <= criminal_report <= 10:
    print('Hey Batman I need your help.')
else:
    print('Good luck Batman! You need to handle this case.')