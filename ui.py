from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game.")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, foreground="white",)
        self.score_label.grid(row=0, column=1)

        self.text_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.text_canvas.create_text(
            150, 
            125,
            width=280,
            text="Some Questuon Text.", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.text_canvas.grid(row=1, column=0, columnspan=2,pady=50)

        tick_image = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=tick_image, command=self.correct_ans)
        self.correct_button.grid(row=2, column=1)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_image, command=self.wrong_ans)
        self.wrong_button.grid(row=2, column=0)
        
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.text_canvas.config(bg="white")
        self.text_canvas.itemconfig(self.question_text, text= q_text,)

    def correct_ans(self):
        check_point = self.quiz.check_answer("True")
        self.give_feedback(check_point)

    def wrong_ans(self):
        check_point = self.quiz.check_answer("False")
        self.give_feedback(check_point)

    def give_feedback(self, correct):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}\nQuestion's Attempted: {self.quiz.question_number}")
            if correct:
                self.text_canvas.config(bg="light green")
            else:
                self.text_canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_question)
        else:
            self.text_canvas.itemconfig(self.question_text, text=f"You Have Completed your Quiz.\nFinal Score: {self.quiz.score}/{self.quiz.question_number}")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

