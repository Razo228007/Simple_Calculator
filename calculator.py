import tkinter as tk
###################
#This function is called whenever a calculator button is clicked.
#It gets the text from the button and decides what action to take.
#If "=" is clicked, it calculates the result.
#If "C" is clicked, it clears the entry.
#Otherwise, it adds the clicked button text to the entry
###################
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expr = entry.get()    
            result = operations(expr)   
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


############
#This function performs the mathematical operation.
#It checks which operator (+, -, *, /) is in the expression.
#Then it splits the expression into two numbers and calculates the result
############

def operations(expr):
    if "+" in expr:
        a, b = expr.split("+")
        return float(a) + float(b)
    elif "-" in expr:
        a, b = expr.split("-")
        return float(a) - float(b)
    elif "*" in expr:
        a, b = expr.split("*")
        return float(a) * float(b)
    elif "/" in expr:
        a, b = expr.split("/")
        return float(a) / float(b)
    else:
        return float(expr)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 50), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

###########
#This function creates all calculator buttons.
#It uses two loops:
#- i represents the row number
#- j represents the column number
#Each button is placed on the grid and connected to the click function.
###########

def functions():
    for i, row in enumerate(buttons):
        for j, btn_text in enumerate(row):
            btn = tk.Button(root, text=btn_text, font=("Arial", 18), width=5, height=3)
            btn.grid(row=i+1, column=j, padx=5, pady=5)
            btn.bind("<Button-1>", click)

functions()  
root.mainloop()
