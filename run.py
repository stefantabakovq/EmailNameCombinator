"""
Author: Stefan Tabakov 2021

--------------------------------------------------------
Email name combinator, taking domain name + CSV of names
for conversion, Console application
--------------------------------------------------------
"""

import os
from DataLoader import DataLoader


def import_from_file(nDf, dDf):
    print("--------------------------------------------------------------------------")
    print(f"Loaded {len(nDf.index)} names and {len(dDf.index)} domains")
    print(" ________ NOT IMPLEMENTED YET, PLEASE USE MANUAL INPUT FROM MENU !!!!!!!!!")
    return


def use_manually(nDf):
    print("--------------------------------------------------------------------------")
    print(f"Loaded {len(nDf.index)} names")
    print("Enter row number of person data")
    row = 1
    while 1:
        row = int(input())
        if row <= 0:
            print("Row number is invalid! Please enter valid row number....")
        else:
            break

    "User will prefer 1-inf than 0-inf"
    row -= 1
    print("Enter domain name without @ sign (example: instagram.com) person data")
    domain = "domain.com"
    while 1:
        domain = str(input())
        if "." not in domain:
            print("Domain is invalid! Please enter valid domain like google.com")
        else:
            break

    firstName = nDf.iloc[row, 2]
    lastName = nDf.iloc[row, 3]
    print(f"Creating combinations for {firstName} {lastName}")

    emails = [f"{firstName.lower()}.{lastName.lower()}@{domain}",
              f"{firstName.lower()}_{lastName.lower()}@{domain}",
              f"{firstName[0].upper()}{firstName[1:].lower()}{lastName.lower()}@{domain}",
              f"{firstName[0].upper()}.{lastName.lower()}@{domain}",
              f"{firstName[0].upper()}_{lastName.lower()}@{domain}",
              f"{firstName[0].upper()}{lastName.lower()}@{domain}",
              f"{lastName[0].upper()}{lastName[1:].lower()}{firstName.lower()}@{domain}",
              f"{lastName[0].upper()}{lastName[1:].lower()}.{firstName.lower()}@{domain}",
              f"{lastName[0].upper()}{lastName[1:].lower()}_{firstName.lower()}@{domain}",
              f"{lastName[0].upper()}{lastName[1:].lower()}{firstName[0].lower()}@{domain}",
              f"{lastName[0].upper()}{lastName[1:].lower()}.{firstName[0].lower()}@{domain}",
              f"{lastName[0].upper()}{lastName[1:].lower()}_{firstName[0].lower()}@{domain}"]
    print(*emails, sep=', ')
    return


loader = DataLoader()

"""
Load data and chose method for combining
"""
while 1:
    namesDf = loader.load_names_data()
    if namesDf is None:
        break

    else:
        print("--------------------------------------------------------------------------")
        print("Import domains from file, or enter company or domain manually?\n")
        print("Enter 'M' or 'm' for manual entry, or press ENTER for importing from file.\n")
        print("--------------------------------------------------------------------------\n")
        choice = str(input())
        if choice == "M" or choice == "m":
            use_manually(nDf=namesDf)
        else:
            domainsDf = loader.read_domains_data()
            if domainsDf is None:
                break
            import_from_file(nDf=namesDf, dDf=domainsDf)
        print("Enter R to repeat or press ENTER to exit")
        retry = str(input())
        if retry == "R" or retry == "r":
            pass
        else:
            break

print("Exiting program...\n")
print("--------------------------------------------------------------------------\n")
print("Author: Stefan Tabakov")
print("2021")
