import qrcode
from tkinter import Tk, Label, Entry, Button, messagebox, Canvas, Frame
from PIL import Image, ImageTk
import io

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.configure(bg="#f0f0f0")  # Set background color

        # Create a frame for better organization
        frame = Frame(root, bg="#ffffff", padx=20, pady=20)
        frame.pack(pady=20)

        # Input label
        self.label = Label(frame, text="Enter text or URL:", font=("Arial", 14), bg="#ffffff")
        self.label.pack(pady=10)

        # Input field
        self.entry = Entry(frame, width=50, font=("Arial", 12), bd=2, relief="groove")
        self.entry.pack(pady=10)

        # Generate button
        self.button = Button(frame, text="Generate QR Code", command=self.generate_qr,
                             font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", width=20)
        self.button.pack(pady=20)

        # Canvas to display the QR code
        self.canvas = Canvas(frame, width=250, height=250, bg="white", highlightthickness=2, highlightbackground="#4CAF50")
        self.canvas.pack(pady=20)

        self.img_tk = None  # Variable to hold the PhotoImage reference

    def generate_qr(self):
        input_data = self.entry.get()
        if not input_data:
            messagebox.showerror("Input Error", "Please enter text or URL to generate QR code.")
            return

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(input_data)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert the image to a format Tkinter can use
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)  # Move the pointer to the start of the image byte array

        # Open the image with PIL and display it on the canvas
        img_pil = Image.open(img_byte_array)
        self.display_qr_code(img_pil)

    def display_qr_code(self, img):
        # Resize the image to fit within the canvas dimensions
        img = img.resize((250, 250), Image.LANCZOS)  # Resize to fit the canvas
        self.img_tk = ImageTk.PhotoImage(img)  # Keep a reference to avoid garbage collection

        # Clear the canvas
        self.canvas.delete("all")

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor='nw', image=self.img_tk)  # Top-left corner

if __name__ == "__main__":
    root = Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
