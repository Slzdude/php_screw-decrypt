#ifndef  ZENCODE_H
#define ZENCODE_H
#include <stdio.h>
#include <stdlib.h>
#include <zlib.h>
#include <string.h>

char *zencode(char *inbuf, int inbuf_len, int *resultbuf_len);

char *zdecode(char *inbuf, int inbuf_len, int *resultbuf_len);
#endif