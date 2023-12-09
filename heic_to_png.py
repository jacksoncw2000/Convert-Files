import subprocess

def convert_heic_to_png(heic_file_path, png_file_path):
    subprocess.run(["magick", heic_file_path, png_file_path])

# Example usage
heic_file_path = '/Users/jackson/Desktop/IMG_6401.HEIC'
png_file_path = 'Headshot Jackson Williams.png'

convert_heic_to_png(heic_file_path, png_file_path)
