import tkinter as tk
root = tk.Tk()
from focusAid import focusAid

button = tk.Button(root,
                   text="Do you need motivation?",
                   command = focusAid,
                   anchor="center",
                   )

button.pack(expand=True)

root.mainloop()