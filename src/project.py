import os
from PIL import Image


def main():
    while True:
        print("\n||| Welcome to Reelify! What feature would you like to use? |||")
        
        print("1. Logo Stamp")
        print("2. Watermark")
        print("3. Demo Reel")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            dir_artwork = input("Enter the directory containing the artwork: ")
            logo_path = input("Enter the directory for the logo you would like to stamp: ")
            dir_output = input("Enter the path you would like to save the stamped images to: ")
            global logo_scale
            logo_scale = float(input("Enter the logo scale as a fraction of artwork width (e.g., 0.1 for 10%): ") or 1)

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


            logo_stamp(dir_artwork, logo_path, dir_output, position=position)
        
        elif choice == "2":
            watermark()
        elif choice == "3":
            demo_reel()
        elif choice == "4":
            print("Shutting down Reelify...")
            break
        else:
            print("Unrecognized choice. Please select a number between 1 and 4.")


def logo_stamp(dir_artwork, logo_path, dir_output, position="bottom_right"):
    
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

def watermark():
    print("Haven't implemented this feature yet!")
    

def demo_reel():
    print("Haven't implemented this feature yet!")


if __name__ == "__main__":
    main()

