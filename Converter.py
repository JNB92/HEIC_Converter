import os
from tkinter import Label, Button, filedialog, messagebox, Tk
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()


class HeicToJpgConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEIC to JPG Converter")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#2e3b4e")

        # Style and font settings
        self.font = ("Arial", 12, "bold")
        self.text_color = "#f8f9fa"

        # Header
        self.header = Label(
            self.root,
            text="HEIC to JPG Converter",
            font=("Arial", 16, "bold"),
            fg=self.text_color,
            bg="#2e3b4e"
        )
        self.header.pack(pady=10)

        # Instructions
        self.instructions = Label(
            self.root,
            text="Select HEIC files using the button below",
            font=self.font,
            fg=self.text_color,
            bg="#2e3b4e"
        )
        self.instructions.pack(pady=10)

        # Buttons
        self.select_button = Button(
            self.root,
            text="Select Files",
            command=self.select_files,
            font=self.font,
            bg="#007bff",
            fg="white",
            activebackground="#0056b3",
            activeforeground="white"
        )
        self.select_button.pack(pady=10)

        self.convert_button = Button(
            self.root,
            text="Convert",
            command=self.convert_files,
            font=self.font,
            bg="#28a745",
            fg="white",
            activebackground="#1e7e34",
            activeforeground="white"
        )
        self.convert_button.pack(pady=10)

        # Placeholder for files
        self.files = []

    def select_files(self):
        """Open file dialog to select HEIC files."""
        filetypes = [("HEIC Files", "*.heic")]
        self.files = filedialog.askopenfilenames(filetypes=filetypes)
        if self.files:
            messagebox.showinfo("Files Selected", f"{len(self.files)} files selected!")

    def convert_files(self):
        """Convert HEIC files to JPG."""
        if not self.files:
            messagebox.showwarning("No Files", "Please select HEIC files first!")
            return

        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return

        converted_count = 0
        for file_path in self.files:
            try:
                with Image.open(file_path) as img:
                    img.convert("RGB").save(
                        os.path.join(output_dir, os.path.basename(file_path).replace(".heic", ".jpg")),
                        "JPEG"
                    )
                    converted_count += 1
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert {os.path.basename(file_path)}: {e}")

        messagebox.showinfo("Conversion Complete", f"{converted_count} files converted successfully!")


# Main application
if __name__ == "__main__":
    root = Tk()
    app = HeicToJpgConverterApp(root)
    root.mainloop()
