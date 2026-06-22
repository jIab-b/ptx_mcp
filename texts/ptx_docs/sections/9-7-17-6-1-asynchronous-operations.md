##### 9.7.17.6.1. Asynchronous Operations

The tcgen05 family of instructions are divided into 2 categories:

1. Asynchronous instructions: These `tcgen05` operations are not inherently ordered with respect to other `tcgen05` operations in the same thread (unless pipelined as mentioned below).
2. Synchronous instructions: These `tcgen05` operations are inherently ordered with respect to other `tcgen05` operations in the same order. The Tensor Memory allocation related instructions that access shared memory maintain same-address ordering with respect to non-`tcgen05` instructions.

The following table lists the category of each of the `tcgen05` instruction:

| tcgen05.* operation | Category |
| --- | --- |
| `.alloc` | Synchronous instructions |
| `.dealloc` | Synchronous instructions |
| `.relinquish_alloc_permit` | Synchronous instructions |
| `.fence::*` | Synchronous instructions |
| `.wait::*` | Synchronous instructions |
| `.commit` | Synchronous instructions |
| `.mma` | Asynchronous instructions |
| `.cp` | Asynchronous instructions |
| `.shift` | Asynchronous instructions |
| `.ld` | Asynchronous instructions |
| `.st` | Asynchronous instructions |
