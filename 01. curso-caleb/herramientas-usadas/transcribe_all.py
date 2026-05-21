import subprocess
import re
import shutil
import sys
import os

OUTPUT_FILE = r'C:\Users\alvaro\Desktop\AI SEO Mastery\transcripts.md'
WATCH_SCRIPT = r'C:\Users\alvaro\.claude\plugins\claude-video\scripts\watch.py'

videos = [
    (3, r'C:\Users\alvaro\Desktop\AI SEO Mastery\Local SEO Foundations\videos\Updating Google Business Profile via Management Software.mp4'),
    (4, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\What is the Core 30.mp4'),
    (5, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Core 30 Local SEO Site Structure.mp4'),
    (6, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Core 30 Content Audit.mp4'),
    (7, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Plumbing Website Structure for Local Leads.mp4'),
    (8, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Technical SEO Audit Workflow with Screaming Frog.mp4'),
    (9, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Adding Schema.mp4'),
    (10, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\How to Add Local Business Schema.mp4'),
    (11, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Using Local SEO Rank Heatmaps in Leadsnap.mp4'),
    (12, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Determining Local Rank Map Size.mp4'),
    (13, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Identifying Low Competition Local SEO Markets.mp4'),
    (14, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Granting Manager and WordPress Access Steps.mp4'),
    (15, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\New Client Onboarding Process and Tracking.mp4'),
    (16, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Estimating Scope for Local SEO Growth.mp4'),
    (17, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Core 30, Topical, and Geographic Relevance (1).mp4'),
    (18, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Building More Topical Relevance.mp4'),
    (19, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Building More Geographical Relevance.mp4'),
    (20, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\AI Content Prioritization - Geographic Relevance.mp4'),
    (21, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\About Us Pages, Building Real Person Trust.mp4'),
    (22, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Local Links Strategy for SEO Authority.mp4'),
    (23, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Optimizing Multiple Google Business Profiles.mp4'),
    (24, r'C:\Users\alvaro\Desktop\AI SEO Mastery\How to do Local AI Seo\videos\Updating Google Business Profile via Management Software.mp4'),
]

success_count = 0
fail_count = 0

for num, video_path in videos:
    video_name = os.path.basename(video_path)
    print(f"\n{'='*60}")
    print(f"Processing video {num}: {video_name}")
    print('='*60)

    try:
        result = subprocess.run(
            ['python', WATCH_SCRIPT, video_path, '--whisper', 'groq', '--max-frames', '1'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=300
        )
        output = result.stdout + result.stderr

        # Extract work dir for cleanup
        work_dir_match = re.search(r'\[watch\] working dir: (.+)', output)
        work_dir = work_dir_match.group(1).strip() if work_dir_match else None

        # Extract transcript section
        transcript_match = re.search(r'## Transcript\s*\n_Source: whisper \(groq\)\._\s*\n```\n(.*?)```', output, re.DOTALL)

        if transcript_match:
            transcript_text = transcript_match.group(1).strip()

            entry = f"\n## {num}. {video_name}\n\n{transcript_text}\n"

            with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
                f.write(entry)

            print(f"SUCCESS: Transcript appended ({len(transcript_text)} chars)")
            success_count += 1
        else:
            print(f"FAILED: Could not find transcript in output")
            print("Output snippet:", output[:500])
            fail_count += 1

        # Cleanup work dir
        if work_dir and os.path.exists(work_dir):
            shutil.rmtree(work_dir, ignore_errors=True)
            print(f"Cleaned up: {work_dir}")

    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: Video {num} exceeded 5 minutes")
        fail_count += 1
    except Exception as e:
        print(f"ERROR: {e}")
        fail_count += 1

print(f"\n{'='*60}")
print(f"DONE: {success_count} succeeded, {fail_count} failed")
print(f"Total videos processed: {success_count + fail_count} of {len(videos)}")
