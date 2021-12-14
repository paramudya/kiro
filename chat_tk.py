import tkinter as tk
root = tk.Tk()
root.title("Chatbot")
def send():
    send = "You -> "+e.get()
    txt.insert("n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert("n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert("n" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert("n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert("n" + "Bot -> Great! how can I help you.")
    else:
        txt.insert("n" + "Bot -> Sorry! I dind't got you")
txt = tk.Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = tk.Entry(root, width=100)
e.grid(row=1, column=0)
send = tk.Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()