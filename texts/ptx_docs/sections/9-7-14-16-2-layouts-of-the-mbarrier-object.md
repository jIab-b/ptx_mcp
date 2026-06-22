##### 9.7.14.16.2. Layouts of the mbarrier object

An opaque *mbarrier object* supports two different layouts:

- `.layout::v0`
- `.layout::v1`

The exact layout of the *mbarrier object* can be specified at the time of creation. The asynchronous operations that can be tracked by an *mbarrier object* depend on the layout. Refer to [Contents of the mbarrier object](#parallel-synchronization-and-communication-instructions-mbarrier-contents) for more details.
