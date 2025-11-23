PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin

.PHONY: install uninstall

install:
	pipx install youtube_transcript_api || pip3 install --user youtube_transcript_api
	install -d $(BINDIR)
	install -m 755 summarize.py $(BINDIR)/gttp

uninstall:
	rm -f $(BINDIR)/gttp
	pipx uninstall youtube_transcript_api 2>/dev/null || pip3 uninstall -y youtube_transcript_api 2>/dev/null || true
