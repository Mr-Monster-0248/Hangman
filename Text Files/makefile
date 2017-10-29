version = python3.5
target = Text_files.py
file = test.txt

#To run List_of_word.py cleanly
clean: run
	@rm -rf __pycache__

run:
	@${version} ${target}

#To protect the word file
safe:
	@cp ${file} ${file}.save
	@${version} ${target}
	@rm -rf __pycache__
