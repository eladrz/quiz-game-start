class QuizBrain:
    def __init__(self,Q_list):
        self.q_number=0
        self.q_list=Q_list
        self.score=0
        self.end_q=len(Q_list)-1

    def NextQuestion(self):
        current_q=self.q_list[self.q_number]
        self.q_number+=1
        user_answer=input(f"Q.{self.q_number}: {current_q.text} (True/False): ").lower()
        while user_answer!='true' and user_answer!='false':
            user_answer=input("Please type true or false: ").lower()
        self.check_answer(user_answer, current_q.answer)
    
    def still_has_q(self):
        return len(self.q_list)>self.q_number

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You right!")          
        else:
            print("That's wrong")
            print(f"The correct answer is: {correct_answer}")
        print(f"Your corrent score is: {self.score}/{self.q_number}")
        print(f"{self.end_q} questions remain\n")
        self.end_q-=1
