import sys

video_num = sys.argv[1]
video_name = sys.argv[2]
transcript_text = sys.argv[3]

entry = f"\n## {video_num}. {video_name}\n\n{transcript_text}\n"

with open(r'C:\Users\alvaro\Desktop\AI SEO Mastery\transcripts.md', 'a', encoding='utf-8') as f:
    f.write(entry)

print(f"Appended video {video_num}: {video_name}")
