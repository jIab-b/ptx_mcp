##### 9.7.17.10.6. Shared Memory Layout and Swizzling

If the bit `Transpose A Matrix` / `Transpose B Matrix` in the [Instruction descriptor](#tcgen05-instruction-descriptor) is 0, then *K-major* is used for matrix `A` / `B` respectively. If the bit `Transpose A Matrix` in the [Instruction descriptor](#tcgen05-instruction-descriptor) is 1 then *M-major* is used for matrix `A`. If the bit `Transpose B Matrix` in the [Instruction descriptor](#tcgen05-instruction-descriptor) is 1, then *N-major* is used for matrix `B`.

In a column-major default BLAS library such as cuBLAS, the matrices `A` and `B` with and without transpose can be classified as either *K-Major* or *M-or-N-Major* as shown in the following table:

|  | Non-Transposed | Transposed |
| --- | --- | --- |
| A | K-major | M-major |
| B | K-major | N-major |

To avoid confusion with `A`, `B`, `row-major`, `col-major`, `transpose`, and `non-transpose`, we will use *MN-Major* and *K-Major* throughout this section.

The matrices in the shared memory are made up of one or more âswizzle layout atomâ. The exact layout of these swizzle atoms depends on the swizzling mode, swizzle-atomicity, and the leading dimension. The layout of the swizzle are shown in [Table 58](#tcgen05-smem-swizzle-mode)

**Table 58 Layout for swizzle atoms**

| Swizzling mode and Swizzle-Atomicity | Leading Dimension | Swizzle atom layout (128b element) |
| --- | --- | --- |
| 128B Swizzling with 32B atomicity | M/N | 8x4 |
| 128B Swizzling with 32B atomicity | â | â |
| 128B Swizzling with 16B atomicity | M/N | 8x8 |
| 128B Swizzling with 16B atomicity | K | 8x8 |
| 64B Swizzling Mode | M/N | 4x8 |
| 64B Swizzling Mode | K | 8x4 |
| 32B Swizzling Mode | M/N | 2x8 |
| 32B Swizzling Mode | K | 8x2 |
| None | M/N | 1x8 |
| None | K | 8x1 |

The above shapes are for elements of size 128 bits. For smaller element sizes, the same shapes would get multiplied along the leading dimension by a factor of `128 / sizeof_bits(Element)`. For example, 128B MN major swizzle atom would have a shape of (8*(128/32))x8 = 32x8 for tf32 tensor core inputs.

Some example Layouts of *MxK* or *KxN* matrices with various swizzling modes, and are in units of 128b elements as shown by each colored cell as shown in [Figure 219](#tcgen05-smem-layout-128b-32b-atom-mn), [Figure 220](#tcgen05-smem-layout-128b-mn), [Figure 221](#tcgen05-smem-layout-128b-k), [Figure 222](#tcgen05-smem-layout-64b-mn), [Figure 223](#tcgen05-smem-layout-64b-k), [Figure 224](#tcgen05-smem-layout-32b-mn), [Figure 225](#tcgen05-smem-layout-32b-k), [Figure 226](#tcgen05-smem-layout-no-swizzle-mn), [Figure 227](#tcgen05-smem-layout-no-swizzle-k).

Figure 219 MN major 128B swizzling with 32B atomicity

Figure 220 MN major 128B swizzling

Figure 221 K major 128B swizzling

Figure 222 MN major 64B swizzling

Figure 223 K major 64B swizzling

Figure 224 MN major 32B swizzling

Figure 225 K major 32B swizzling

Figure 226 MN major no-swizzling mode

Figure 227 K major no-swizzling mode

Following are some of the examples of the 128B swizzling layout for `tf32` element type.

- K-Major: [Figure 228](#tcgen05-smem-layout-k)
  Figure 228 K major
- MN-Major: [Figure 229](#tcgen05-smem-layout-mn)
  Figure 229 MN major
