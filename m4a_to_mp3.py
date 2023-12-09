from pydub import AudioSegment

# Load the m4a file
m4a_audio = AudioSegment.from_file("file_path.m4a", format="m4a")

# Convert to mp3
m4a_audio.export("export_file_name.mp3", format="mp3")
