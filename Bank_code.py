from tkinter.ttk import *
from tkinter import *

def deposit_cmd(dwindow, deposit_entry):
    deposit_amount = deposit_entry.get()
    ewindow = Tk()
    ewindow.title("Deposit Confirmation")
    ewindow.geometry("800x400")

    label_abc = Label(ewindow, text="ABC Bank", font=("Consolas", 30, 'bold'), fg="blue")
    label_abc.pack(pady=20)

    updated_amount = 10000 + int(deposit_amount)
    label_18 = Label(ewindow, text="Deposit Successful!", font=("Consolas", 25), fg="green")
    label_18.pack(pady=10)

    label_19 = Label(ewindow, text=f"Updated Amount = ${updated_amount}", font=("Consolas", 25), fg="black")
    label_19.pack(pady=10)

    close_button = Button(ewindow, text="Close", font=("Consolas", 20), command=ewindow.destroy, bg="#f5f536", fg="#88308a")
    close_button.pack(pady=20)

    ewindow.mainloop()
    dwindow.destroy()

def cmd_2():
    cwindow = Tk()
    cwindow.title("Transactions")
    label6 = Label(cwindow, text="Transactions with Person A : Received 10000.00$", font=("Consolas", 25))
    label7 = Label(cwindow, text="Transactions with Person B : Sent 1000.00$", font=("Consolas", 25))
    label8 = Label(cwindow, text="Transactions with Person C : Sent 10000.00$", font=("Consolas", 25))

    labelmain = Label(cwindow, text="ABC Bank", font=("Consolas", 25))
    labelmain.pack(side="top")

    label10 = Label(cwindow, text="View your previous Transactions", font=("Consolas", 25))
    label10.pack(side="top")

    label6.place(x=10, y=400)
    label7.place(x=10, y=450)
    label8.place(x=10, y=500)

    cwindow.mainloop()

def cmd():
    username = entry.get()
    password = passentry.get()
    if username == "User" and password == "1234":
        window.destroy()
        bwindow = Tk()
        bwindow.title("Account")
        bwindow.config(bg="white")
        label_11 = Label(bwindow, text="Successfully logged into account", font=("Consolas", 25), fg="blue", bg="White")
        label_11.place(y=300, x=0)

        label_12 = Label(bwindow, text="Account balance : 10000", font=("Consolas", 25), fg="green")
        label_12.place(y=300, x=1100)

        label_13 = Label(bwindow, text="ABC Bank", font=("Consolas", 25))
        label_13.pack(side="top")

        buttona = Button(bwindow, text="Show transactions", command=cmd_2, font=("Consolas", 25))
        buttona.pack(side=RIGHT)

        buttonb = Button(bwindow, text="Deposit", command=lambda: cmd_3(bwindow), font=("Consolas", 25))
        buttonb.pack(side=LEFT)

        buttonc = Button(bwindow, text="Withdraw", command=lambda: cmd_4(bwindow), font=("Consolas", 25))
        buttonc.pack(side=LEFT)

        bwindow.mainloop()

def cmd_3(bwindow):
    bwindow.destroy()
    dwindow = Tk()
    dwindow.title("Deposit")
    label_16 = Label(dwindow, text="ABC Bank", font=("Consolas", 25))
    label_16.pack(side=TOP)

    label10 = Label(dwindow, text="Deposit Desired Amount", font=("Consolas", 25))
    label10.pack(side="top")

    deposit_entry = Entry(dwindow, font=("Consolas", 25), bg="black", fg="white")
    deposit_entry.place(x=560, y=260)

    button_2 = Button(dwindow, text="Deposit", font=("Consolas", 16, 'bold'), bg="#f5f536", fg="#88308a", padx="10", pady="10", relief=RAISED, command=lambda: deposit_cmd(dwindow, deposit_entry), state=ACTIVE)
    button_2.place(x=670, y=500)

    label_17 = Label(dwindow, text="Amount: ", font=("Consolas", 25))
    label_17.place(y=260, x=350)

    dwindow.mainloop()

def withdrawal_cmd(fwindow, withdrawal_entry):
    withdraw = withdrawal_entry.get()  
    if withdraw.isdigit():  
        gwindow = Tk()
        gwindow.title("Withdraw Confirmation")
        gwindow.geometry("800x400")

        label_abc = Label(gwindow, text="ABC Bank", font=("Consolas", 30, 'bold'), fg="blue")
        label_abc.pack(pady=20)

        updated_amount_2 = 10000 - int(withdraw)  # Update balance
        label_18 = Label(gwindow, text="Withdrawal Successful!", font=("Consolas", 25), fg="green")
        label_18.pack(pady=10)

        label_19 = Label(gwindow, text=f"Updated Amount = ${updated_amount_2}", font=("Consolas", 25), fg="black")
        label_19.pack(pady=10)

        close_button = Button(gwindow, text="Close", font=("Consolas", 20), command=gwindow.destroy, bg="#f5f536", fg="#88308a")
        close_button.pack(pady=20)

        gwindow.mainloop()
        fwindow.destroy()
    else:
        error_window = Tk()
        error_window.title("Error")
        error_label = Label(error_window, text="Please enter a valid number!", font=("Consolas", 20), fg="red")
        error_label.pack(pady=10)
        error_button = Button(error_window, text="Close", command=error_window.destroy, font=("Consolas", 20))
        error_button.pack(pady=20)
        error_window.mainloop()

def cmd_4(bwindow):
    bwindow.destroy()  
    fwindow = Tk()
    fwindow.title("Withdrawal")

    label_17 = Label(fwindow, text="ABC Bank", font=("Consolas", 25))
    label_17.pack(side=TOP)

    label18 = Label(fwindow, text="Enter Amount to Withdraw", font=("Consolas", 25))  
    label18.pack(side="top")

    withdrawal_entry = Entry(fwindow, font=("Consolas", 25), bg="black", fg="white")
    withdrawal_entry.place(x=560, y=260)

    button_3 = Button(fwindow, text="Withdraw", font=("Consolas", 16, 'bold'), bg="#f5f536", fg="#88308a", padx="10", pady="10", relief=RAISED, command=lambda: withdrawal_cmd(fwindow, withdrawal_entry), state=ACTIVE)  # Corrected button text
    button_3.place(x=670, y=500)

    label_19 = Label(fwindow, text="Amount: ", font=("Consolas", 25))
    label_19.place(y=260, x=350)

    fwindow.mainloop()


window = Tk()
window.title("Banking Simulator")

button = Button(window, text="Login", font=("Consolas", 16, 'bold'), bg="#f5f536", fg="#88308a", padx="10", pady="10", relief=RAISED, command=cmd, state=ACTIVE)

entry = Entry(window, font=("Consolas", 25), bg="black", fg="white")
passentry = Entry(window, font=("Consolas", 25), bg="black", fg="white", show="*")

label = Label(window, text="username: ", font=("Consolas", 25))
label.place(y=260, x=350)

label2 = Label(window, text="password: ", font=("Consolas", 25))
label2.place(y=340, x=350)

label3 = Label(window, text="ABC Bank", font=("Consolas", 25))
label4 = Label(window, text="Enter your username and password to login", font=("Consolas", 25))

label5 = Label(window, text="To Login, Username = User, Password = 1234 ", font=("Consolas", 25))
label5.pack(side="bottom")

label3.pack(side="top")
label4.pack(side="top")
entry.place(x=560, y=260)
button.place(x=670, y=500)
passentry.place(x=560, y=340)

window.mainloop()
