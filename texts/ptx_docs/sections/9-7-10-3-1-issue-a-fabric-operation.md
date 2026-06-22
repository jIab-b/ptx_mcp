##### 9.7.10.3.1. Issue a Fabric Operation

A thread initiates fabric operations by executing any of the following fabric instructions:

- `fabric.try_get`: read from CFT Handle
- `fabric.try_put`: write to CFT Handle
- `fabric.try_red`: reduction to CFT Handle
- `fabric.try_pullred`: pull-reduction from CFT handle (`multimem.ld_reduce` equivalent).
