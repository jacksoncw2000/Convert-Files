import datetime
from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(mov_file_path, output_file_path):
    # Load the .mov video file
    clip = VideoFileClip(mov_file_path)

    # Write the clip as an .mp4 file with audio
    # codec="libx264" ensures video encoding with H.264 codec
    # audio_codec="aac" ensures audio is encoded with AAC codec
    # If the original video has audio, it will be included in the output
    clip.write_videofile(output_file_path, codec="libx264", audio_codec="aac")

current_date_time = datetime.datetime.now()
current_date_time = current_date_time.strftime('%Y.%m.%d_%H.%M.%S')

# Example usage
convert_mov_to_mp4("file_path.mov", f"{current_date_time}_exported_video.mp4")
