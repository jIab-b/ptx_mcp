###### 9.7.14.16.5.2. Conditional phase

The primary phase of an mbarrier object advances upon completion of arrivals, and transaction-count updates of asynchronous operations tracked by the mbarrier. The conditional phase advances if the primary phase advances, and no asynchronous operation tracked by the mbarrier prevents it via a [report-on](#parallel-synchronization-and-communication-instructions-mbarrier-report-on) operation.

Mbarrier objects with `.layout::v0` do not support tracking asynchronous operations that could prevent the conditional phase from advancing via [report-on](#parallel-synchronization-and-communication-instructions-mbarrier-report-on), resulting in both phases advancing in unison. That is, either both phase advance, or no phase advances.

Mbarrier objects with `.layout::v1` support tracking asynchronous operations that can prevent the conditional phase from advancing via a [report-on](#parallel-synchronization-and-communication-instructions-mbarrier-report-on) operation. If the primary phase advances, but the conditional phase does not advance, the payload report is non-zero and may contain more information. If the conditional phase advances, the payload report is zero.

An mbarrier object is automatically reinitialized upon completion of the current primary phase for immediate use in the next phase. Refer [Phase Completion of the mbarrier object](#parallel-synchronization-and-communication-instructions-mbarrier-phase-completion) for more details on conditional phase completion.
