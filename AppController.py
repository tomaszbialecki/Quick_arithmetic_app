import tkinter as tk
# from tkinter import messagebox
# from math_generator import MathGenerator
# from review_planner import ReviewPlanner
# from settings import Settings
# from progress_tracker import ProgressTracker
# from statistics_window import StatisticsWindow

#sample modules that I will need/przykładowe moduły które będą mi potrzebne



class AppController:

#These are sample components and functions that I will need in the application,
#Remember __init__ means for the class itself/
#To są przykładowe komponenty i funkcje które będą mi potrzebne w aplikacji,
#Pamiętaj __init__ czyli dla klasy samej w sobie

    def __init__(self,root):
        self.root = root
        # self.math_generator = MathGenerator()
        # self.review_planner = ReviewPlanner()
        # self.settings = Settings()
        # self.progress_tracker = ProgressTracker()
        # self.statistics_window = StatisticsWindow()
        self.create_gui()
    
    def create_gui(self):
        self.root.title("Aplikacja do ćwiczenia matematyki")
        
# Example button/Przykładowy przycisk
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        math_problem = self.math_generator.generate_problem()
        user_answer = self.get_user_answer()
        
# Measuring response time and scheduling repetition/Pomiar czasu odpowiedzi i planowanie powtórki/
    #     response_time = self.measure_response_time()
    #     self.review_planner.schedule_review(math_problem, user_answer, response_time)

if __name__ == "__main__":
    root = tk.Tk()  # Here we create the main application window/Tutaj tworzymy główne okno aplikacji
    app = AppController(root)
    root.mainloop()  # We start the loop of the main window/Rozpoczynamy pętlę głównego okna