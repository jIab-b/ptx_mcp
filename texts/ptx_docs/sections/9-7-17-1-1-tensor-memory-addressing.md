##### 9.7.17.1.1. Tensor Memory Addressing

Tensor Memory addresses are 32-bit wide and specify two components.

1. Lane index
2. Column index

The layout is as follows:

> |  |  |
> | --- | --- |
> | 31 16 | 15 0 |
> | Lane index | Column index |

[Figure 182](#tensor-memory-layout) shows the view of the Tensor Memory Layout within CTA.

Figure 182 Tensor Memory Layout and Addressing
