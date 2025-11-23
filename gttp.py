#!/usr/bin/env python3
import sys
import subprocess

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print('Installing youtube_transcript_api...', file=sys.stderr)
    install_cmd = None
    if subprocess.run(['command', '-v', 'uv'], capture_output=True).returncode == 0:
        install_cmd = ['uv', 'tool', 'install', 'youtube_transcript_api']
    elif subprocess.run(['command', '-v', 'pipx'], capture_output=True).returncode == 0:
        install_cmd = ['pipx', 'install', 'youtube_transcript_api']
    else:
        install_cmd = ['pip3', 'install', '--user', 'youtube_transcript_api']

    result = subprocess.run(install_cmd, capture_output=True)
    if result.returncode != 0:
        print(f'Error installing youtube_transcript_api: {result.stderr.decode()}', file=sys.stderr)
        sys.exit(1)

    from youtube_transcript_api import YouTubeTranscriptApi

import re

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
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = '\n'.join([f"[{int(entry['start']//60):02d}:{int(entry['start']%60):02d}] {entry['text']}" for entry in transcript])
    print(transcript_text)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
