class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0 

    def next_question(self):
        curr_q = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number} {curr_q.text} (True/False)?: ")
        self.check_answer(ans, curr_q.answer)

    def check_answer(self, ans, correct_ans):
        if ans.lower() != correct_ans.lower():
            print("You got it wrong")
            print(f"The correct answer was: {correct_ans}.")

        else:
            print("You got it right")
            self.score += 1
        
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def get_score(self):
        return self.score