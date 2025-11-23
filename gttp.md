---
allowed-tools: Bash(python3:*)
argument-hint: [youtube-url]
description: Summarize YouTube video transcript
---

# YouTube Transcript Summary

$ARGUMENTS

If no YouTube URL was provided above, ask the user for the URL before proceeding.

Otherwise, fetch the transcript using the command below and provide a detailed summary.

!`python3 ~/.local/bin/gttp.py "$ARGUMENTS"`

Based on the full transcript above:
1. Provide a comprehensive summary organized by main topics
2. Include key timestamps for important points
3. Highlight any actionable insights or conclusions

Note: You can ask me to make the summary shorter or longer, or inquire about specific timestamps or topics from the transcript.
