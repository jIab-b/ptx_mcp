##### 9.7.17.10.1. Transpose and Negate operations

The matrices `A` and `B` can be transposed by specifying the Tranpose `A` Matrix and Transpose `B` Matrix bits in the instruction descriptor respectively.

The elements of the matrices `A` and `B` can be negated by specifying the Negate `A` Matrix and Negate `B` Matrix bits in the instruction descriptor respectively.

The support for Transpose and Negate operation for various MMA-Kind are shown in [Table 54](#tcgen05-transpose-negate-mma-kind).

**Table 54 Transpose and Negate operation for various MMA-Kind**

| MMA-Kind | Is Transpose A/B supported | Is Negate A/B supported |
| --- | --- | --- |
| `.kind::tf32` | Yes | Yes |
| `.kind::f16` | Yes | Yes |
| `.kind::f8f6f4` | Yes | Yes |
| `.kind::mxf8f6f4` | Yes | Yes |
| `.kind::i8` | Yes | No |
| `.kind::mxf4` | No | Yes |
| `.kind::mxf4nvf4` | No | Yes |

For `.kind::tf32`, the transpose operations on matrices `A` and `B` are supported only with 128B swizzling mode with 32B swizzle-atomicity.

For all other MMA-Kinds, the transpose operations on matrices `A` and `B` are not supported on 128B swizzling mode with 32B swizzle-atomicity.

[Table 55](#tcgen05-kind-shapes-8b-transpose-b) shows the valid combinations of N shape with `.cta_group` qualifier for 8bit transpose B.

**Table 55 Various combinations of N shape with .cta_group qualifier for 8bit transpose B**

| .cta_group | N shape |
| --- | --- |
| 1 | 16 <= N <= 256, step 16 |
| 2 | 32 <= N <= 256, step 32 |
