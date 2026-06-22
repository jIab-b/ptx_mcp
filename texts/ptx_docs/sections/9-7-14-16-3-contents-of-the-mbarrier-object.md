##### 9.7.14.16.3. Contents of the mbarrier object

An opaque *mbarrier object* irrespective of the layout keeps track of the following information :

- Current primary and conditional phases of the *mbarrier object*
- Count of pending arrivals for the current phase of the *mbarrier object*
- Count of expected arrivals for the next phase of the *mbarrier object*
- Count of pending asynchronous memory operations (or transactions) tracked by the current phase of the *mbarrier object*. This is also referred to as *tx-count*.

However, an *mbarrier object* with `.layout::v1` additionally keeps track of the following information:

- Payload report corresponding to each primary phase

An *mbarrier object* progresses through a sequence of phases where each phase is defined by threads performing an expected number of [arrive-on](#parallel-synchronization-and-communication-instructions-mbarrier-arrive-on) operations.

The valid range of each of the counts differs based on the mbarrier layout. Refer [Table 37](#mbarrier-counts) for more details.

**Table 37 Mbarrier counts for different layouts**

| Layout | Count name | Minimum value | Maximum value |
| --- | --- | --- | --- |
| `.layout::v0` | Expected arrival count | 1 | 220 - 1 |
| `.layout::v0` | Pending arrival count | 0 | 220 - 1 |
| `.layout::v0` | tx-count | -(220 - 1) | 220 - 1 |
| `.layout::v1` | Expected arrival count | 1 | 29 - 1 |
| `.layout::v1` | Pending arrival count | 0 | 29 - 1 |
| `.layout::v1` | tx-count | -(220 - 1) | 220 - 1 |
