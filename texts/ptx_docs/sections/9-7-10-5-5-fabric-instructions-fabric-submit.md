##### 9.7.10.5.5. Fabric Instructions: `fabric.submit`

`fabric.submit`

Submits prior fabric operations issued by the current thread.

Syntax

```
fabric.submit{.submitop};

.submitop = { .op_restrict::fetching }
```

Description

Submits prior fabric operations issued by the current thread. For any thread to observe completion of fabric operations via an `mbarrier` object, the issuing thread is required to submit those operations before the barrier phase tracking these operations advances. Otherwise, the behavior is undefined. See [Life of a Fabric Operation](#fabric-operations-lifecycle).

If `.op_restrict::fetching` is specified, then only prior `fabric.try_get` and `fabric.try_pullred` operations issued by the current thread are submitted. Otherwise, all prior fabric operations issued by the current thread are submitted.

This operation has no effect on fabric operations that have already been submitted.

PTX ISA Notes

Introduced in PTX ISA version 9.3.

Target ISA Notes

Requires `sm_100` or higher.

Examples

```
fabric.submit.op_restrict::fetching;

fabric.submit;
```
