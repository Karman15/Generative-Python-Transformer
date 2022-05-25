import os

dir = "repos"
for dirpath, dirnames, filenames in os.walk(dir):
    for file in filenames:
        full_path = os.path.join(dirpath, file)

        if (full_path.endswith('.py')):
            print(f"Keeping {full_path}")
        else:
            print(f"--------Deleting {full_path}")
            if dir in full_path:
                os.remove(full_path)
