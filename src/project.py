import os
from PIL import Image
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, OptionMenu, Frame
from moviepy.editor import *

class ReelifyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Reelify - Portfolio Preparation Made Easy")
        self.master.config(bg="#333333")
        master.geometry("525x500")  # Window size
        master.resizable(False, False)  # Disable resizing both width and height

        title_frame = Frame(master, bg="#333333")
        title_frame.grid(row=0, column=0, columnspan=3, pady=20)

        Label(title_frame, text="REELIFY", font=("Helvetica", 36, "bold"), fg="white", bg="#333333").grid(row=0, column=0)

        # Variables for input paths
        self.dir_artwork = StringVar()
        self.logo_path = StringVar()
        self.dir_output = StringVar()
        
        
        # UI Layout for file paths
        Label(master, text="Artwork Directory:", fg="white", bg="#333333").grid(row=1, column=0, padx=10, pady=5)
        Entry(master, textvariable=self.dir_artwork, width=50).grid(row=1, column=1, padx=10, pady=5)
        Button(master, text="Browse", command=self.browse_artwork, bg="#555555", fg="white").grid(row=1, column=2, padx=10, pady=5)

        Label(master, text="Logo Path:", fg="white", bg="#333333").grid(row=2, column=0, padx=10, pady=5)
        Entry(master, textvariable=self.logo_path, width=50).grid(row=2, column=1, padx=10, pady=5)
        Button(master, text="Browse", command=self.browse_logo, bg="#555555", fg="white").grid(row=2, column=2, padx=10, pady=5)

        Label(master, text="Output Directory:", fg="white", bg="#333333").grid(row=3, column=0, padx=10, pady=5)
        Entry(master, textvariable=self.dir_output, width=50).grid(row=3, column=1, padx=10, pady=5)
        Button(master, text="Browse", command=self.browse_output, bg="#555555", fg="white").grid(row=3, column=2, padx=10, pady=5)

        # Dropdown for features
        Label(master, text="Feature:", fg="white", bg="#333333").grid(row=4, column=0, padx=10, pady=5)
        self.feature = StringVar()
        self.feature.set("Logo Stamp")
        OptionMenu(master, self.feature, "Logo Stamp", "Watermark", "Demo Reel", command=self.update_feature_fields).grid(row=4, column=1, padx=10, pady=5)

        # Frame for feature-specific input fields
        self.feature_frame = Frame(master)
        self.feature_frame.grid(row=5, column=0, columnspan=3)

        # Run button
        Button(master, text="Run", command=self.run_feature, bg="#555555", fg="white").grid(row=6, column=1, pady=20)

        # Initialize fields based on default feature
        self.update_feature_fields("Logo Stamp")

    def browse_artwork(self):
        self.dir_artwork.set(filedialog.askdirectory())

    def browse_logo(self):
        self.logo_path.set(filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")]))

    def browse_output(self):
        self.dir_output.set(filedialog.askdirectory())

    def update_feature_fields(self, selected_feature):
        # Clear any existing feature-specific fields
        for widget in self.feature_frame.winfo_children():
            widget.destroy()

        if selected_feature == "Logo Stamp":
            # Fields for Logo Stamp
            self.logo_scale = StringVar()
            Label(self.feature_frame, text="Scale Multiplier:").grid(row=0, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.logo_scale, width=20).grid(row=0, column=1, padx=10, pady=5)
            self.logo_scale.set("1")

            self.logo_position = StringVar()
            self.logo_position.set("bottom_right")  # Default position
            positions = ["top_left", "top_right", "bottom_left", "bottom_right"]
            Label(self.feature_frame, text="Logo Position:").grid(row=1, column=0, padx=10, pady=5)
            OptionMenu(self.feature_frame, self.logo_position, *positions).grid(row=1, column=1, padx=10, pady=5)

        elif selected_feature == "Watermark":
            # Fields for Watermark
            self.scale_multiplier = StringVar()
            self.opacity = StringVar()
            self.rotation = StringVar()

            Label(self.feature_frame, text="Scale Multiplier:").grid(row=0, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.scale_multiplier, width=20).grid(row=0, column=1, padx=10, pady=5)
            self.scale_multiplier.set("1")

            Label(self.feature_frame, text="Opacity (0-255):").grid(row=1, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.opacity, width=20).grid(row=1, column=1, padx=10, pady=5)
            self.opacity.set("128")

            Label(self.feature_frame, text="Rotation Angle:").grid(row=2, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.rotation, width=20).grid(row=2, column=1, padx=10, pady=5)
            self.rotation.set("45")

        elif selected_feature == "Demo Reel":
            # Fields for Demo Reel
            self.artist_name = StringVar()
            self.phone_number = StringVar()
            self.email = StringVar()
            self.reel_title = StringVar()

            Label(self.feature_frame, text="Artist Name:").grid(row=0, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.artist_name, width=30).grid(row=0, column=1, padx=10, pady=5)
            self.artist_name.set("John Doe")

            Label(self.feature_frame, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.phone_number, width=30).grid(row=1, column=1, padx=10, pady=5)
            self.phone_number.set("123-456-7890")

            Label(self.feature_frame, text="Email:").grid(row=2, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.email, width=30).grid(row=2, column=1, padx=10, pady=5)
            self.email.set("johndoe@example.com")

            Label(self.feature_frame, text="Reel Title:").grid(row=3, column=0, padx=10, pady=5)
            Entry(self.feature_frame, textvariable=self.reel_title, width=30).grid(row=3, column=1, padx=10, pady=5)
            self.reel_title.set("My Demo Reel")

    def run_feature(self):
        # Validate paths
        if not self.dir_artwork.get() or not self.logo_path.get() or not self.dir_output.get():
            print("Please ensure all directories are selected.")
            return

        feature = self.feature.get()

        if feature == "Logo Stamp":
            self.run_logo_stamp()
        elif feature == "Watermark":
            self.run_watermark()
        elif feature == "Demo Reel":
            self.run_demo_reel()

    def run_logo_stamp(self):
        print("Running Logo Stamp...")
        logo_stamp(self.dir_artwork.get(), self.logo_path.get(), self.dir_output.get(),
                   position=self.logo_position.get(),
                   logo_scale=int(self.logo_scale.get()))

    def run_watermark(self):
        print("Running Watermark...")
        watermark(self.dir_artwork.get(), self.logo_path.get(), self.dir_output.get(),
                  scale_multiplier=float(self.scale_multiplier.get()), 
                  opacity=int(self.opacity.get()), rotation=int(self.rotation.get()))

    def run_demo_reel(self):
        print("Running Demo Reel...")
        demo_reel(self.dir_artwork.get(), self.logo_path.get(), self.dir_output.get(),
                  artist_name=self.artist_name.get(), 
                  phone_number=self.phone_number.get(), 
                  email=self.email.get(), 
                  reel_title=self.reel_title.get())


def logo_stamp(dir_artwork, logo_path, dir_output, position="bottom_right", logo_scale=1):
    
    
    if not os.path.exists(dir_output):
        os.makedirs(dir_output)

    logo = Image.open(logo_path).convert("RGBA")
    

    for filename in os.listdir(dir_artwork):
        artwork_path = os.path.join(dir_artwork, filename)


        if filename.lower().endswith((".png", ".jpg", ".jpeg")):

            artwork = Image.open(artwork_path).convert("RGBA")
            artwork_width, artwork_height = artwork.size

            scale_multiplier = logo_scale/100

            new_logo_width = int(artwork_width * scale_multiplier)
            logo_aspect_ratio = logo.height / logo.width
            new_logo_height = int(new_logo_width * logo_aspect_ratio)
            resized_logo = logo.resize((new_logo_width, new_logo_height), Image.Resampling.LANCZOS)
            


            margin_x = int(artwork_width * 0.01)
            margin_y = int(artwork_width * 0.01)


            if position == "bottom_right":
                x = artwork_width - new_logo_width - margin_x
                y = artwork_height - new_logo_height - margin_y
            elif position == "bottom_left":
                x = margin_x
                y = artwork_height - new_logo_height - margin_y
            elif position == "top_right":
                x = artwork_width - new_logo_width - margin_x
                y = margin_y
            elif position == "top_left":
                x = margin_x
                y = margin_y
            else:
                x = artwork_width - new_logo_width - margin_x
                y = artwork_height - new_logo_height - margin_y


            artwork.paste(resized_logo, (x, y), resized_logo)


            output_path = os.path.join(dir_output, filename)
            artwork.convert("RGB").save(output_path, "PNG")

    print(f"Completed stamping logos on images within {dir_output}")

def watermark(dir_artwork, logo_path, dir_output, scale_multiplier=1, opacity=128, rotation=45):

    logo = Image.open(logo_path).convert("RGBA")
    logo_width, logo_height = logo.size

    logo_opacity = Image.new("RGBA", logo.size)
    for x in range(logo_width):
        for y in range(logo_height):
            r, g, b, a = logo.getpixel((x, y))
            logo_opacity.putpixel((x, y), (r, g, b, int(a * (opacity / 255))))

    for filename in os.listdir(dir_artwork):
        artwork_path = os.path.join(dir_artwork, filename)

        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            artwork = Image.open(artwork_path).convert("RGBA")
            artwork_width, artwork_height = artwork.size

            scaled_logo_width = int(artwork_width * scale_multiplier / 10)
            logo_aspect_ratio = logo.height / logo.width
            scaled_logo_height = int(scaled_logo_width * logo_aspect_ratio)
            resized_logo = logo_opacity.resize(
                (scaled_logo_width, scaled_logo_height), Image.Resampling.LANCZOS
            )

            rotated_logo = resized_logo.rotate(rotation, expand=True)

            watermark_layer = Image.new("RGBA", (artwork_width, artwork_height), (0, 0, 0, 0))

            x_offset, y_offset = 0, 0
            while y_offset < artwork_height:
                while x_offset < artwork_width:
                    watermark_layer.paste(rotated_logo, (x_offset, y_offset), rotated_logo)
                    x_offset += rotated_logo.width
                x_offset = 0
                y_offset += rotated_logo.height

            watermarked_artwork = Image.alpha_composite(artwork, watermark_layer)
            output_path = os.path.join(dir_output, filename)
            watermarked_artwork.convert("RGB").save(output_path, "PNG")

    print(f"Completed watermarking images within {dir_output}")
    

def demo_reel(dir_artwork, logo_path, dir_output, artist_name, phone_number, email, reel_title):
    
    print("Processing files for demo reel...")

    clips = []

    #Create Demo Reel Intro Plate

    title_text = TextClip(f"{reel_title}", fontsize=120, color='white', bg_color='black', size=(1920, 200)).set_position(("center", 100))
    name_text = TextClip(f"{artist_name}", fontsize=60, color='white', bg_color='black', size=(1920, 100)).set_position(("center", 700))
    phone_text = TextClip(f"{phone_number}", fontsize=50, color='white', bg_color='black', size=(1920, 100)).set_position(("center", 800))
    email_text = TextClip(f"{email}", fontsize=50, color='white', bg_color='black', size=(1920, 100)).set_position(("center", 900))

    logo = Image.open(logo_path)

    if logo.mode != "RGBA":
        logo = logo.convert("RGBA")

    logo.save("logo_with_alpha.png")

    logo_clip = (
        ImageClip("logo_with_alpha.png")
        .resize(height=300)  
        .set_position(("center", 350))  
    )

    intro_text = CompositeVideoClip([title_text, name_text, phone_text, email_text, logo_clip], size=(1920, 1080)).set_duration(5)

    supported_images = (".png", ".jpg", ".jpeg")
    supported_videos = (".mp4", ".mov")

    clips.append(intro_text)

    for filename in os.listdir(dir_artwork):
        file_path = os.path.join(dir_artwork, filename)

        if filename.lower().endswith(supported_images):

            image_clip = (
                ImageClip(file_path)
                .set_duration(1)
                
            )
            clips.append(image_clip)

        elif filename.lower().endswith(supported_videos):

            video_clip = VideoFileClip(file_path)
            clips.append(video_clip)


        if not clips:
            print("One or more of the files in the directory is unsupported! Please try again...")
            return
        
    reel = concatenate_videoclips(clips, method="compose")

    output_file = os.path.join(dir_output, "demo_reel.mp4")

    reel.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    root = Tk()
    app = ReelifyApp(root)
    root.mainloop()
