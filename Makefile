.PHONY: install uninstall

install:
	install -d $(HOME)/.claude/commands
	install -d $(HOME)/.local/bin
	install -m 644 gttp.md $(HOME)/.claude/commands/
	install -m 755 gttp.py $(HOME)/.local/bin/

uninstall:
	rm -f $(HOME)/.claude/commands/gttp.md
	rm -f $(HOME)/.local/bin/gttp.py
