import time 
from tkinter import*

a, b = 1, 1

def fibonacci():
    global a, b
    text_box.delete(1.0, END)  # Clear previous output
    a, b = 1, 1
    while True:
        text_box.insert(END, str(a) + "\n")
        text_box.yview(1.0)
        text_box.update()
        time.sleep(0.5)
        a, b = b, a + b
        if a > 1000:
            break


def user():
    user_input = int(entry.get())
    global a, b
    a, b = 1, 1
    while True:
        if user_input == a:
            result.config(text="yes")
            break
        elif user_input < a:
            result.config(text="no")
            break
            
        a, b = b, a + b

def stop():
    global stop_flag
    stop_flag = True

root = Tk()
root.geometry("390x500")
root.title("Fibonacci Series")

label = Label(root, text="Enter Number to check if it's in the Fibonacci series: ", font=("Arial", 10))
label.grid()

result = Label(root, text="", font=("Arial", 10))
result.grid()


entry = Entry(root, font=("Arial", 15))
entry.grid(row=1, column=0, pady=10,sticky=EW)

btn_check = Button(root, text="Check", font=("Arial", 15), command=user)
btn_check.grid(row=2, column=0, pady=10, sticky=EW)

btn_fibonacci = Button(root, text="Fibonacci Series", font=("Arial", 15), command=fibonacci)
btn_fibonacci.grid(row=3, column=0, pady=10,sticky=EW)

text_box = Text(root, width=40, height=10, font=("Arial", 12))
text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=10)



btn_stop = Button(root, text="Stop", font=("Arial", 15), command=stop)
btn_stop.grid(row=6, column=0, pady=10, sticky=EW)

root.mainloop()
