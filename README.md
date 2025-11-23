# gttp

**Get to the point** - YouTube transcript fetcher and summarizer for Claude CLI.

## Installation

Copy the slash command to your global Claude CLI commands directory:

```bash
cp gttp.md ~/.claude/commands/
```

## Usage

In any Claude CLI session:

```bash
/gttp https://www.youtube.com/watch?v=VIDEO_ID
```

The command will:
1. Auto-install `youtube_transcript_api` if needed (via uv/pipx/pip)
2. Fetch the full transcript with timestamps
3. Provide a detailed summary organized by topics
4. Keep the transcript in context for follow-up queries

## Follow-up queries

After the initial summary, you can:
- Ask for shorter or longer versions
- Query specific timestamps or topics
- Request additional analysis

## Requirements

- Claude CLI
- Python 3
- One of: uv, pipx, or pip3 (for auto-installing dependencies)
