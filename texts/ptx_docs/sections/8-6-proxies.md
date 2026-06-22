## 8.6. Proxies

A *memory proxy*, or a *proxy* is an abstract label applied to a method of memory access. When two memory operations use distinct methods of memory access, they are said to be different *proxies*.

A *proxy fence* is required to synchronize memory operations across different *proxies*. Although virtual aliases use the *generic* method of memory access, since using distinct virtual addresses behaves as if using different *proxies*, they require a *proxy fence* to establish memory ordering.

Unless otherwise specified, memory operations as defined in [Operation types](#operation-types) use *generic* method of memory access, i.e. a *generic proxy*. Operations using methods of access distinct from the *generic* method include:

- textures and surface accesses,
- accesses to the same location via the same proxy using distinct virtual memory addresses,
- async-proxy and tensormap-proxy accesses by .async.bulk operations,
- fabric-proxy accesses by fabric operations.
