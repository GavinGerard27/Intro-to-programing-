def tally_score(ans1, ans2, ans3, ans4, ans5,):
    score = 0
    if ans1.lower() == "paris":
        score += 1
        print("Question 1: Correct!")
    else:
        print("Question 1: Incorrect.")
    if ans2 == "4":
        score += 1
        print("Question 2: Correct!")
    else:
        print("Question 2: Incorrect.")
    if ans3 == "6":
        score+= 1
        print("Question 3 is Correct!")
    else:
        print("Question 3 is Incorrect.")
    if ans4 == "305":
        score+= 1 
        print(" Question 4 is Correct!")
    else: 
        print("Question 4 is incorrect.")
    if ans5 == "Rome":
        score+= 1 
        print("Question 5 is Correct!")
    else:
        print("Question 5 is incorrect>")
    
    return score




#question prompting 
answer_one = input("What is the capital of France? ")
answer_two = input("What is 2 + 2? ")
answer_three = input("What is 3 + 3?")
anwser_four = input(" What is the 300 + 5?")
anwser_five =input(" What is the capital of Italy?")



final_score = tally_score(answer_one, answer_two,answer_three,anwser_four,anwser_five)





print(f"\nYour final score is: {final_score}/5")    