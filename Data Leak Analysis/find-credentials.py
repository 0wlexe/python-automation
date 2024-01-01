''' 
Purpose: Extract Email Addresses from a data leak using a domain 
Reference: https://www.computerhope.com/issues/ch001721.htm
Last Modification: 01/01/2024
'''
# Declare empty list to store the credentials
credentials = []
linenum = 0
# Sub string to researched 
subster = "domain.com".lower() 
# Open file for rt - reading text 
with open ('leak-example.txt', 'rt') as myfile:
    # Conditional for each line in the file 
    for line in myfile:
        # Strip a new line and add to credentials list
        linenum += 1
        # See if case-insesitive sub string match and add to list
        if line.lower().find(subster) != -1:
            credentials.append(str(linenum) + line.rstrip('\n'))
for emails in credentials:
    print(emails)

