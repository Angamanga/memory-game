import tkinter as tk

root = tk.Tk()
root.title("A festive Memory Game")
root.geometry("1000x600")

result_label = tk.Label(root, text="", font=("Helvetica", 18))
heading = tk.Label(root, text="Welcome to the Memory Game!", font=("Helvetica", 24)).pack(pady=20)  
instructions = tk.Label(root, text="Memorize the order of the numbers before they are hidden, then try to recall them in the correct sequence.", font=("Helvetica", 16)).pack(pady=10)




root.mainloop()