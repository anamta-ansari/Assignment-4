# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.cell_size = 30
        self.grid = []
        self.eraser_size = 50

        self.create_grid()
        self.create_eraser()

        # Bind mouse movement
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        """Creates a grid of blue cells."""
        for row in range(0, 500, self.cell_size):
            row_cells = []
            for col in range(0, 500, self.cell_size):
                rect = self.canvas.create_rectangle(col, row, col + self.cell_size, row + self.cell_size, fill="blue", outline="black")
                row_cells.append(rect)
            self.grid.append(row_cells)

    def create_eraser(self):
        """Creates the eraser rectangle."""
        self.eraser = self.canvas.create_rectangle(50, 50, 50 + self.eraser_size, 50 + self.eraser_size, fill="white", outline="black")

    def move_eraser(self, event):
        """Moves the eraser and erases blue cells."""
        x, y = event.x, event.y
        x1, y1, x2, y2 = x - self.eraser_size // 2, y - self.eraser_size // 2, x + self.eraser_size // 2, y + self.eraser_size // 2

        # Move eraser
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Erase affected cells
        for row in self.grid:
            for cell in row:
                cx1, cy1, cx2, cy2 = self.canvas.coords(cell)
                if not (cx2 < x1 or cx1 > x2 or cy2 < y1 or cy1 > y2):  # Check overlap
                    self.canvas.itemconfig(cell, fill="white")

# Run the application
root = tk.Tk()
app = EraserApp(root)
root.mainloop()
