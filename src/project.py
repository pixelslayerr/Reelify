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
            logo_stamp()
        elif choice == "2":
            watermark()
        elif choice == "3":
            demo_reel()
        elif choice == "4":
            print("Shutting down Reelify...")
            break
        else:
            print("Unrecognized choice. Please select a number between 1 and 4.")


def logo_stamp():
    print("Haven't implemented this feature yet!")
   

def watermark():
    print("Haven't implemented this feature yet!")
    

def demo_reel():
    print("Haven't implemented this feature yet!")


if __name__ == "__main__":
    main()

