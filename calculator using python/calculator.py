import tkinter as tk

def buttonPressed(i):
    if i != '=':
        entry.insert(tk.END, i)
    else:
        expression = entry.get()
        try:
            value = eval(expression)
            new_string = f'{value: ,}'
            entry.delete(0, tk.END)
            entry.insert(0, new_string)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, e)

root = tk.Tk()
root.title("MikeyCalc")

entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 20))
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=5)

btn_frame = tk.Frame(root, width=80, height=100)
btn_frame.grid(row=1, columnspan=5)

Button_text = ['7', '8', '9', '/', '*', '4', '5', '6', '-', '+', '0', ' 1', '2', '3', '=']
i = j = 0
for x in Button_text:
    b = tk.Button(btn_frame, width=15, text=x, command=lambda x=x: buttonPressed(x))
    b.grid(row=i, column=j, ipadx=2, ipady=4)
    j += 1
    if j == 5:
        i += 1
        j = 0
del_btn = tk.Button(root, text='clear', width=82, command=lambda: entry.delete(0, tk.END))
del_btn.grid(row=2, columnspan=5, ipadx=5, ipady=4)
root.mainloop()
