#--------------
#Prepare the Student Roster,Let's create a new register by combining data from two classes while making some modifications to the register.
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
print(new_class.append('Peter Warden'),new_class)
print(new_class.remove('Carla Gentry'),new_class)
# Code ends here


# --------------
#Grade Please,Let's create a dictionary for Geoffrey Hinton in each subject to generate his progress report.
#code starts here
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
marks=courses.values()
print(marks)
total=sum(marks)
print(total)
percentage=total/500*100
print(percentage)
# Code ends here


# --------------
# Kudos to the Math Genius!For the student who got the highest marks in this subject, the school has decided to award a scholarship.
#Let's check who performed best in mathematics from all the students who appeared for the test.
# Code starts here
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)
# Code ends here  


# --------------
#Scholarship Certificate,From the previous task, we know who is the 'Maths' topper in the class. You now have to print the name of the student on the certificate, but you will have to print his last name and then his first name.
# Code starts here
topper = 'andrew ng'
first_name=topper.split()[0]
print(first_name)
last_name=topper.split()[1]
print(last_name)
full_name='ng '+'andrew'
print(full_name)
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here
