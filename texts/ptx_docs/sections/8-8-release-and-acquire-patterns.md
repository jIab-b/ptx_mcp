## 8.8. Release and Acquire Patterns

Some sequences of instructions give rise to patterns that participate in memory synchronization as described later. The *release* pattern makes prior operations from the current thread1 visible to some operations from other threads. The *acquire* pattern makes some operations from other threads visible to later operations from the current thread.

A *release* pattern on a location M consists of one of the following:

1. A *release* operation on M E.g.: `st.release [M];` or `atom.release [M];` or `mbarrier.arrive.release [M];`
2. Or a *release* or *acquire-release* operation on M followed by a *strong* write on M in *program order* E.g.: `st.release [M]`; `st.relaxed [M];`
3. Or a *release* or *acquire-release* *memory fence* followed by a *strong* write on M in *program order* E.g.: `fence.release; st.relaxed [M];` or `fence.release; atom.relaxed [M];`
4. Or a *release* or *acquire-release memory fence* followed in *program order* by an asynchronous operation that performs a *strong* write on M E.g.: `fence.release; cp.async.bulk.global.shared.relaxed.sys.b128 [M];`
5. Or a *release* asynchronous operation that performs a *strong* write on M E.g.: `st.async.release.sys [M];`

Any *memory synchronization* established by a *release* pattern only affects operations occurring in *program order* before the first instruction in that pattern.

An *acquire* pattern on a location M consists of one of the following:

1. An *acquire* operation on M E.g.: `ld.acquire [M];` or `atom.acquire [M];` or `mbarrier.test_wait.acquire [M];`
2. Or a *strong* read on M followed by an *acquire* operation on M in *program order* E.g.: `ld.relaxed [M]; ld.acquire [M];`
3. Or a *strong* read on M followed by an acquire *memory fence* in *program order* E.g.: `ld.relaxed [M]; fence.acquire;` or `atom.relaxed [M]; fence.acquire;`
4. Or first observing completion of an asynchronous operation that performs a *strong* read on M and then this observation is followed by an *acquire* memory fence in *program order* E.g.: `cp.async.bulk.mbarrier::complete_tx::bytes.relaxed.sys.b128 [dst], [M], size, [barrier];` // strong read on M `mbarrier.try_wait.relaxed p, [barrier];` // observes completion of async op that performs strong read on M `@p fence.acquire;` // acquire fence in program order after observing completion

Any *memory synchronization* established by an *acquire* pattern only affects operations occurring in *program order* after the last instruction in that pattern.

Note that while atomic reductions conceptually perform a strong read as part of its read-modify-write sequence, this strong read does not form an acquire pattern.

> E.g.: `red.add [M], 1; fence.acquire;` is not an acquire pattern.

1 For both *release* and *acquire* patterns, this effect is further extended to operations in other threads through the transitive nature of *causality order*.
