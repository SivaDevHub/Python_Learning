SurName= "Kotigari"
FirstName= "Siva"
LastName= "Reddy"

print("Name: " + SurName + " " + FirstName + " "+ LastName)

FullName = SurName + " " + FirstName + " "+ LastName

print("Full-Name: "+ FullName)

length = len(FullName)

print("Lenght:", length)

print("Lower case :", FullName.lower())

print("upper case :", FullName.upper())

Replace_SurName = SurName.replace("Kotigari", "k")

print("Name: " + Replace_SurName + " " + FirstName + " "+ LastName)

Split_FullName = FullName.split()

print("Split Name :", Split_FullName)


text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

AWS = "It's AWS Cloud Provider"

substring = "DC"

if substring in AWS:
    print("Its Cloud Provider")
else:
    print("Its not DC")

substring2 = "Cloud"

if substring2 in AWS:
    print("Its Cloud Provider")