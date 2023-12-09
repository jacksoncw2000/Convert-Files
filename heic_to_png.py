import os
import subprocess
import datetime
from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path
from tqdm import tqdm

def convert_heic_to_png(heic_file_path, png_file_path):
    subprocess.run(["magick", heic_file_path, png_file_path])

# Example usage
heic_file_path = 'file_path.HEIC'
png_file_path = 'export_file_name.png'

convert_heic_to_png(heic_file_path, png_file_path)

def batch_convert_images(active_directory_path, source_folder_name):
    current_date_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    print(f'\nConvert HEIC to PNG {current_date_time}')

    source_folder = Path(f'{active_directory_path}/{source_folder_name}')
    output_folder = Path(f'{active_directory_path}/outputs/{current_date_time} {source_folder_name}')
    output_folder.mkdir(parents=True, exist_ok=True)

    image_files = list(source_folder.iterdir())
    for image_file in tqdm(image_files, desc="Converting images", unit="file"):
        if image_file.suffix.lower() in ['.heic', '.jpg', '.jpeg']:
            if image_file.suffix.lower() == '.heic':
                register_heif_opener()
            output_path = output_folder / f"{image_file.stem}.png"
            save_as_png(image_file, output_path)

    print("\nHEIC to PNG conversion complete")

# Example usage
batch_convert_images('active_directory_path', 'source_folder_name')
