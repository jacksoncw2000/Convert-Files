from pydub import AudioSegment

# Load the m4a file
m4a_audio = AudioSegment.from_file("/Users/jackson/Desktop/Avery Chinese.m4a", format="m4a")

# Convert to mp3
m4a_audio.export("TEST 1.mp3", format="mp3")
