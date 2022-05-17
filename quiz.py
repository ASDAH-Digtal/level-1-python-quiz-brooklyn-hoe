#introduction
print("welcome to the anime quiz. this quiz is about animes. so lets test your anime knowledge.")

#Question 1
score = 0
q1 = input("Question 1)What is the most popular anime? \n One Piece \n Naruto \n Dragon Ball \n Fullmetal Alchemist").lower()

if q1 == "dragon ball":
    print("thats correct you get one point")
    score += 1
elif q1 == "one piece" or q1 == "naruto" or q1 == "fullmetal alchemist":
    print("incorrect")
    score -= 1
else:
    print("sorry that is not an option")
    score -= 1

#Question 2
q2 = input(" Question 2)Which anime character is stronger? \n Luffy \n Naruto \n Asta \n Itadori").lower()

if q2 == "luffy":
    print("thats correct you get one point")
    score += 1
elif q2 == "naruto" or q2 == "asta" or q2 == "itadori":
    print("Incorrect you lose a point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 3
q3 = input(" Question 3) Which anime has the most episode? \n Dragon Ball \n Death Note \n Black Clover \n Fullmetal Alchemist").lower()

if q3 == "black clover":
    print("Thats correct you get one point")
    score += 1
elif q3 == "dragon ball" or q3 == "death note" or q3 == "fullmetal alchemist":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 4
 q4 = input(" Question 4) Who died first out of thease characters from naruto? \n Itachi \n Jiraiya \n Rin \n Kurama").lower()

if q4 == "rin":
    print("Thats correct you get one point")
    score += 1
elif q4 == "itachi" or q4 == "jiraiya" or q4 == "kurama":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 5
q5 = input(" Question 5) Who are the current four yonkos? \n Shanks, Big Mom, Kaido, Black Beard \n Shanks, Black Beard, Luffy, Kaido \n Naruto, Sasuke, Sakura, Kakashi \n Kaido, whitebeard, Big mom, Shanks").lower()

if q5 == "shanks, big Mom, kaido, black beard":
    print("Thats correct you get one point")
    score += 1
elif q5 == "Shanks, Black Beard, Luffy, Kaido" or q5 == "naruto, saskue, sakura, kakashi" or q5 == "kaido, whitebeard, big mom, shanks":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1



