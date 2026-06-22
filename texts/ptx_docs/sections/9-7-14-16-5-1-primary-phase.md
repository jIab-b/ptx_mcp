###### 9.7.14.16.5.1. Primary phase

The primary phase of an *mbarrier object* is the number of times the *mbarrier object* has been used to synchronize threads and [asynchronous](#program-order-async-operations) operations. In each primary phase {0, 1, 2, â¦}, threads perform in program order :

- [arrive-on](#parallel-synchronization-and-communication-instructions-mbarrier-arrive-on) operations to complete the current primary phase and
- *test_wait* / *try_wait* operations to check for the completion of the current primary phase.

An *mbarrier object* is automatically reinitialized upon completion of the current primary phase for immediate use in the next phase. The current primary phase is incomplete and all prior primary phases are complete.

For each primary phase of the mbarrier object, at least one *test_wait* or *try_wait* operation must be performed which returns `True` for `waitComplete` before an [arrive-on](#parallel-synchronization-and-communication-instructions-mbarrier-arrive-on) operation in the subsequent primary phase.
