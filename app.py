import tkinter as tk
import random

# Basic setup
root = tk.Tk()
root.title("A festive Memory Game")
root.geometry("1000x600")

# Game state
number_of_tries = 0
sequence = []

# UI Elements
heading = tk.Label(root, text="Welcome to the Memory Game!", font=("Helvetica", 24)).pack(pady=20)  
instructions = tk.Label(root, text="Memorize the order of the numbers before they are hidden, then try to recall them in the correct sequence.", font=("Helvetica", 16))
result_label = tk.Label(root, text="", font=("Helvetica", 18))
sequence_label = tk.Label(root, font=("Helvetica", 20))
hint_label = tk.Label(root, font=("Helvetica", 16))
user_input = tk.Entry(root, font=("Helvetica", 18))
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 18))
start_button = tk.Button(root, text="Start Game", font=("Helvetica", 18))
restart_button = tk.Button(root, text="Restart", font=("Helvetica", 18))

# Function to check the user's input against the sequence
def check_sequence():
    global number_of_tries, sequence, user_input, result_label, submit_button
    result_label.pack_forget()
    number_of_tries += 1
    user_input_value = user_input.get()
    user_sequence = list(map(int, user_input_value.split()))

    if user_sequence == sequence:
        result_label.config(
            text=f"Correct! You recalled the sequence in {number_of_tries} tries.", 
            font=("Helvetica", 18)
        )
        user_input.pack_forget()
        submit_button.pack_forget()
        start_button.config(text="Play Again")
        start_button.pack(pady=30)
    else:
        user_input.delete(0, tk.END)
        result_label.config(
            text=f"Incorrect sequence. You entered {user_input_value}. You have now guessed {number_of_tries} times. Try again!", 
            font=("Helvetica", 18)
        )
    
    result_label.pack(pady=20)
    
def start_game():
    global sequence, user_input, hint_label, submit_button, result_label, number_of_tries
    global sequence, userInput, submit_button, result_label, number_of_tries

    # cleaning up UI if user is playing again
    start_button.pack_forget()
    result_label.pack_forget()
    number_of_tries = 0
    hint_label.pack_forget()
    user_input.delete(0, tk.END)
    user_input.pack_forget()
    submit_button.pack_forget()
    restart_button.place_forget()

    # generate random sequence
    sequence = random.sample(range(1, 11), 5)
    hint = sequence.copy()
    random.shuffle(hint)
    instructions.pack(pady=10)
    sequence_label.config(text=" ".join(map(str, sequence)))
    sequence_label.pack(pady=20)
    hint_label.config(text=f"Hint (shuffled): {' '.join(map(str, hint))}")
    submit_button.config(command=check_sequence)

    # showing sequence for 3 seconds, then hiding it and showing input field
    root.after(3000, sequence_label.pack_forget)
    root.after(3000, lambda: hint_label.pack(pady=10))
    root.after(3000, lambda: user_input.pack(pady=20))
    root.after(3000, lambda: submit_button.pack(pady=20))
    restart_button.config(command=start_game)
    restart_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        
start_button.config(command=start_game)
start_button.pack(pady=30)
root.mainloop()