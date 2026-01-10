#create kbc
#Create a program capable of displaying questions to the user like KBC.
#  Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.
#players choose their subject-science,maths,sports,social science
question_science=[# list of quesions and its options
"\n1.What is the earth's natural satellite? \n(a) Sun  \n(b) Moon \n(c) Earth \n(d) Venus",
"2.What is the main function of the heart? \n\na) To pump blood \nb) To digest food\nc) To absorb nutrients\nd) To filter waste",
"3.Which of the following is a plant?\na) A dog\nb) A tree\nc) A bird\nd) A fish",
"4.What color is the sky during the day?\na) Red\nb) Blue\nc) Green\nd) Yellow",
"5.Which of these is an animal?\na) A flower\nb) A cat\nc) A rock\nd) A chair",
"6.Which of the following helps us breathe?\na) Heart\nb) Lungs\nc) Stomach\nd) Brain",
"7.What do we use to see?\na) Ears\nb) Nose\nc) Eyes\nd) Mouth",
"8.Which of the following is a part of the body?\na) Tree\nb) Flower\nc) Hair\nd) Sun",
"9.What do we use to hear?\na) Eyes\nb) Ears\nc) Mouth\nd) Nose",
"10.What do we use to taste with?\n(a)Eyes\n(b)Mouth\n(c)Toungue\n(d)Hair",
]
question_maths=[
    "\n1.What is 5+10?\na) 21 \nb) 19 \nc) 15 \nd) 19",
    "2.What is 3 x 4?\na) 12\nb) 8\nc) 7\nd) 2",
    "3.What is 20 + 5?\na) 25\nb) 30\nc) 15\nd) 20",
    "4.What is 10 - 6?\na) 5\nb) 4\nc) 3\nd) 6",
    "5.If you have 2 groups of 5 cookies, how many cookies do you have in total?\na) 10\nb) 5\nc) 15\nd) 2"
]
sci_ans=["b", "a", "b", "b", "b", "b", "c", "c", "b", "c"]

maths_ans=["c", "a", "a", "b", "a"]

gk_question=[
    "1.Who is SRK\na)Horse\nb)Actor\nC)Celebrity\nd)Robot",
    "2.Who is the current President of the United States?\na) Joe Biden\nb) Donald Trump\nc) Barack Obama\nd) George W. Bush",
    "3.What is the capital of France?\na) Berlin\nb) Madrid\nc) Paris\nd) Rome",
    "4.Which planet is known as the Red Planet?\na) Earth\nb) Mars\nc) Jupiter\nd) Venus",
    "5.What is the largest ocean on Earth?\na) Atlantic Ocean\nb) Indian Ocean\nc) Arctic Ocean\nd) Pacific Ocean",
]
gk_answer=["b", "b","c", "b", "d"]
#writing the code
def kbc(questions,answers,subject_name):
    print("\nThe questions for group",subject_name,"are:\n")
    score=0
    for i in range(len(questions)):#here it loop to all elements of the list one by one till the end
        print(questions[i])
        user_ans=input("\nEnter the correct answer\n[a/b/c/d]:")
        if user_ans== answers[i]:
            print("CORRECT!!\n")
            score+=1000
        else:
            print("WRONG, THE CORRECT ANSWER IS",answers[i])
    print("You Won $",score) 

#############################################################################

sub_list=["science","maths","s.st","sports","gk"]#list of selectable subject
subject=(input("1.Science  2.Maths  3.S.St  4.Sports 5.gk \n\nChoose your subject:"))
if subject in("science","1"):
    print("\nThe questions for group science are:")
    score=0
    for i in range(len(question_science)):# here it selects 10 que
        print(question_science[i])
        user_ans=input("\nEnter the correct answer\n[a/b/c/d]:")
        if user_ans == sci_ans[i]:
            print("CORRECT!!\n")
            score+=1000
        else:
            print("WRONG, THE CORRECT ANSWER IS",sci_ans[i])  
    print("You Won $",score)
elif subject in ("maths","2"):
    kbc(question_maths,maths_ans, "maths")#adding choice for maths subject
elif subject in("gk","5"):
    print("\nThe questions for GK group are:")
    score=0
    for i in range((len(gk_question))):
        print(gk_question[i])
        user_ans=input("\nenter the correct answer\n[a/b/c/d]")
        if user_ans==gk_answer[i]:
            print("\nCorrect")
            score+=10
        else:
            print("wrong answer")
    print("you won",score,"dolla")    
else:
    print("\nSubject not implemented yet\n")
           
