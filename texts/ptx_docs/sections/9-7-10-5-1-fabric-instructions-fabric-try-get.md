##### 9.7.10.5.1. Fabric Instructions: `fabric.try_get`

`fabric.try_get`

Asynchronous copy from fabric handle.

Syntax

```
fabric.try_get.async.dst.completion_mechanism.sem.scope.b128 [dst], [srcLeId, srcDataOff], size, [bar];

.dst = { .shared::cta }
.completion_mechanism = { .mbarrier::complete_tx::bytes.mbarrier::report::fabric }
.sem = { .relaxed }
.scope = { .sys }
```

Description

Asynchronously copies `size` bytes from fabric handle `[srcLeId, srcDataOff]` to destination memory `[dst]`, where `srcLeId` is a 32-bit unsigned value denoting the logical endpoint identifier, and `srcDataOff` is a 64-bit unsigned value denoting the base offset of the resource to access within the logical endpoint associated with `srcLeId`.

The logical endpoint associated with `srcLeId` must be a unicast logical endpoint.

The `size` operand is 32 bits and specifies the number of bytes to be copied. It must be a multiple of 16; otherwise, the behavior is undefined. The range `[dst, dst + size - 1]` must be in bounds of the destination memory space. The range `[srcDataOff, srcDataOff + size - 1]` must be in bounds of the logical endpoint resources associated with `srcLeId`.

The source handle offset `srcDataOff` and destination pointer `dst` must be 16-byte aligned.

If `.dst` is `.shared::cta`, then:

- The destination of the copy `[dst]` and the barrier `[bar]` must refer to the local CTAâs shared memory; otherwise, the behavior is undefined.
- The completion mechanism must be `.mbarrier::complete_tx::bytes.mbarrier::report::fabric`.

The `mbarrier` object `bar` must be initialized with `.layout::v1` (see [Layouts of the mbarrier object](#parallel-synchronization-and-communication-instructions-mbarrier-object-layout)). Qualifier `.mbarrier::complete_tx::bytes` specifies that the operation completes by performing a [complete-tx operation](#parallel-synchronization-and-communication-instructions-mbarrier-complete-tx-operation) with the total number of bytes copied (`size`) on mbarrier object at the location specified by the address operand `bar`. Refer to [Fabric Reporting Mechanism](#fabric-reporting-mechanism) for the description of `.mbarrier::report::fabric`. For any thread to observe completion of fabric operations via an `mbarrier` object, the issuing thread is required to submit those operations before the barrier phase tracking these operations advances.

This instruction reads the data at the location specified by the handle operand through the fabric-proxy, copies it to the destination `.shared::cta` memory through the async-proxy, and updates the `mbarrier` object in `.shared::cta` through the generic-proxy.

The completion of this operation may be observed by waiting at the barrier via *CTA-scope* operations. Threads must submit `fabric` operations and wait for their completion before grid exit; otherwise, the behavior is undefined.

Accesses to a source handle are 128-bit-wide atomic with `.relaxed.sys` memory-order semantics as described in the [Memory Consistency Model](#memory-consistency-model).

PTX ISA Notes

Introduced in PTX ISA version 9.3.

Target ISA Notes

Requires `sm_100` or higher.

Examples

```
fabric.try_get.async.shared::cta.mbarrier::complete_tx::bytes.mbarrier::report::fabric.relaxed.sys.b128 [dstSmem], [srcLeId, srcLeOff], 0x100, [mbar];

fabric.try_get.async.shared::cta.relaxed.sys.mbarrier::complete_tx::bytes.mbarrier::report::fabric.b128 [dstSmem], [srcLeId, srcLeOff], sizeBytes, [mbar];
```
