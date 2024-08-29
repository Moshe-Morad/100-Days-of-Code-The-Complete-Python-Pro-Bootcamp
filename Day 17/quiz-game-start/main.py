from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qu in question_data:
    qu_text = qu["question"]
    qu_answer = qu["correct_answer"]
    question = Question(qu_text, qu_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():#if quiz still has questions remaining:
    quiz.next_question()

print(f"You've completed the quiz, Your final score was {quiz.score}/{quiz.question_number}")