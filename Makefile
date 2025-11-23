.PHONY: install uninstall

install:
	@if ! command -v uv >/dev/null 2>&1; then \
		echo "Error: uv is required. Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh" >&2; \
		exit 1; \
	fi
	install -d $(HOME)/.claude/commands
	install -d $(HOME)/.local/bin
	install -m 644 gttp.md $(HOME)/.claude/commands/
	install -m 755 gttp.py $(HOME)/.local/bin/

uninstall:
	rm -f $(HOME)/.claude/commands/gttp.md
	rm -f $(HOME)/.local/bin/gttp.py
