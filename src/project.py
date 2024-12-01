import os
from PIL import Image
from moviepy.editor import *

dir_artwork = ""
logo_path = ""
dir_output = ""


def main():
    global dir_artwork, logo_path, dir_output

    print("\n--- Set Global Directories ---")
    dir_artwork = input("Enter the directory containing the artwork: ")
    logo_path = input("Enter the directory for the logo: ")
    dir_output = input("Enter the path for the output directory: ")


    while True:
        print("\n||| Welcome to Reelify! What feature would you like to use? |||")
        
        print("1. Logo Stamp")
        print("2. Watermark")
        print("3. Demo Reel")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            
            global logo_scale
            logo_scale = float(input("Enter a multiplier for the size of the logo: ") or 1)

            print("\nWhere would you like the logo to be stamped?:")
            print("1. Bottom Right")
            print("2. Bottom Left")
            print("3. Top Right")
            print("4. Top Left")
            
            position_choice = input("Enter your choice (1-4): ")

            position_map = {
                "1": "bottom_right",
                "2": "bottom_left",
                "3": "top_right",
                "4": "top_left",
            }
            
            position = position_map.get(position_choice, "bottom_right")


            logo_stamp(position=position)
        
        elif choice == "2":

            logo_scale = float(input("Enter a multiplier for size of the logo: ") or 1)
            opacity = int(input("Enter the watermark opacity (0-255): ") or 128)
            rotation_angle = float(input("Enter the watermark rotation angle (e.g., 45): ") or 0)
           
            watermark(logo_scale, opacity, rotation_angle)
        
        elif choice == "3":
            
            artist_name = (input("Enter your name: ") or "John Doe")
            phone_number = (input("Enter your phone number") or "123-456-7890")
            email = (input("Enter your E-Mail Address") or "johndoe@example.com")
            reel_title = (input("Enter the title of your reel: ") or "My Demo Reel")

            demo_reel(artist_name, phone_number, email, reel_title)

        elif choice == "4":
            print("Shutting down Reelify...")
            break
        else:
            print("Unrecognized choice. Please select a number between 1 and 4.")


def logo_stamp(position="bottom_right"):
    global dir_artwork, logo_path, dir_output
    
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

def watermark(scale_multiplier=1, opacity=128, rotation=45):
    global dir_artwork, logo_path, dir_output

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

            scale_multiplier = logo_scale/100

            scaled_logo_width = int(artwork_width * scale_multiplier)
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
    

def demo_reel(artist_name, phone_number, email, reel_title):

    global dir_artwork, dir_output
    
    print("Processing files for demo reel...")

    clips = []

    #Create Demo Reel Intro Plate
    text = f"Artist: {artist_name}\nPhone: {phone_number}\nEmail: {email}\nReel Title: {reel_title}"

    intro_text = TextClip(text, fontsize=40, color='white', bg_color='black', size=(1920, 1080))

    intro_text = intro_text.set_duration(3)

    intro_text = intro_text.set_position('center')

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
    main()

