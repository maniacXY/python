year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 != 0:
    print ("Schaltjahr")
  else:
    if year % 400 != 0:
      print ("kein Schaltjahr")
    else:
      print ("Schaltjahr")

else:
  print ("kein Schaltjahr")


