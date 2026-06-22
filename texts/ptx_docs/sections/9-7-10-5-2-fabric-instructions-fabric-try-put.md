##### 9.7.10.5.2. Fabric Instructions: `fabric.try_put`

`fabric.try_put`

Asynchronous copy to fabric handle.

Syntax

```
fabric.try_put.async{.multimem}.src.completion_mechanism0.sem.scope.b128 [dstLeId, dstDataOff], [src], size, [bar];

fabric.try_put.async{.multimem}.src.completion_mechanism0.cp_mask.sem.scope.b128 [dstLeId, dstDataOff], [src], size, [bar], bytemask;

fabric.try_put.async{.multimem}.src.completion_mechanism1.sem.scope.b128 [dstLeId, dstDataOff, dstCounterOff], [src], size, [bar];

.src = { .shared::cta }
.completion_mechanism0 = { .mbarrier::complete_tx::16B.mbarrier::report::fabric }
.completion_mechanism1 = { .mbarrier::complete_tx::16B.mbarrier::report::fabric.counted::bytes }
.sem = { .relaxed }
.scope = { .sys }
```

Description

Asynchronously copies `size` bytes from `[src]` to destination fabric handle `[dstLeId, dstDataOff]`, where `dstLeId` is a 32-bit unsigned value denoting the logical endpoint identifier, and `dstDataOff` is a 64-bit unsigned value denoting the base offset of the resource to access within the logical endpoint associated with `dstLeId`.

The `size` operand is 32 bits and specifies the number of bytes to be copied. It must be a multiple of 16; otherwise, the behavior is undefined. The range `[src, src + size - 1]` must be in bounds of the source memory space. The range `[dstDataOff, dstDataOff + size - 1]` must be in bounds of the resource at the logical endpoint associated with `dstLeId` on the current device.

The source pointer `src` and the destination handle offset `dstDataOff` must be 16-byte aligned.

If the modifier `.multimem` is specified, then `dstLeId` must be associated with a multicast logical endpoint and the device that issues the operation must be a member of that endpoint. In the absence of the `.multimem` modifier, `dstLeId` must be associated with a unicast logical endpoint.

If `.src` is `.shared::cta`, then the source of the copy `[src]` and the barrier `[bar]` refer to the local CTAâs shared memory.

The `mbarrier` object `bar` must be initialized with `.layout::v1` (see [Layouts of the mbarrier object](#parallel-synchronization-and-communication-instructions-mbarrier-object-layout)). Qualifier `.mbarrier::complete_tx::16B` specifies that the complete-tx operation is performed on `bar` with completion count equal to the number of bytes copied divided by 16; that is, the count is incremented by 1 for every 16 bytes copied. Note that this completion mechanism differs from `fabric.try_get`, where the complete-tx operation uses a completion count equal to the number of bytes copied. For any thread to observe completion of fabric operations via an `mbarrier` object, the issuing thread is required to submit those operations before the barrier phase tracking these operations advances.

If the modifier `.counted::bytes` is present (`completion_mechanism1` form), then:

- `dstLeId` must be associated with a logical endpoint with counted completion support ([Counted completion mechanism](#fabric-counted-completion-mechanism)), and
- the counter offset `dstCounterOff` must be 256-byte aligned, and
- this operation provides counter-based completion for destination data using a 256-byte-aligned counter of size 8 bytes spcified at `[dstLeId, dstCounterOff]`.

The `.counted::bytes` modifier is incompatible with the `.cp_mask` modifier.

Refer to [Fabric Reporting Mechanism](#fabric-reporting-mechanism) for the description of `.mbarrier::report::fabric`.

If `.cp_mask` is specified, the `bytemask` operand is required and must contain a 16-bit-wide mask to select which bytes of each 16-byte chunk are written to the destination.

This instruction accesses the data and the counter at the locations specified by the handle operands through the fabric-proxy, reads from the source `.shared::cta` through the async-proxy, and updates the `mbarrier` object in `.shared::cta` through the generic-proxy.

The completion of this operation may be observed by waiting at the barrier via *CTA-scope* operations. Threads must submit `fabric` operations and wait for their completion before grid exit; otherwise, the behavior is undefined.

This operation has `.relaxed.sys` memory-order semantics as described in the [Memory Consistency Model](#memory-consistency-model).

PTX ISA Notes

Introduced in PTX ISA version 9.3.

Target ISA Notes

Requires `sm_100` or higher.

Examples

```
fabric.try_put.async.shared::cta.mbarrier::complete_tx::16B.mbarrier::report::fabric.relaxed.sys.b128 [dstLeId, dstLeOffData], [srcSmem], 0x100, [mbar];

fabric.try_put.async.counted::bytes.shared::cta.mbarrier::complete_tx::16B.mbarrier::report::fabric.relaxed.sys.b128 [dstLeId, dstLeOffData, dstLeOffCntr], [srcSmem], size, [mbar];
```
