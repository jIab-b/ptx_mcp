#### 9.7.17.6. Memory Consistency Model for 5th generation of TensorCore operations

Ordering of `tcgen05` instructions is described in terms of two key concepts:

1. Pipelined tcgen05 instructions
2. Specialized tcgen05-specific inter-thread synchronization mechanisms.

These concepts combine to form four canonical synchronization patterns, as described further below.
