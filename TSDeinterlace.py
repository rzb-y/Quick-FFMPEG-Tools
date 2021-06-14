import os
import ffmpeg

list = []
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  list.append(f)

directory = "."
files_in_directory = os.listdir(directory)
filtered_files = [file for file in files_in_directory if file.endswith("py")]
filtered_files.extend([file for file in files_in_directory if file.endswith("m4a")])
filtered_files.extend([file for file in files_in_directory if file.endswith(".DS_Store")])

for files in filtered_files:
    list.remove(files)

if not os.path.exists("output"):
    os.makedirs("output")

for i in list:
    video = ffmpeg.input(i)
    if i.startswith('[DLK'):
        strr = "./output/" + i[10:-3] + ".mov"
    else:
        strr = "./output/" + i[:-3] + ".mov"
    out = ffmpeg.output(video, strr, vf="yadif=1")
    out.run()