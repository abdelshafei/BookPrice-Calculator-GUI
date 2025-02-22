import tkinter as tk
from tkinter import messagebox
import math

def roundto(z):
    z = "%.3f"%z
    str_z = str(z)
    if (int(str_z[-3]) >= 1 and int(str_z[-3]) < 5):
        str_z = str_z.replace(str_z[-3:], "500")
        str_z = float(str_z)
        return "%.3f"%str_z
    elif (int(str_z[-3]) == 0):
        if(int(str_z[-2]) >= 1 and int(str_z[-2]) <= 9):
            str_z = str_z.replace(str_z[-3:], "500")
            str_z = float(str_z)
            return "%.3f"%str_z
        elif (int(str_z[-2]) == 0):
            if (int(str_z[-1]) >= 1 and int(str_z[-1]) <= 9):
                str_z = str_z.replace(str_z[-3:], "500")
                str_z = float(str_z)
                return "%.3f"%str_z
    elif (int(str_z[-3]) == 5):
        if(int(str_z[-2]) >= 1 and int(str_z[-2]) <= 9):
            z = math.ceil(float(str_z))
            return "%.3f"%z
        elif (int(str_z[-2]) == 0):
            if (int(str_z[-1]) >= 1 and int(str_z[-1]) <= 9):  
                z = math.ceil(float(str_z))
                return "%.3f"%z
    elif (int(str_z[-3]) > 5 and int(str_z[-3]) <= 9):
        z = math.ceil(float(str_z))
        return "%.3f"%z

    return z

