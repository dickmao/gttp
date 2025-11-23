.PHONY: install uninstall

install:
	@if command -v uv >/dev/null 2>&1; then \
		uv tool install --force youtube-transcript-api; \
	elif command -v pipx >/dev/null 2>&1; then \
		pipx install --force youtube-transcript-api; \
	else \
		pip3 install --user --upgrade youtube-transcript-api; \
	fi
	install -d $(HOME)/.claude/commands
	install -d $(HOME)/.local/bin
	install -m 644 gttp.md $(HOME)/.claude/commands/
	install -m 755 gttp.py $(HOME)/.local/bin/

uninstall:
	rm -f $(HOME)/.claude/commands/gttp.md
	rm -f $(HOME)/.local/bin/gttp.py
