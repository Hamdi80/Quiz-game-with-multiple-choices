user_action = input("Do you want to play  YES/NO \n")
sentence_One = "Choose the correct answers below \n"
YES = "yes"
No = "no"



def play():
    if user_action != YES:
        print('EXIT')
    elif user_action == YES:
        print(sentence_One)

        print("Q1) Select the correct example of the complex datatype in Python")
        print("A) 3 + 2j \n"
              "B) -100j  \n"
              "C) 5j \n"
              "D) All of the above are correct")
        result1 = input('')
        if result1 == "c":
            print(f"correct! ")
        else:
            print('wrong answer!\n')
        print("Q2) How to represent 261500000 as a floating number in Python??"
                  "A) 2.615E8 \n"
                  "B) 261500000  \n"
                  "C) 261.5E8 \n"
                  "D)  2.6 ")
        result2 = input('')
        if result2 == "A":
            print("correct!")
        else:
                print('wrong answer!! \n')
        print("Q3) How to add a single-line comment in Python??"
              "A) /* This is a comment */ \n"
              "B)!! This is a comment \n"
              "C) // This is a comment \n"
              "D)  # This is a comment ")
        result3 = input('')
        if result3 == "D":
           print("correct!")
        else:
             print('wrong answer!!\n')

        print("Q4 How to create a variable in Python with a value 22.6?")
        print("A) int a = 22.6 \n"
              "B) a = 22.6  \n"
              "C) Integer a = 22.6 \n"
              "D) None of the above ")
        result4 = input('')
        if result4 == "B":
                print("correct!")
        else:
            print ('wrong answer!!\n')

        print("Q5) How to output the string “May the odds favor you” in Python?"
              "A) print(“May the odds favor you”) \n"
              "B) echo(“May the odds favor you”)  \n"
              "C) System.out(“May the odds favor you”) \n"
              "D)  printf(“May the odds favor you”) ")

        result5 = input('')
        if result5 == "A":
            print("correct!")
        else:
            print('wrong answer!!')
        print("""Q6) Do we need to compile a program before execution in Python??"
                          "A) Yes \n"
                          "B) No  """
                          )
        result6 = input('')
        if result6 == "B":
           print("correct!")
        else:
           print('wrong answer!!\n \n')

        score = (result1 + result2 + result3 + result4 + result5 + result6)
        print(score)
def ending():

    print("Thank you for answering the questions above ")



play()
ending()
