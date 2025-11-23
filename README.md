# gttp

**Get to the point** - YouTube transcript fetcher and summarizer for Claude CLI.

## Installation

```bash
make install
```

## Usage

In any Claude CLI session:

```bash
/gttp [https://www.youtube.com/watch?v=VIDEO_ID]
```

If no URL is provided, Claude will prompt you for one.

The command will:
1. Fetch the full transcript with timestamps
2. Provide a detailed summary organized by topics
3. Keep the transcript in context for follow-up queries

## Follow-up queries

After the initial summary, you can:
- Ask for shorter or longer versions
- Query specific timestamps or topics
- Request additional analysis

## Requirements

- Claude CLI
- Python 3
- uv (for dependency management)
