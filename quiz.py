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

#Question 6
q6 = input("Question 6) which anime character is weaker? \n Light Yagami \n Jin Mori \n Ussop \n Sakura").lower()

if q6 == "light yagami":
    print("Thats correct you get one point")
    score += 1
elif q6 == "jin mori" or q6 == "Ussop" or q6 == "Sakura":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 7
q7 = input("Question 7)how many episode are in one piece? \n 1000 \n 900 \n 500 \n Neither Its Still going").lower()

if q7 == "neither its still going":
    print("Thats correct you get one point")
    score += 1
elif q7 == "1000" or q7 == "900" or q7 == "500":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 8
q8 = input("Question 8) who is a swordman out of thease characters? \n Kuroko \n Yami \n Loid \n Asta").lower()

if q8 == "asta":
    print("Thats correct you get one point")
    score += 1
elif q8 == "kuroko" or q8 == "yami" or q8 == "loid":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 9
q9 = input("Question 9) which anime cost more to make? \n One Piece \n Pokemon \n Demon Slayer \n Jujustu Kaisen").lower()

if q9 == "pokemon":
    print("Thats correct you get one point")
    score += 1
elif q9 == "one piece" or q9 == "demon slayer" or q9 == "jujustu kaisen":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1

#Question 10
q10 = input("Question 10) which anime is a action genre?  \n Kurokos Basketball \n Attack On Titans \n Jujustu Kaisen \n Death Note").lower()

if q10 == "jujustu kaisen":
    print("Thats correct you get one point")
    score += 1
elif q10 == "kurokos basketball" or q10 == "attack on titans" or q10 == "death note":
    print("Incorrect you lose one point")
    score -= 1
else:
    print("Sorry thats not an option")
    score -= 1