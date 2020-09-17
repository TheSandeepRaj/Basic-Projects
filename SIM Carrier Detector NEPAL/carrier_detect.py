import re

# +977-985******* Nepal Telecom
# +977-986******* Nepal Telecom
# +977-984******* Nepal Telecom 
# +977-980******* Ncell 
# +977-981******* Ncell
# +977-982******* Ncell
# +977-961******* SmartCell (maybe)
# +977-988******* SmartCell (maybe)
user_details = input("Hey! What's your phone number?\n")

def carrier_detect(carrier):
    carrier = int(carrier)
    if (carrier == 980) or (carrier == 981) or (carrier == 982) :
        return 'Ncell'

    elif (carrier == 984) or (carrier == 985) or (carrier == 986):
        return 'Nepal Telecom'

    elif (carrier == 961) or (carrier == 988) :
       return'SmartCell'

phone_num_regex = re.compile(r'(\+)?(\d\d\d)?(-)?(\d\d\d)\d\d\d\d\d\d\d')
num = phone_num_regex.search(user_details)

carrier_part = num.group(4)

print('Your mobile number is', num.group())
print('Your carrier is', carrier_detect(carrier_part))