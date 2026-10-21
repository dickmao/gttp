#!/usr/bin/env python3
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

def find(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                yield v
            else:
                yield from find(v, key)
    elif isinstance(o, list):
        for v in o:
            yield from find(v, key)

def fetch_comments(api, video_id, limit=300):
    fetcher = api._fetcher
    html = fetcher._fetch_video_html(video_id)
    url = f"https://www.youtube.com/youtubei/v1/next?key={fetcher._extract_innertube_api_key(html, video_id)}"
    version = re.search(r'"INNERTUBE_CONTEXT_CLIENT_VERSION":"([^"]+)"', html).group(1)
    context = {'client': {'clientName': 'WEB', 'clientVersion': version}}
    post = lambda body: fetcher._http_client.post(url, json={'context': context, **body}).json()
    sections = [s for s in find(post({'videoId': video_id}), 'itemSectionRenderer') if s.get('sectionIdentifier') == 'comment-item-section']
    token = next(find(sections, 'token'), None)
    comments = []
    while token and len(comments) < limit:
        data = post({'continuation': token})
        comments += [c for c in find(data, 'commentEntityPayload') if '.' not in c['properties']['commentId']]
        items = [i for a in find(data, 'continuationItems') for i in a if 'continuationItemRenderer' in i]
        token = next(find(items, 'token'), None)
    return comments[:limit]

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
    manual = [t for t in transcript_list if not t.is_generated]
    generated = [t for t in transcript_list if t.is_generated]
    pick = lambda ts: next((t for t in ts if t.language_code.startswith('en')), ts[0] if ts else None)
    transcript = pick(manual) or pick(generated)
    transcript_text = '\n'.join([f"[{int(entry.start//60):02d}:{int(entry.start%60):02d}] {entry.text}" for entry in transcript.fetch()])
    print(transcript_text)
    print("\n=== COMMENTS ===")
    for c in fetch_comments(api, video_id):
        text = c['properties']['content']['content'].replace('\n', ' ')
        print(f"[{c['toolbar']['likeCountNotliked'].strip() or 0}] {c['author']['displayName']}: {text}")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
