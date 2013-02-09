HYDE=../bin/hyde

gen:
	rm -rv deploy/*
	$(HYDE) gen
	$(HYDE) gen
serve: gen
	$(HYDE) serve
