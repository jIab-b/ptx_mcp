##### 9.7.14.16.8. Phase Completion of the mbarrier object

The requirements for completion of the current phase are described below. Upon completion of the current phase, the phase transitions to the subsequent phase as described below.

**Current primary phase completion requirements**

An *mbarrier object* irrespective of the layout completes the current primary phase when all of the following conditions are met:

- The count of the pending arrivals has reached zero.
- The *tx-count* has reached zero.

**Current conditional phase completion requirements**

An *mbarrier object* completes the current conditional phase when all of the following conditions are met:

- The count of the pending arrivals has reached zero.
- The *tx-count* has reached zero.
- If the layout of the mbarrier is `.layout::v1`, then the payload report associated with the primary phase was zero.

**Phase transition**

When an *mbarrier* object with `.layout::v0` completes the current phase, the following actions are performed atomically:

- The *mbarrier object* transitions to the next primary and conditional phases.
- The pending arrival count is reinitialized to the expected arrival count.

When an *mbarrier* object with `.layout::v1` completes the current phase, the following actions are performed atomically:

- If the payload report associated with the current primary phase of the mbarrier is zero, then the conditional phase advances.
- The *mbarrier object* transitions to the next primary phase.
- The payload report corresponding to the next primary phase is reinitialized to zero.
- The pending arrival count is reinitialized to the expected arrival count.
