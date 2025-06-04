import speech_recognition as sr
import tkinter as tk
from threading import Thread

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Speech-to-Text Captioning")
        self.root.geometry("600x400")

        self.text_area = tk.Text(root, font=("Arial", 14), wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start Captioning", command=self.start_listening)
        self.start_button.pack(pady=10)

        self.recognizer = sr.Recognizer()
        self.listening = False

    def start_listening(self):
        if not self.listening:
            self.listening = True
            self.start_button.config(text="Listening...")
            Thread(target=self.listen_and_transcribe, daemon=True).start()

    def listen_and_transcribe(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.text_area.insert(tk.END, "Listening started...\n")
            while self.listening:
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    text = self.recognizer.recognize_google(audio)
                    self.text_area.insert(tk.END, f"> {text}\n")
                    self.text_area.see(tk.END)
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    self.text_area.insert(tk.END, "[Unrecognized speech]\n")
                except sr.RequestError as e:
                    self.text_area.insert(tk.END, f"[API Error: {e}]\n")
                    break

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()
