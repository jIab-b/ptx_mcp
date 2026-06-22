##### 9.7.10.4.3. Counted completion mechanism

Fabric operations support tracking the completion of the destination data accesses performed by `try_put` and `try_red` using a global memory counter. It enables programs to wait on data modifications by observing the counter updates. Multiple fabric operations may share the same counter concurrently. Since concurrent operations are not ordered with respect to each other, programs must wait on the counter reaching a final value.

This mechanism increments a counter by one for each byte of data accessed. The granularity at which counter updates occur is unspecified; updates may happen once per byte, once collectively at the end of the operation, or any granularity in between. The 8B-wide counter must be 256B aligned, and the counter increment is a system-scope atomic operation.

If counter and data overlap, the behavior is undefined. If the logical endpoint lacks support for counted completion, the behavior is undefined (refer to the [Logical Endpoint section of the CUDA Driver API](https://docs.nvidia.com/cuda/cuda-driver-api/cuda-driver-api/group__CUDA__LOGICAL__ENDPOINT.html#logical-endpoint) for details).

This is a partial completion mechanism that programs can use to wait on destination data accesses. For `.multimem` fabric operations with counted completion, counters only track accesses at their destination device.
