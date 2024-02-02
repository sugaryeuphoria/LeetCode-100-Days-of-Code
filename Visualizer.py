import tkinter as tk  # Import the Tkinter module for creating GUI applications
import random  # Import the random module for generating random numbers
import time  # Import the time module for introducing delays

class AlgorithmVisualizer:
    def __init__(self, master, size=50):
        # Initialize the AlgorithmVisualizer class with the main window and an optional array size
        self.master = master
        self.master.title("Algorithm Visualizer")  # Set the title of the main window
        self.canvas = tk.Canvas(self.master, width=800, height=400)  # Create a canvas for drawing
        self.canvas.pack()  # Pack the canvas into the main window

        self.size = size  # Set the size of the array
        self.array = [random.randint(10, 300) for _ in range(size)]  # Generate a random array of given size
        self.rectangles = []  # List to store rectangle objects representing array bars

        self.draw_array()  # Draw the initial state of the array

    def draw_array(self):
        # Draw the array on the canvas using rectangles
        self.canvas.delete("all")  # Clear the canvas
        self.rectangles = []  # Reset the list of rectangles
        bar_width = 800 / self.size  # Calculate the width of each bar

        for i, value in enumerate(self.array):
            x1, y1 = i * bar_width, 400  # Coordinates of the bottom-left corner of the rectangle
            x2, y2 = x1 + bar_width, 400 - value  # Coordinates of the top-right corner of the rectangle
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")  # Create a blue rectangle
            self.rectangles.append(rect)  # Add the rectangle object to the list

    def bubble_sort(self):
        # Implement the bubble sort algorithm
        for i in range(self.size - 1):
            for j in range(self.size - i - 1):
                if self.array[j] > self.array[j + 1]:
                    # Swap elements if they are in the wrong order
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.update_canvas()  # Update the canvas to reflect the changes
                    time.sleep(0.1)  # Introduce a delay for visualization

    def update_canvas(self):
        # Update the canvas with the current state of the array
        self.draw_array()  # Redraw the array
        self.master.update_idletasks()  # Update the main window

def main():
    root = tk.Tk()  # Create the main Tkinter window
    visualizer = AlgorithmVisualizer(root)  # Create an instance of the AlgorithmVisualizer

    # Add buttons to trigger sorting algorithms
    bubble_sort_button = tk.Button(root, text="Bubble Sort", command=visualizer.bubble_sort)
    bubble_sort_button.pack()  # Pack the button into the main window

    root.mainloop()  # Start the main event loop

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
