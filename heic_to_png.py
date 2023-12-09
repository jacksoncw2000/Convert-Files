import subprocess

def convert_heic_to_png(heic_file_path, png_file_path):
    subprocess.run(["magick", heic_file_path, png_file_path])

# Example usage
heic_file_path = 'file_path.HEIC'
png_file_path = 'export_file_name.png'

convert_heic_to_png(heic_file_path, png_file_path)
