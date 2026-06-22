##### 9.7.10.3.2. Submit and then arrive at mbarrier

For any thread to observe completion of fabric operations via an `mbarrier` object, the issuing thread is required to submit those operations before the barrier phase tracking these operations advances. Otherwise, the behavior is undefined.

A single `arrive expect_tx` operation can be issued for multiple and different types of fabric operations tracked by the same barrier.
