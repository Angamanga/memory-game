import tkinter as tk
import random

root = tk.Tk()
root.title("A festive Memory Game")
root.geometry("1000x600")
number_of_tries = 0

result_label = tk.Label(root, text="", font=("Helvetica", 18))
heading = tk.Label(root, text="Welcome to the Memory Game!", font=("Helvetica", 24)).pack(pady=20)  
instructions = tk.Label(root, text="Memorize the order of the numbers before they are hidden, then try to recall them in the correct sequence.", font=("Helvetica", 16)).pack(pady=10)


def check_sequence():
    global number_of_tries, userInput, sequence, submit_button, result_label
    result_label.pack_forget()
    number_of_tries += 1
    user_input = userInput.get()
    user_sequence = list(map(int, user_input.split()))

    if user_sequence == sequence:
        result_label.config(
            text=f"Correct! You recalled the sequence in {number_of_tries} tries.", 
            font=("Helvetica", 18)
        )
        userInput.pack_forget()
        submit_button.pack_forget()
        start_game.config(text="Play Again")
        start_game.pack(pady=30)
    else:
        userInput.delete(0, tk.END)
        result_label.config(
            text=f"Incorrect sequence. You entered {user_input}. You have now guessed {number_of_tries} times. Try again!", 
            font=("Helvetica", 18)
        )
    
    result_label.pack(pady=20)
    
def start_button():
    global sequence, userInput, submit_button, result_label, number_of_tries
    # cleaning up UI if user is playing again
    start_game.pack_forget()
    result_label.pack_forget()
    number_of_tries = 0
    
    # generate random sequence
    sequence = random.sample(range(1, 11), 5)
    sequence_label = tk.Label(root, text=" ".join(map(str, sequence)), font=("Helvetica", 20))
    sequence_label.pack(pady=20)
    
    userInput = tk.Entry(root, font=("Helvetica", 18))
    submit_button = tk.Button(root, text="Submit", font=("Helvetica", 18), command=check_sequence)
    
    # showing sequence for 3 seconds, then hiding it and showing input field
    root.after(3000, sequence_label.destroy)
    root.after(3000, lambda: userInput.pack(pady=20))
    root.after(3000, lambda: submit_button.pack(pady=20))

start_game = tk.Button(root, text="Start Game", font=("Helvetica", 18), command=start_button)
start_game.pack(pady=30)

root.mainloop()