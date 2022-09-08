import phonenumbers
from phonenumbers import geocoder #import geocoder

#specify then phone number
a = input('Enter the phone number: ')
phonenumber = phonenumbers.parse(a)

#display the location of the phone number
print(geocoder.description_for_number(phonenumber, 'en'))