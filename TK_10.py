from tkinter import *

x_root = Tk()
x_root.geometry("644x344")
x_root.title("Harry Ka GUI")
canvas_width=800
canvas_height=400

x_root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(x_root,width=canvas_width,height=canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="red")

# To create a rectangle specify parameters in this order - coors of top left and coors of bottom right
can_widget.create_rectangle(3, 5, 700, 300, fill="blue")

#center coors
can_widget.create_text(200, 200, text="python")

#rectangle- coors and then creates the oval
can_widget.create_oval(344,233,244,355)

x_root.mainloop()