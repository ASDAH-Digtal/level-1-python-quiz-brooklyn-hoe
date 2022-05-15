#introduction
print("welcome to the anime quiz. this quiz is about animes. so lets test your anime knowledge.")

#Question 1
score = 0
q1 = input("Question 1)What is the most popular anime? \n One Piece \n Naruto \n Dragon Ball \n Fullmetal Alchemist.")

if q1 == "Dragon ball":
    print("thats correct you get one point")
    score += 1
elif q1 == "One piece" or q1 == "Naruto" or q1 == "Fullmetal Alchemist":
    print("incorrect")
    score -= 1
else:
    print("sorry that is not an option")
    score -= 1

#Question 2
q2 = input(" Question 2)Which anime character is stronger? \n Luffy \n Naruto \n Asta \n Itadori.")

if q2 == "Luffy":
    print("thats correct you get one point")
    score += 1
elif q2 == "Naruto" or q2 == "Asta" or q2 == "Itadori":
    print("Incorrect you lose a point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 3
q3 = input(" Question 3) Which anime has the most episode? \n Dragon Ball \n Death Note \n Black Clover \n Fullmetal Alchemist.")

if q3 == "Black Clover":
    print("Thats correct you get one point")
    score += 1
elif q3 == "Dragon Ball" or q3 == "Death Note" or q3 == "Fullmetal Alchemist":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1



