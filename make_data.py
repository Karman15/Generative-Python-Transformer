import os

dir = "repos"

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 250

NEWLINECHAR = "<N>"

full_paths = []
for dirpath, dirnames, filenames in os.walk(dir):
    for file in filenames:
        full_path = os.path.join(dirpath, file)
        full_paths.append(full_path)
print(len(full_paths))

with open("python_text_data.txt", "a") as f:
    for fpath in full_paths:
        try:
            d = open(fpath,"r").read()
            fd = d.replace("\n", NEWLINECHAR)

            if 100 < len(d) <= MAX_CHAR_LENGTH:
                f.write(fd+'\n')
            else:
                sd = fd.split(f"{NEWLINECHAR}{NEWLINECHAR}")
                substring = ""
                for split in sd:
                    substring += split+f"{NEWLINECHAR}{NEWLINECHAR}"
                    if MIN_CHAR_LENGTH <= len(substring) <= MAX_CHAR_LENGTH:
                        f.write(substring+'\n')
                        substring = ""
        except Exception as e:
            print(str(e))
                
