import os

print(os.getcwd())
directory = "SukumaSwitch2"

lyric_files = os.listdir(directory)

mergedFileName = "SwitchAll.txt"
mergedFile = open(mergedFileName, "w", encoding="utf8")

for f in lyric_files:
	if ".txt" not in f:
		continue

	file = open(directory + "/" + f, "r", encoding="utf8")
	content = file.read()
	mergedFile.write(content)
	mergedFile.write("\n\n" + "=" * 30 + "\n\n")
	file.close()

mergedFile.close()
print("Merge processing done!")