def price_10files():
    global button_return
    button_return.grid_remove()
    change_label.grid_remove()

    def calculate_price1():
    
        input_field_value1 = input_field1.get()

        try:
            input = int(input_field_value1)
            if input >= 0 and input < 200:
                price = input* 0.01 + 0.25
                price1 = roundto(price)
            elif input >= 200 and input < 400:
                price = input* 0.01 + 0.5
                price1 = roundto(price)                
            elif input >= 400:
                price = input* 0.01 + 1
                price1 = roundto(price)                
            answer.config(text = ("The price is "+price1+" KWD"), fg = "#000000")
        except Exception as ve:
            messagebox.showerror("Price Calculator Malfunction", "Please enter only positive whole numbers on your next try")
      

    price_input1 = tk.Label(window, text = "Total Pages:", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    price_input1.grid(column = 0, row = 0)

    input_field1 = tk.Entry(window, font = "Arial", bg = "#FEFCF2")
    input_field1.grid(column = 1, row = 0, padx = 0,pady = 10)
   
    button_return1 = tk.Button(window, text = "Calculate Price", command = calculate_price1, bg = "#777474")
    button_return1.grid(column = 1, row = 120, )

    change_label1 = tk.Label(window, text = "*10 fils*", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    change_label1.grid(column = 0, row = 1)

def price_9files():
    global button_return
    button_return.grid_remove()
    change_label.grid_remove()  

    def calculate_price3():
    
         
        input_field_value2 = input_field2.get()

        try:
            input = int(input_field_value2)
            if input >= 0 and input < 200:
                price = input* 0.009 + 0.25
                price1 = roundto(price)
            elif input >= 200 and input < 400:
                price = input* 0.009 + 0.5
                price1 = roundto(price) 
            elif input >= 400:
                price = input* 0.009 + 1
                price1 = roundto(price) 
            answer.config(text = ("The price is "+price1+" KWD"), fg = "#000000")
        except Exception as ve:          
            messagebox.showerror("Price Calculator Malfunction", "Please enter only positive whole numbers on your next try")
      

    price_input2 = tk.Label(window, text = "Total Pages:", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    price_input2.grid(column = 0, row = 0)

    input_field2 = tk.Entry(window, font = "Arial", bg = "#FEFCF2")
    input_field2.grid(column = 1, row = 0, padx = 0,pady = 10)
   
    button_return2 = tk.Button(window, text = "Calculate Price", command = calculate_price3, bg = "#777474")
    button_return2.grid(column = 1, row = 120)

    change_label2 = tk.Label(window, text = "* 9 fils *", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    change_label2.grid(column = 0, row = 1)

def price_7files():
    global button_return
    button_return.grid_remove()
    change_label.grid_remove()  

    def calculate_price5():
    
         
        input_field_value2 = input_field2.get()

        try:
            input = int(input_field_value2)
            if input >= 0 and input < 200:
                price = input* 0.007 + 0.25
                price1 = roundto(price)
            elif input >= 200 and input < 400:
                price = input* 0.007 + 0.5
                price1 = roundto(price) 
            elif input >= 400:
                price = input* 0.007 + 1
                price1 = roundto(price) 
            answer.config(text = ("The price is "+price1+" KWD"), fg = "#000000")
        except Exception as ve:          
            messagebox.showerror("Price Calculator Malfunction", "Please enter only positive whole numbers on your next try")
      

    price_input2 = tk.Label(window, text = "Total Pages:", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    price_input2.grid(column = 0, row = 0)

    input_field2 = tk.Entry(window, font = "Arial", bg = "#FEFCF2")
    input_field2.grid(column = 1, row = 0, padx = 0,pady = 10)
   

    button_return2 = tk.Button(window, text = "Calculate Price", command = calculate_price5, bg = "#777474")
    button_return2.grid(column = 1, row = 120)

    change_label2 = tk.Label(window, text = "* 7 fils *", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    change_label2.grid(column = 0, row = 1)


def price_6files():
    global button_return
    button_return.grid_remove()
    change_label.grid_remove()  

    def calculate_price4():
    
         
        input_field_value2 = input_field2.get()

        try:
            input = int(input_field_value2)
            if input >= 0 and input < 200:
                price = input* 0.006 + 0.25
                price1 = roundto(price)
            elif input >= 200 and input < 400:
                price = input* 0.006 + 0.5
                price1 = roundto(price) 
            elif input >= 400:
                price = input* 0.006 + 1
                price1 = roundto(price) 
            answer.config(text = ("The price is "+price1+" KWD"), fg = "#000000")
        except Exception as ve:          
            messagebox.showerror("Price Calculator Malfunction", "Please enter only positive whole numbers on your next try")
      

    price_input2 = tk.Label(window, text = "Total Pages:", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    price_input2.grid(column = 0, row = 0)

    input_field2 = tk.Entry(window, font = "Arial", bg = "#FEFCF2")
    input_field2.grid(column = 1, row = 0, padx = 0,pady = 10)
   

    button_return2 = tk.Button(window, text = "Calculate Price", command = calculate_price4, bg = "#777474")
    button_return2.grid(column = 1, row = 120)

    change_label2 = tk.Label(window, text = "* 6 fils *", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    change_label2.grid(column = 0, row = 1)

def price_8files():
    global button_return
    button_return.grid_remove()
    change_label.grid_remove()  

    def calculate_price2():
    
         
        input_field_value2 = input_field2.get()

        try:
            input = int(input_field_value2)
            if input >= 0 and input < 200:
                price = input* 0.008 + 0.25
                price1 = roundto(price)
            elif input >= 200 and input < 400:
                price = input* 0.008 + 0.5
                price1 = roundto(price) 
            elif input >= 400:
                price = input* 0.008 + 1
                price1 = roundto(price) 
            answer.config(text = ("The price is "+price1+" KWD"), fg = "#000000")
        except Exception as ve:          
            messagebox.showerror("Price Calculator Malfunction", "Please enter only positive whole numbers on your next try")
      

    price_input2 = tk.Label(window, text = "Total Pages:", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    price_input2.grid(column = 0, row = 0)

    input_field2 = tk.Entry(window, font = "Arial", bg = "#FEFCF2")
    input_field2.grid(column = 1, row = 0, padx = 0,pady = 10)
   
    button_return2 = tk.Button(window, text = "Calculate Price", command = calculate_price2, bg = "#777474")
    button_return2.grid(column = 1, row = 120)

    change_label2 = tk.Label(window, text = "* 8 fils *", font = "Arial", bg = "#777474", fg = "#FEFCF2")
    change_label2.grid(column = 0, row = 1)

# Create the main window
window = tk.Tk()
window.title("Price Calculator")
window.geometry("800x300")
window.config(background = "#777474")

def calculate_price():
    
        input_field_value1 = input_field.get()

        try:
            input = int(input_field_value1)
            if input >= 0 and input < 200:
                price = input* 0.01 + 0.25
                price1 = roundto(price)
            elif input >= 200 and input < 400:
                price = input* 0.01 + 0.5
                price1 = roundto(price)                
            elif input >= 400:
                price = input* 0.01 + 1
                price1 = roundto(price)                
            answer.config(text = ("The price is "+price1+" KWD"), fg = "#000000")
        except Exception as ve:
            messagebox.showerror("Price Calculator Malfunction", "Please enter only positive whole numbers on your next try")
      

price_input = tk.Label(window, text = "Total Pages:", font = "Arial", bg = "#777474", fg = "#FEFCF2")
price_input.grid(column = 0, row = 0)

input_field = tk.Entry(window, font = "Arial", bg = "#FEFCF2")
input_field.grid(column = 1, row = 0, padx = 0,pady = 10)
   

answer = tk.Label(window, font = "Arial" ,bg = "#777474")
answer.grid(column = 2, row = 0)

button_return = tk.Button(window, text = "Calculate Price", command = calculate_price, bg = "#777474")
button_return.grid(column = 1, row = 140, rowspan = 120)

change_label = tk.Label(window, text = "*10 fils*", font = "Arial", bg = "#777474", fg = "#FEFCF2")
change_label.grid(column = 0, row = 1)

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="10 fils", command=price_10files)
filemenu.add_command(label="9 fils", command=price_9files)
filemenu.add_command(label="8 fils", command=price_8files)
filemenu.add_command(label="7 fils", command=price_7files)
filemenu.add_command(label="6 fils", command=price_6files)

menubar.add_cascade(label="change", menu=filemenu)

window.config(menu=menubar)

# Run the main loop
window.mainloop()