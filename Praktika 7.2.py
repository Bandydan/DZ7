Python = {'Ivanov', 'Sidorov', 'Balanov'}
Java = {'Zaharchenko', 'Vinichenko', 'Shevchenko'}
Frontend = {'Kish', 'Ivanov', 'Losenko'}
Fullstack = {'Kish', 'Logvinenko', 'Egorov'}
a = (Python & Java,  Frontend & Fullstack, Python & Frontend, Python & Fullstack, Java & Fullstack,
      Java & Frontend)
b = list(filter(None, a))
print("Cтуденты, которые учаться в двух или более групах", b)
print("Cтуденты, которые не учатся на Frontend:", set(Python | Java | Fullstack) - Frontend)
print("Студенты, которые изучают Java или Python,", " Java: ", Java - set(Python | Frontend | Fullstack),
      " Python: ", Python - set(Java | Frontend | Fullstack))