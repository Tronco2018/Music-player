import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, window):
        
        self.window = window
        self.window.title("Music player")
        self.window.geometry("400x150")

        
        self.btn_select_file = tk.Button(text="Select file", command=self.open_file)
        self.btn_play = tk.Button(text="Play", command=self.play)
        self.btn_stop = tk.Button(text="Stop", command=self.stop)

        
        self.btn_select_file.pack(fill=tk.X, padx=10, pady=10)
        self.btn_play.pack(fill=tk.X, padx=10, pady=10)
        self.btn_stop.pack(fill=tk.X, padx=10, pady=10)

        
        pygame.mixer.init()

        self.file_path = ""

    def open_file(self):
        
        self.file_path = filedialog.askopenfilename()

    def play(self):
        
        if self.file_path:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def stop(self):
        
        pygame.mixer.music.stop()

if __name__ == '__main__':
    
    window = tk.Tk()
    app = MusicPlayer(window)
    window.mainloop()