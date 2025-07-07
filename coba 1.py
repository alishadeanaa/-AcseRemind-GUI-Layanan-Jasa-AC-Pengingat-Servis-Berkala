# f


import tkinter as tk
from PIL import Image, ImageTk

def resize_image(event):
    global img, img_ref
    new_width = event.width
    new_height = event.height
    resized_image = img.resize((new_width, new_height), Image.ANTIALIAS)
    img_ref = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_image, image=img_ref)

root = tk.Tk()

# Set atribut fullscreen dan topmost
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)

# Menyembunyikan title bar
root.overrideredirect(True)

# Membuat canvas sebagai latar belakang
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

# Buka gambar
image_path = "loginn2.png"  # Gantilah dengan path gambar Anda
img = Image.open(image_path)
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), 'antialias')  # Use 'antialias' instead of Image.ANTIALIAS
img_ref = ImageTk.PhotoImage(img)

# Tambahkan gambar ke canvas
canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=img_ref)

# Fungsi untuk menyesuaikan ukuran gambar saat jendela diresize
root.bind("<Configure>", resize_image)

root.mainloop()