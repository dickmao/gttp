#!/bin/bash
VIDEO_ID=$(echo "$1" | sed 's/.*v=\([^&]*\).*/\1/')
youtube_transcript_api "$VIDEO_ID" --format text | claude -p "Summarize this YouTube transcript:"
