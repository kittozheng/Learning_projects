# c flag
override CFLAGS += -g -Wall
# romove files
RM=rm -rf
# create directories
MKDIR=mkdir -p
# binary files route
BIN_DIR=../bin/chapter1

build:
	$(MKDIR) $(BIN_DIR)
	@echo Compiling apue/chapter1 c files
	$(CC) $(CFLAGS) exec_cmd_from_stdin.c -o $(BIN_DIR)/exec_cmd_from_stdin
	$(CC) $(CFLAGS) exec_cmd_from_stdin2.c -o $(BIN_DIR)/exec_cmd_from_stdin2
	$(CC) $(CFLAGS) ls.c -o $(BIN_DIR)/ls
	$(CC) $(CFLAGS) printerror.c -o $(BIN_DIR)/printerror
	$(CC) $(CFLAGS) printid.c -o $(BIN_DIR)/printid
	$(CC) $(CFLAGS) printpid.c -o $(BIN_DIR)/printpid
	$(CC) $(CFLAGS) stdin2stdout.c -o $(BIN_DIR)/stdin2stdout

clean:
	$(RM) $(BIN_DIR)
