import re

# +977-985******* Nepal Telecom
# +977-986******* Nepal Telecom
# +977-984******* Nepal Telecom 
# +977-980******* Ncell 
# +977-981******* Ncell
# +977-982******* Ncell
# +977-961******* SmartCell 
# +977-962******* SmartCell 
# +977-988******* SmartCell


user_details = input("Hey! What's your phone number?\n")

def carrier_detect(carrier):
    carrier = int(carrier)
    if (carrier == 980) or (carrier == 981) or (carrier == 982) :
        return 'Ncell'

    elif (carrier == 984) or (carrier == 986):
        return 'Nepal Telecom (Pre-Paid)'

    elif carrier == 985):
        return 'Nepal Telecom (Post-Paid)'

    elif (carrier == 961) or (carrier == 988) :
       return'SmartCell'

phone_num_regex = re.compile(r'(\+)?(\d\d\d)?(-)?(\d\d\d)\d\d\d\d\d\d\d')
num = phone_num_regex.search(user_details)

carrier_part = num.group(4)

print('Your mobile number is', num.group())
print('Your carrier is', carrier_detect(carrier_part))