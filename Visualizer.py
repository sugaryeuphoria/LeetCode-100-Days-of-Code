import tkinter as tk
import random
import time

class AlgorithmVisualizer:
    def __init__(self, master, size=50):
        self.master = master
        self.master.title("Algorithm Visualizer")
        self.canvas = tk.Canvas(self.master, width=800, height=400)
        self.canvas.pack()

        self.size = size
        self.array = [random.randint(10, 300) for _ in range(size)]
        self.rectangles = []

        self.draw_array()

    def draw_array(self):
        self.canvas.delete("all")
        self.rectangles = []
        bar_width = 800 / self.size
        for i, value in enumerate(self.array):
            x1, y1 = i * bar_width, 400
            x2, y2 = x1 + bar_width, 400 - value
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            self.rectangles.append(rect)

    def bubble_sort(self):
        for i in range(self.size - 1):
            for j in range(self.size - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.update_canvas()
                    time.sleep(0.1)

    def update_canvas(self):
        self.draw_array()
        self.master.update_idletasks()

def main():
    root = tk.Tk()
    visualizer = AlgorithmVisualizer(root)

    # Add buttons to trigger sorting algorithms
    bubble_sort_button = tk.Button(root, text="Bubble Sort", command=visualizer.bubble_sort)
    bubble_sort_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
