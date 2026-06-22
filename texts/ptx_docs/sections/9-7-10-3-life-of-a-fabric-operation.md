#### 9.7.10.3. Life of a Fabric Operation

The lifecycle of a handle starts and ends in the host,when the host-side of the CUDA application detects whether the system supports fabric operations, creates logical endpoints, binds resources to the logical endpoints, and shares them with other GPUs in the *NVLink* domain. To enable remote source accesses the logical endpoint readiness should be queried. The lifecycle of a fabric operation starts and ends in the device. This section only covers the PTX device-side programming model of fabric operations; refer to the [Logical Endpoint section of the CUDA Driver API](https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__LOGICAL__ENDPOINT.html#logical-endpoint) for the end-to-end programming model of fabric operations spanning host-code and device-code.

The lifecycle of fabric operations includes:

- Threads issue one or more fabric operations tracked by an `mbarrier.layout::v1`.
- Each thread submits the fabric operations before the associated *mbarrier phase* completes.
- Threads arrive-on and expect-tx at the *mbarrier phase* to ensure it advances once the fabric operations complete.
- Threads wait until the *mbarrier phase* completes.
- Threads inspect the predicate report for errors, and handle them. The status report may contain additional information about the errors.
