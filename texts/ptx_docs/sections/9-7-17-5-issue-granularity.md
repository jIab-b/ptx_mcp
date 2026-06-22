#### 9.7.17.5. Issue Granularity

Each of the `tcgen05` operation has different requirements for the number of threads/warps that needs to issue them.

The following table lists the execution granularity requirements of each of the `tcgen05` operation:

**Table 49 Execution granularity requirements for tcgen05 operations**

| tcgen05 operation | .cta_group | Issue Granularity |
| --- | --- | --- |
| .mma, .cp, .shift, .commit | ::1 | An issue from a single thread in the current CTA would initiate the base operation. |
| .mma, .cp, .shift, .commit | ::2 | Issue from a single thread from the [CTA-Pair](#tcgen05-cta-pair) would initiate the base operation. When the current CTA issues the operation, the peer CTA should be active and should not have exited. |
| .alloc, .dealloc, .relinquish_alloc_permit | ::1 | Issue from a single warp in the current CTA would initiate the allocation management instruction. |
| .alloc, .dealloc, .relinquish_alloc_permit | ::2 | Issue from two warps, one in each of the current CTA and its [Peer CTA](#tcgen05-peer-cta), in order to collectively perform the operation, i.e., the first warp to perform the operation could block until the the second warp in the [Peer CTA](#tcgen05-peer-cta) also performs the operation (see examples below). |
| .ld, .st, .wait::{ld, st} | N/A | Issue from a warp in the current CTA can access only 1/4 of the Tensor Memory of the current CTA. So, a warpgroup is needed to access the entire Tensor Memory of the current CTA. |
| .fence::* | N/A | A thread needs to fence all its accesses to the tensor memory that it wants to order with other accesses to the tensor memory from other threads. |

The following example shows that:

- Before attempting to deallocate Tensor Memory, it suffices to ensure that there are no concurrent Tensor Memory accesses from the [Peer CTA](#tcgen05-peer-cta).
- Warps can immediately exit after deallocating Tensor Memory; no extra synchronization required.

**Table 50 Example of deallocating Tensor Memory before CTA exit.**

| CTA0 Warp | CTA1 Warp |
| --- | --- |
| barrier.cluster.arrive; barrier.cluster.wait; tcgen05.dealloc.2cta.sync.aligned; exit; | barrier.cluster.arrive; barrier.cluster.wait; tcgen05.dealloc.2cta.sync.aligned; exit; |

This example uses a cluster barrier for illustration purposes but in practice other synchronization mechanisms are often used.

The following example illustrates a scenario in which the program exhibits non-deterministic behavior due to incorrect synchronizaton because `.dealloc` may or may not block:

**Table 51 Example of non-determinstic hang due to incorrect synchronization**

| CTA0 Warp | CTA1 Warp |
| --- | --- |
| barrier.cluster.arrive; barrier.cluster.wait; tcgen05.dealloc.2cta.sync.aligned; exit; | tcgen05.dealloc.2cta.sync.aligned; barrier.cluster.arrive; barrier.cluster.wait; exit; |
