# c flag
override CFLAGS += -g -Wall
# remove files
RM = rm - rf
# create diretories
MKDIR = mkdir -p
# binary files route setting
BIN_DIR = ../bin/chapter2

build:
	$(MKDIR) $(BIN_DIR)
	@echo Compiling apue/chapter2 c files
	$(CC) $(CFLAGS) get_openmax.c -o $(BIN_DIR)/get_openmax
	$(CC) $(CFLAGS) get_pathmax.c -o $(BIN_DIR)/get_pathmax
	$(CC) $(CFLAGS) printconf.c -o $(BIN_DIR)/printconf

clean:
	$(RM) $(BIN_DIR)
