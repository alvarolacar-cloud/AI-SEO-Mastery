import sys

src = sys.argv[1]
dst = sys.argv[2]

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

with open(dst, 'a', encoding='utf-8') as f:
    f.write(content)

print(f"Appended {src} to {dst}")
