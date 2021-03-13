# Ferramenta para o rastreio de numeros telefonicos

import phonenumbers

from phonenumbers import geocoder

phone = input("Insert a phone number in format +551148828922: ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
