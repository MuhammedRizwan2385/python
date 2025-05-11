import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Load the image using Pillow
image_path = r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\deep learning.png"  # Replace with your image path
try:
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
except FileNotFoundError:
    print(f"Error: Image file not found at {image_path}")
    root.destroy()
    exit()

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.pack()



# Start the Tkinter event loop
root.mainloop()
