HYDE=../bin/hyde

gen:
	$(HYDE) gen
	$(HYDE) gen
serve: gen
	$(HYDE) serve
