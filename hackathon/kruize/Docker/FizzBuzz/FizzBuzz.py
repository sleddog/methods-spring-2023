import tkinter as tk

def fizzbuzz(n):
    out = ''
    if (n % 3 == 0):                      
        out += 'Fizz'
    if (n % 5 == 0):                     
        out += 'Buzz'
    if (n % 7 == 0):                     
        out += 'Ping'
    if (n % 11 == 0):                    
        out += 'Pong'
    if (out == ''):                       
        out = str(n)
    
    return out

def run_fizzbuzz():
    myInput = entry.get()
    output.delete('1.0', tk.END)          
    try:
        myInput = int(myInput)
        output.insert(tk.END, fizzbuzz(myInput) + '\n')
    except ValueError:
        myInput = myInput.strip().split()
        try:
            start = int(myInput[0])
            end = int(myInput[1])
            if start > end:
                start, end = end, start
            for n in range(start, end+1):
                output.insert(tk.END, fizzbuzz(n) + '\n')
        except:
            output.insert(tk.END, "Invalid input. Please enter a single number or a range of numbers in the format 'start end'.\n")

root = tk.Tk()
root.title("FizzBuzz")

label = tk.Label(root, text="Enter a number or a range (in the format 'start end'):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Run", command=run_fizzbuzz)
button.pack()

output = tk.Text(root, height=10, width=50)
output.pack()

root.mainloop()
