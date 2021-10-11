class Quizbrain:
    question_number = 0
    def __init__(self,q_list):
        self.list = q_list
        self.question_number=0
        self.correct =0
    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number+=1
        answer = input(f"Q.{self.question_number} : {current_question.question} ")
        if answer==current_question.correct_answer:
            print("You got it right!")
            self.correct+=1
        else:
            print("incorrect")

        print(f"Correct answer was {current_question.correct_answer}")
        print(f"Your current score is: {self.correct}/{self.question_number}")


