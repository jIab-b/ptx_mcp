##### 9.7.14.16.6. Tracking asynchronous operations by the mbarrier object

Starting with the Hopper architecture (`sm_9x`), *mbarrier object* supports a new count, called *tx-count*, which is used for tracking the completion of asynchronous memory operations or transactions. *tx-count* tracks the number of asynchronous transactions, in units specified by the asynchronous memory operation, that are outstanding and yet to be complete.

The *tx-count* of an *mbarrier object* must be set to the total amount of asynchronous memory operations, in units as specified by the asynchronous operations, to be tracked by the current phase. Upon completion of each of the asynchronous operations, the [complete-tx](#parallel-synchronization-and-communication-instructions-mbarrier-complete-tx-operation) operation will be performed on the *mbarrier object* and thus progress the mbarrier towards the completion of the current phase.
