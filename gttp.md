---
allowed-tools: Bash
argument-hint: [youtube-url]
description: Summarize YouTube video transcript
---

# YouTube Transcript Summary

Fetch the transcript and top comments using the command below.

```bash
uv run --with youtube-transcript-api python3 ~/.local/bin/gttp.py $1 > /tmp/gttp.$$
```

Based on the full transcript (everything before `=== COMMENTS ===`):
1. Provide a comprehensive summary organized by main topics
2. Include key timestamps for important points

Then, based on the comments (each prefixed with its like count),
follow the summary with a synopsis of the comment section: prevailing
sentiment, recurring themes, notable disagreements or corrections, and
standout highly-liked comments.
