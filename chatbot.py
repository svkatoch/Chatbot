import tkinter as tk
from tkinter import scrolledtext, messagebox
import openai

api_key = "add ypur key from creating account on open_ai"
client = openai.OpenAI(api_key=api_key)

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot GUI")

        
        self.root.geometry("600x400+200+100")

        self.root.configure(bg='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=15, bg="#ffffff")
        self.chat_display.pack(padx=10, pady=10)

       
        self.user_input = tk.Entry(self.root, width=50)
        self.user_input.pack(padx=10, pady=10)

       
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bg='#4CAF50', fg='white')
        self.send_button.pack(padx=10, pady=10)

      
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, bg='#e74c3c', fg='white')
        self.quit_button.pack(padx=10, pady=10)

       
        self.display_message("Bot: You are a helpful assistant.", 'blue')

    def send_message(self):
        user_message = self.user_input.get()
        self.display_message(f"User: {user_message}", 'black')

        if user_message.lower() == "quit":
            self.root.quit()

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            chat_completion = response.choices[0]
            assistant_message = chat_completion.message.content
            self.display_message(f"Bot: {assistant_message}", 'blue')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        self.user_input.delete(0, tk.END)

    def display_message(self, message, color):
        self.chat_display.tag_config(color, foreground=color)
        self.chat_display.insert(tk.END, message + "\n", color)
        self.chat_display.yview(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
