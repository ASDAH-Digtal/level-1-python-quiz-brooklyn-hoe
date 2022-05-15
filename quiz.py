print("welcome to the anime quiz. this quiz is about animes. so lets test your anime knowledge.")

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


