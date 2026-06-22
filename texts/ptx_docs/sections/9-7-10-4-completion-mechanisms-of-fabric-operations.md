#### 9.7.10.4. Completion mechanisms of fabric operations

The completion of fabric operations can be tracked by mbarrier objects of type [layout::v1](#parallel-synchronization-and-communication-instructions-mbarrier-object-layout). For details refer to [mbarrier based completion mechanism](#data-movement-and-conversion-instructions-asynchronous-copy-completion-mechanisms-mbarrier). Observing completion of a fabric operation provides ordering for all memory accesses and CFT Handle resource accesses performed by the operation, irrespective of whether any errors were reported or not.

In addition to tracking the completion of the fabric operation, a subset of operation effects, such as waiting on reads from shared memory, waiting on changes in a counter value, etc., can also be tracked independently from the entire completion of the operation.
