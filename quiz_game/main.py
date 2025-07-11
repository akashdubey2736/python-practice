from question_module import  Question
from data import question_data
from quiz_game import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_q=Question(question_text,question_answer)
    question_bank.append(new_q)

quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score is : {quiz.score}")