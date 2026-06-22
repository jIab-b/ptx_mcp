##### 9.7.14.16.7. Tracking successful completion of an operation using the mbarrier object

An mbarrier object with layout `.layout::v1` can track asynchronous operations that prevent the conditional phase from advancing and provide additional information via the payload report on completion.

The `mbarrier.test_wait` and `mbarrier.try_wait` instructions with `.phase_type::primary` allow observing primary phase completion and the payload report. The payload report consists of a report predicate (`reportPredicate`) and a report value (`reportValue`). For the conditional phase to advance, the entire payload report must be zero. If the predicate i.e. `reportPredicate` is zero, the value `reportValue` is guaranteed to be zero and therefore the conditional phase has advanced.

The `mbarrier.test_wait` and `mbarrier.try_wait` instructions with `.phase_type::conditional` allow observing the conditional phase advance which means the payload report was zero.
