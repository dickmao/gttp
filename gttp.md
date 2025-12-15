---
allowed-tools: Bash
argument-hint: [youtube-url]
description: Summarize YouTube video transcript
---

# YouTube Transcript Summary

Fetch the transcript using the command below.

```bash
uv run --with youtube-transcript-api python3 ~/.local/bin/gttp.py $1 > /tmp/gttp.$$
```

Based on the full transcript:
1. Provide a comprehensive summary organized by main topics
2. Include key timestamps for important points
