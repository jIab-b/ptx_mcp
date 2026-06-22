##### 9.7.10.4.1. Fabric Reporting Mechanism

Fabric operations tracked by mbarrier use the `report::fabric` reporting mechanism with the following semantics:

- If the operation succeeds, the payload report ([contents of the mbarrier object](#parallel-synchronization-and-communication-instructions-mbarrier-contents)) is not modified. In other words, report predicate and report value both remain unchanged.
- Otherwise, the operation fails, the mbarrier report predicate is set, and the opaque report value may contain more information, which may be decoded via the [cudaFabricOpErrorStatusGet/Count](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__FABRIC.html) APIs.

The behavior of a program that combines fabric operations specifying `report::fabric` with other operations specifying different reporting mechanism is undefined.
