# Reelify

## Repository
https://github.com/pixelslayerr/Reelify

## Description
Reelify is a simply Python tool that automates the process of adding logos, watermarking, and editing a demo reel for a collection of digital artwork. Prepping your art to be posted on your portfolio can always take some time, so this tool is designed to make that process more efficient whilst also offering a variety of different settings to the user.

## Features
- Feature 1: Logo Stamp
	- This feature allows the user to provide a directory that contains a folder of artwork as well as a logo so that the logo can be repeatedly assigned to a specific location on all of the artwork. This will primarily use basic Pillow commands for image compositing, but will also feature some settings for editing the amount of logo padding, which corner of the image it occupies, its size, color, etc. 
- Feature 2: Watermark Overlay
	- For freelance artists that may want to display a series of commission examples on their page without risking theft, this feature will add an overlay of the artist's logo repeatedly stamped across the image. This feature will make use of a for loop in conjunction with Pillow to march across the image and stamp the watermark several times over. Users will be able to adjust the overlay's opacity, rotation, and number of logo stamps per row.
- Feature 3: Demo Reel Generator
	- For artists who want to present their work in a video format, this feature will use Pillow and Movie.py to automate the process of creating a demo reel. The program will read a user's folder containing all the content they wish to combine (though each file must be already named sequenctially 0001, 0002, etc. so the user can decide the order they wish each work to be presented in) and then string it together into a .mp4 file. Likewise, the video will also include a customizable introduction image at the beginning, which is typical of reels. It contains things such as the artist's name, title of the reel, and contact information. All of these things can be determined by the user before the function is run. If time allows, I'd also like to add options for fade in/fade out transitions, more format customization for the introduction page, and even the option to include background music. 

## Challenges
- Learning how to instruct Python to read and write to specific directories.
- Becoming well-acquainted enough with Pillow in order to perform more complex image operations.
- Using Movie.py to edit both images and video files together in a way that is seamless and works with different file formats.

## Outcomes
Ideal Outcome:
- All three of the program's main features work and include several different customizable settings. The program is smart enough to not totally break if something is inputed incorrectly, but return and error message and go back to the previous step.

Minimal Viable Outcome:
- All three of the program's main features work, but may not include as much customization or break under certain conditions. 

## Milestones

- Week 1
  1. Implement basic functionality for Logo Stamp tool.
  2. Clean up code, add some customization and error message triggers. 

- Week 2
  1. Implement basic functionality for Watermark Overlay tool.
  2. Clean up code, add some customization and error message triggers. 

- Week 3 (Final)
  1. Implement basic functionality for Demo Reel tool.
  2. Clean up code, ensure the tool can work with multiple formats, run multiple tests, implement more customization options if time allows. 
