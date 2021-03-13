import random
from questions import question

correct_answer={"Delhi",'28',"Aryabhatta","Mitochondria","26","Jaipur",
            "Russia","Peacock","64","Sundar pichai"}
quiz=dict(zip(question,correct_answer))

print("RULES OF GAME")
print("The first initial must be a capital letter of answer")
print("Add a space between two words")
score=0
count=0
while count<10:
	x=random.randint(1,len(question)+1)
	y=question[x]
	print(y)
	count+=1
	your_answer=input("Enter The Correct Answer")
if your_answer == quiz[y]:
	score+=1
	print('correct answer')
	print("play again")
	print("current score is:",score)
else:
	print("current score is:",score)
	print('BETTER LUCK NEXT TIME')
	print("play again")


