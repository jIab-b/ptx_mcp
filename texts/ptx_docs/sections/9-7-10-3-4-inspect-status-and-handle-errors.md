##### 9.7.10.3.4. Inspect status and handle errors

A single operation like `fabric.try_put` may issue many requests, and each of the requests may fail for a different reason. The failures are [reported on](#parallel-synchronization-and-communication-instructions-mbarrier-report-on) the *mbarrier* objects.

Multiple different fabric operations may also be tracked by the same *mbarrier* object and fail for different reasons.

The `mbarrier.try_wait.phase_type::primary` operation that notifies the program of completion sets the report predicate if there were any errors; the opaque report value may contain more information. See [fabric reporting mechanism](#fabric-reporting-mechanism) for details. The application can then decide how to handle the errors based on their severity nature.
