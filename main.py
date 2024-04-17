import tkinter as tk
from tkinter import messagebox, font


class NumberGuesser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("数字当てゲーム")
        self.geometry("1600x300")  # ウィンドウのサイズをここで調整します
        self.l = 0
        self.r = 10001
        self.q_num = 0
        self.custom_font = font.Font(family="Arial", size=28)  # フォントサイズを調整
        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="", font=self.custom_font)
        self.question_label.pack(pady=40)  # テキストの周りの余白も調整

        yes_button = tk.Button(
            self,
            text="Yes",
            font=self.custom_font,
            command=lambda: self.process_answer(True),
        )
        yes_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=50, pady=20)

        no_button = tk.Button(
            self,
            text="No",
            font=self.custom_font,
            command=lambda: self.process_answer(False),
        )
        no_button.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=50, pady=20)

    def ask_question(self):
        if self.r - self.l > 1:
            self.q_num += 1
            self.mid = (self.l + self.r) // 2
            self.question_label.config(
                text=f"{self.q_num}回目の質問です。貴方の思い浮かべている数字は{self.mid}以上ですか？"
            )
        else:
            self.ask_final_question()

    def ask_final_question(self):
        answer = messagebox.askyesno(
            "確認", f"貴方の思い浮かべている数字は、ズバリ{self.l}ですね？"
        )
        if answer:
            messagebox.showinfo("結果", "正解できました。")
        else:
            messagebox.showerror("エラー", "プログラムにバグがあるようです...")
        self.destroy()

    def process_answer(self, is_yes):
        if is_yes:
            self.l = self.mid
        else:
            self.r = self.mid
        self.ask_question()


if __name__ == "__main__":
    app = NumberGuesser()
    app.mainloop()
