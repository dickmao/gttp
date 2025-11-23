PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin

.PHONY: install uninstall

install:
	@if command -v uv >/dev/null 2>&1; then \
		uv tool install youtube_transcript_api; \
	elif command -v pipx >/dev/null 2>&1; then \
		pipx install youtube_transcript_api; \
	else \
		pip3 install --user youtube_transcript_api; \
	fi
	install -d $(BINDIR)
	install -m 755 summarize.py $(BINDIR)/gttp

uninstall:
	rm -f $(BINDIR)/gttp
	@if command -v uv >/dev/null 2>&1; then \
		uv tool uninstall youtube_transcript_api 2>/dev/null || true; \
	elif command -v pipx >/dev/null 2>&1; then \
		pipx uninstall youtube_transcript_api 2>/dev/null || true; \
	else \
		pip3 uninstall -y youtube_transcript_api 2>/dev/null || true; \
	fi
