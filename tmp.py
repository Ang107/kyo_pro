import tkinter as tk
from tkinter import messagebox


class BinarySearchGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("数字当てゲーム")
        self.low = 1
        self.high = 1000
        self.query_count = 0
        self.max_queries = 10
        self.history = []

        self.label = tk.Label(master, text="", font=("Arial", 16))
        self.label.pack(pady=20)

        self.yes_button = tk.Button(
            master, text="Yes", font=("Arial", 14), width=10, command=self.yes_pressed
        )
        self.yes_button.pack(side="left", padx=20, pady=20)

        self.no_button = tk.Button(
            master, text="No", font=("Arial", 14), width=10, command=self.no_pressed
        )
        self.no_button.pack(side="right", padx=20, pady=20)

        self.next_question()

    def next_question(self):
        if self.query_count >= self.max_queries:
            messagebox.showinfo("結果", f"正解は {self.low} だと思います！")
            self.master.destroy()
            return

        if self.low == self.high:
            messagebox.showinfo("結果", f"正解は {self.low} です！")
            self.master.destroy()
            return

        self.mid = (self.low + self.high) // 2
        self.query_count += 1
        question = f"Q{self.query_count}: N は {self.mid} 以下？"
        self.label.config(text=question)

        self.history.append((self.low, self.high, self.mid))

    def yes_pressed(self):
        self.high = self.mid
        self.next_question()

    def no_pressed(self):
        self.low = self.mid + 1
        self.next_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = BinarySearchGUI(root)
    root.mainloop()
