print("Welcome to the Love Calculator!")
# Input the names
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# combine names to one string and lower all letters
combinedname = (name1 + name2).lower()

# count the numbers of true and build the sum true
t = combinedname.count("t")
r = combinedname.count("r")
u = combinedname.count("u")
e = combinedname.count("e")
true = t + r + u + e
# count the numbers of love and build the sum love
l = combinedname.count("l")
o = combinedname.count("o")
v = combinedname.count("v")
e = combinedname.count("e")
love = l + o + v + e
#combine 2 strings and convert them into integer
truelove_int = int(str(true) + str(love))
# truelove_str = str(true) + str(love)
# truelove_int = int(truelove_str)
# simple IF-case
if truelove_int < 10 or truelove_int > 90:
  print(f"Your score is {truelove_int} You Suck")
elif truelove_int >= 40 and truelove_int <= 50:
  print(f"Your score is {truelove_int} perfect")
else: 
  print (f"Your score is {truelove_int}")
