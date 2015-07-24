LYRICS_DIR="/usr/local/bin/lyrics.d"
LYRICS_FILE="/usr/local/bin/lyrics"

install:
	@chmod u+x run.sh
	@[ -d $(LYRICS_DIR) ] || mkdir $(LYRICS_DIR)
	@cp *.* $(LYRICS_DIR)
	@echo "#!/bin/bash" > $(LYRICS_FILE)
	@echo "cd $(LYRICS_DIR) && ./run.sh" >> $(LYRICS_FILE)
	@chmod u+x $(LYRICS_FILE)
