fruits =["Apple", "Peach", "Pear"]
for fruit in fruits:   #weißt jedem Element aus der Liste fruits die variable fruit zu so lange bis alle durch sind und jedes ausgegeben wurde.
    print(fruit)
    print(fruit + " Pie")
    print(fruits)  #auf Einrückung (Intendation) achten. hier würde dann 3 mal die ganze liste nach jedem der anderen prints
                   #ausgegeben werden. Ohne Einrückung nach der for Schleife nur einmal.

#AverageStudentHeight
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height_sum = 0
for height in student_heights:
  height_sum += height
items = 0
for students in student_heights:
    items += 1

result = round(height_sum/items)
print(result)

#HighScore Coding Challenge
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score=0
for score in student_scores:
    if score > highest_score:
       highest_score = score
print(f"The highest score in the class is: {highest_score}")

#for loops with range() function

for number in range(1, 10):
    print(number)

for number in range(1, 11):
    print(number)

for number in range(1, 11, 3):
    print(number)

#Gauss
total=0
for number in range(1, 101):
    total += number
print(total)

#Gauss nur mit geraden Zahlen
total=0
for number in range(2,101,2):
    total += number
print(total)

#Möglichkeit 2:
total2=0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)

#Nummern tauschen Wiederholung
a=5
b=2
print(a, b)
c=a
a=b
b=c
print(a, b)

#FizzBuzz

for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
chosen_letters = []
for letter in range(nr_letters):
    l = random.randint(0, len(letters)-1)
    chosen_letters.append(letters[l])
chosen_symbols = []
for symbol in range(nr_symbols):
    s = random.randint(0, len(symbols)-1)
    chosen_symbols.append(symbols[s])
    #chosen_symbols.insert(symbol, symbols[s])
chosen_numbers = []
for number in range(nr_numbers):
    n = random.randint(0, len(numbers)-1)
    chosen_numbers.append(numbers[n])
sum_char = nr_letters+nr_symbols+nr_numbers
password = (chosen_letters+chosen_symbols+chosen_numbers) #letters = 0, symbols = 1, numbers = 2
print(password)
random.shuffle(password)
#empty_string = ""   #kann auch jeglicher anderer string sein, muss nicht leer sein. der angegebene string verbindet die Listenobjekte. Wäre er zb. P oder ein Leerzeichen wäre es 0P1,...oder 0 1  (Index der Liste, das auf entsprechendes Objekt in der Liste verweist)
#final_password=empty_string.join(password)  #oder wie unten in einer Zeile: str() kreiert einen leeren String
#final_password = str().join(password)
#oder
final_password = str.join("", password) #wäre auch mit for loop möglich final_password="", for item in password: final_password += item (string concatenation)
print(final_password)