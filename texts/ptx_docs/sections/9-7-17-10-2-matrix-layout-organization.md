##### 9.7.17.10.2. Matrix Layout Organization

[Table 56](#tcgen05-matrices-majorness) describes the major-ness used for different matrices.

**Table 56 Major-ness for different matrices**

| Matrix | Residing in Memory | Default Major-ness |
| --- | --- | --- |
| D | Tensor Memory | Row-Major |
| A | Tensor Memory | Row-Major |
| A | Shared Memory | Depends on swizzling mode. Refer [Shared Memory Layout and Swizzling](#tcgen05-shared-memory-layout-swizzling) |
| B | Shared Memory | Depends on swizzling mode. Refer [Shared Memory Layout and Swizzling](#tcgen05-shared-memory-layout-swizzling) |
