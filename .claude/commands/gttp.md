---
allowed-tools: Bash(python3:*)
argument-hint: [youtube-url]
description: Summarize YouTube video transcript
---

# YouTube Transcript Summary

$ARGUMENTS

If no YouTube URL was provided above, ask the user for the URL before proceeding.

Otherwise, fetch the transcript using the command below and provide a detailed summary.

!`python3 -c "
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi

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

video_id = extract_video_id('$ARGUMENTS')
if not video_id:
    print(f\"Error: Could not extract video ID from '$ARGUMENTS'\", file=sys.stderr)
    sys.exit(1)

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = '\n'.join([f\"[{int(entry['start']//60):02d}:{int(entry['start']%60):02d}] {entry['text']}\" for entry in transcript])
    print(transcript_text)
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(1)
"`

Based on the full transcript above:
1. Provide a comprehensive summary organized by main topics
2. Include key timestamps for important points
3. Highlight any actionable insights or conclusions

Note: You can ask me to make the summary shorter or longer, or inquire about specific timestamps or topics from the transcript.
