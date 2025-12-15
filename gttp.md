---
allowed-tools: Bash
argument-hint: [youtube-url]
description: Summarize YouTube video transcript
---

# YouTube Transcript Summary

Fetch the transcript using the command below and provide a detailed summary.

```bash
uv run --with youtube-transcript-api python3 ~/.local/bin/gttp.py $1
```

Then read and summarize the full transcript from the file it outputs.

Based on the full transcript:
1. Provide a comprehensive summary organized by main topics
2. Include key timestamps for important points
3. Highlight any actionable insights or conclusions

Note: You can ask me to make the summary shorter or longer, or inquire about specific timestamps or topics from the transcript.
