##### 9.7.10.4.2. Fabric-read completion mechanism

All fabric operations that read data from shared memory support tracking the completion of the read operation. This enables applications to reuse the shared memory read by these operations without waiting for the entire operation to complete. This is a partial completion mechanism, that is, it does not track completion of an entire asynchronous operation.

Note that since `fabric.try_get` does not read from shared memory - it writes to it - this completion mechanism does not provide any ordering for `try_get` operations.
