#!/usr/bin/env python3
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

def extract_video_id(url_or_id):
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'^([0-9A-Za-z_-]{11})$'
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return None

if len(sys.argv) < 2:
    print("Error: No YouTube URL or video ID provided", file=sys.stderr)
    sys.exit(1)

video_id = extract_video_id(sys.argv[1])
if not video_id:
    print(f"Error: Could not extract video ID from '{sys.argv[1]}'", file=sys.stderr)
    sys.exit(1)

try:
    api = YouTubeTranscriptApi()
    transcript_list = api.list(video_id)
    codes = [t.language_code for t in transcript_list if t.is_generated] + [t.language_code for t in transcript_list]
    try:
        transcript = transcript_list.find_manually_created_transcript(codes)
    except NoTranscriptFound:
        transcript = transcript_list.find_generated_transcript(codes)
    transcript_text = '\n'.join([f"[{int(entry.start//60):02d}:{int(entry.start%60):02d}] {entry.text}" for entry in transcript.fetch()])
    print(transcript_text)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
