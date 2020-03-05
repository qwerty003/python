def movie(i):
    if i==1:
        print("Actors are : Ayushmann khurana, Nushrat Barucha")
    elif i==2:
        print("Actors are : Ranveer Singh, Alia Bhatt")
    else:
        print("Actors are : Hrithik Roshan, Priyanka Chopra, Vivek Oberoi")
def hint(i):
    if i==1:
        print("A guy works in a call center as a girl named pooja.")
    elif i==2:
        print("Real life struggle of indian rappers Divine and Nucleya")
    else:
        print("A superhero movie in which hero faces a genetically engineered villain")
def guess(i):
    q = input("Enter your answer : ")
    if i == 1 and q == "dream girl":
        print("correct")
    elif i == 2 and q == "gully boy":
        print("correct")
    elif i == 3 and q == "krish 3":
        print("correct")
    else:
        print("incorrect")
print("Guess the movie")
p=1
while p<=3:
     movie(p)
     print("1. Make a guess\n2.Ask for the hint\n3.Quit the game")
     x=int(input("Enter your choise : "))
     if x==1 :
         guess(p)
     elif x==2:
         hint(p)
         guess(p)
     else:
         print("You Quit the game")
         break
     p+=1



