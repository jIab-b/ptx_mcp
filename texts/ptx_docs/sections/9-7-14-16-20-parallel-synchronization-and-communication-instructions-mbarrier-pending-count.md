##### 9.7.14.16.20. Parallel Synchronization and Communication Instructions: `mbarrier.pending_count`

`mbarrier.pending_count`

Query the pending arrival count from the opaque mbarrier state.

Syntax

```
mbarrier.pending_count{.layout}.b64 count, state;

.layout = { .layout::v0 }
```

Description

The pending count can be queried from the opaque mbarrier state using `mbarrier.pending_count`.

The `state` operand is a 64-bit register that must be the result of a prior `mbarrier.arrive.noComplete` or `mbarrier.arrive_drop.noComplete` instruction. Otherwise, the behavior is undefined.

The destination register `count` is a 32-bit unsigned integer representing the pending count of the *mbarrier object* prior to the [arrive-on operation](#parallel-synchronization-and-communication-instructions-mbarrier-arrive-on) from which the `state` register was obtained. The optional qualifier `.layout::v0` denotes the layout of the corresponding mbarrier object as described in the section [Layouts of the mbarrier object](#parallel-synchronization-and-communication-instructions-mbarrier-object-layout).

PTX ISA Notes

Introduced in PTX ISA version 7.0.

Support for `.layout` qualifier introduced in PTX ISA version 9.3.

Target ISA Notes

Requires `sm_80` or higher.

Qualifier `.layout` requires `sm_90` or higher.

Examples

```
.reg .b32 %r1;
.reg .b64 state;
.shared .b64 shMem;

mbarrier.arrive.noComplete.b64 state, [shMem], 1;
mbarrier.pending_count.layout::v0.b64 %r1, state;
```
