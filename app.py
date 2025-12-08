import tkinter as tk

root = tk.Tk()
root.title("A festive Memory Game")
root.geometry("1000x600")
number_of_tries = 0

result_label = tk.Label(root, text="", font=("Helvetica", 18))
heading = tk.Label(root, text="Welcome to the Memory Game!", font=("Helvetica", 24)).pack(pady=20)  
instructions = tk.Label(root, text="Memorize the order of the numbers before they are hidden, then try to recall them in the correct sequence.", font=("Helvetica", 16)).pack(pady=10)


def check_sequence():
    global number_of_tries, userInput, sequence, result_label
    result_label.pack_forget()
    number_of_tries += 1
    user_input = userInput.get()
    user_sequence = list(map(int, user_input.split()))
    if(user_sequence == sequence):
        result_label.config(text=f"Correct! You recalled the sequence in {number_of_tries} tries.", font=("Helvetica", 18))
    else:
        userInput.delete(0, tk.END)
        result_label.config(text=f"Incorrect sequence. You entered {user_input}. You have now guessed {number_of_tries} times. Try again!", font=("Helvetica", 18))
    
    result_label.pack(pady=20)
    
def start_button():
    global game_started, userInput
    game_started = True
    start_game.pack_forget()
    print("Game Started!")
    global sequence
    sequence = [1, 2, 3, 4, 5]
    sequence_label = tk.Label(root, text=" ".join(map(str, sequence)), font=("Helvetica", 20))
    sequence_label.pack(pady=20)
    root.after(3000, sequence_label.destroy)
    userInput = tk.Entry(root, font=("Helvetica", 18))
    userInput.pack(pady=20)
    submit_button = tk.Button(root, text="Submit", font=("Helvetica", 18), command=check_sequence)
    submit_button.pack(pady=10)

start_game = tk.Button(root, text="Start Game", font=("Helvetica", 18), command=start_button)
start_game.pack(pady=30)

root.mainloop()