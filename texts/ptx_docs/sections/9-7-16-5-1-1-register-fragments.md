###### 9.7.16.5.1.1. Register Fragments

This section describes the organization of various matrices located in register operands of the `wgmma.mma_async` instruction.

9.7.16.5.1.1.1.

Matrix Fragments for

wgmma.mma_async.m64nNk16

ï

A warpgroup executing `wgmma.mma_async.m64nNk16` will compute an MMA operation of shape `.m64nNk16` where N is a valid `n` dimension as listed in [Matrix Shape](#asynchronous-warpgroup-level-matrix-shape).

Elements of the matrix are distributed across the threads in a warpgroup so each thread of the warpgroup holds a fragment of the matrix.

- Multiplicand A in registers: The layout of the fragments held by different threads is shown in [Figure 148](#wgmma-64n16-a).
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.f16`/`.bf16`
  
  A vector expression containing four `.f16x2` registers, with each register containing two `.f16`/ `.bf16` elements from matrix A.
  
  a0, a1, a2, a3, a4, a5, a6, a7
  Figure 148 WGMMA .m64nNk16 register fragment layout for matrix A.
- Accumulator D: The layout of the fragments held by different threads is shown in [Figure 149](#wgmma-64n16-d).
  .dtype
  
  Fragment
  
  Elements (low to high)
  
  `.f16`
  
  A vector expression containing N/4 number of `.f16x2` registers, with each register containing two `.f16` elements from matrix D.
  
  d0, d1, d2, d3, â¦, dX, dY, dZ, dW
  
  where `X = N/2Â  -Â  4`
  
  `Y = N/2Â  -Â  3`
  
  `Z = N/2Â  -Â  2`
  
  `W = N/2Â  -Â  1`
  
  `N = 8*i where i = {1, 2, ... , 32}`
  
  `.f32`
  
  A vector expression containing N/2 number of `.f32` registers.
  Figure 149 WGMMA .m64nNk16 register fragment layout for accumulator matrix D.

9.7.16.5.1.1.2.

Matrix Fragments for

wgmma.mma_async.m64nNk8

ï

A warpgroup executing `wgmma.mma_async.m64nNk8` will compute an MMA operation of shape `.m64nNk8` where N is a valid `n` dimension as listed in [Matrix Shape](#asynchronous-warpgroup-level-matrix-shape).

Elements of the matrix are distributed across the threads in a warpgroup so each thread of the warpgroup holds a fragment of the matrix.

- Multiplicand A in registers: The layout of the fragments held by different threads is shown in [Figure 150](#wgmma-64n8-a).
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.tf32`
  
  A vector expression containing four `.b32` registers containing four `.tf32` elements from matrix A.
  
  a0, a1, a2, a3
  Figure 150 WGMMA .m64nNk8 register fragment layout for matrix A.
- Accumulator D: The layout of the fragments held by different threads is shown in [Figure 151](#wgmma-64n8-d).
  .dtype
  
  Fragment
  
  Elements (low to high)
  
  `.f32`
  
  A vector expression containing N/2 number of `.f32` registers.
  
  d0, d1, d2, d3, â¦, dX, dY, dZ, dW
  
  where `X = N/2Â  -Â  4`
  
  `Y = N/2Â  -Â  3`
  
  `Z = N/2Â  -Â  2`
  
  `W = N/2Â  -Â  1`
  
  `N = 8*i where i = {1, 2, ... , 32}`
  Figure 151 WGMMA .m64nNk8 register fragment layout for accumulator matrix D.

9.7.16.5.1.1.3.

Matrix Fragments for

wgmma.mma_async.m64nNk32

ï

A warpgroup executing `wgmma.mma_async.m64nNk32` will compute an MMA operation of shape `.m64nNk32` where N is a valid `n` dimension as listed in [Matrix Shape](#asynchronous-warpgroup-level-matrix-shape).

Elements of the matrix are distributed across the threads in a warpgroup so each thread of the warpgroup holds a fragment of the matrix.

- Multiplicand A in registers: The layout of the fragments held by different threads is shown in [Figure 152](#wgmma-64n32-a).
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.s8`/`.u8`
  
  A vector expression containing four `.b32` registers, with each register containing four `.u8`/ `.s8` elements from matrix A.
  
  a0, a1, a2, a3, â¦ , a14, a15
  
  `.e4m3`/ `.e5m2`
  
  A vector expression containing four `.b32` registers, with each register containing four `.e4m3`/ `.e5m2` elements from matrix A.
  Figure 152 WGMMA .m64nNk32 register fragment layout for matrix A.
- Accumulator D: The layout of the fragments held by different threads is shown in [Figure 153](#wgmma-64n32-d).
  .dtype
  
  Fragment
  
  Elements (low to high)
  
  Miscellaneous Information
  
  `.s32`
  
  A vector expression containing N/2 number of `.s32` registers.
  
  d0, d1, d2, d3, â¦, dX, dY, dZ, dW
  
  where `X = N/2Â  -Â  4`
  
  `Y = N/2Â  -Â  3`
  
  `Z = N/2Â  -Â  2`
  
  `W = N/2Â  -Â  1`
  
  `N` depends on .dtype, as described in the next column.
  
  `N = 8*i where i = {1, 2, 3, 4}`
  
  > `= 16*i where i = {3, 4, ..., 15, 16}`
  
  `.f32`
  
  A vector expression containing N/2 number of `.f32` registers.
  
  `N = 8*i where i = {1, 2, ... , 32}`
  
  `.f16`
  
  A vector expression containing N/4 number of `.f16x2` registers, with each register containing two `.f16` elements from matrix D.
  Figure 153 WGMMA .m64nNk32 register fragment layout for accumulator matrix D.

9.7.16.5.1.1.4.

Matrix Fragments for

wgmma.mma_async.m64nNk256

ï

A warpgroup executing `wgmma.mma_async.m64nNk256` will compute an MMA operation of shape `.m64nNk256` where N is a valid `n` dimension as listed in [Matrix Shape](#asynchronous-warpgroup-level-matrix-shape).

Elements of the matrix are distributed across the threads in a warpgroup so each thread of the warpgroup holds a fragment of the matrix.

- Multiplicand A in registers: The layout of the fragments held by different threads is shown in [Figure 154](#wgmma-64n256-a).
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.b1`
  
  A vector expression containing four `.b32` registers, with each register containing thirty two `.b1` element from matrix A.
  
  a0, a1, a2, â¦, a127
  Figure 154 WGMMA .m64nNk256 register fragment layout for matrix A.
- Accumulator D: The layout of the fragments held by different threads is shown in [Figure 155](#wgmma-64n256-d).
  .dtype
  
  Fragment
  
  Elements (low to high)
  
  `.s32`
  
  A vector expression containing N/2 number of `.s32` registers.
  
  d0, d1, d2, d3, â¦, dX, dY, dZ, dW
  
  where `X = N/2Â  -Â  4`
  
  `Y = N/2Â  -Â  3`
  
  `Z = N/2Â  -Â  2`
  
  `W = N/2Â  -Â  1`
  
  `N = 8*i where i = {1, 2, 3, 4}`
  
  `= 16*i where i = {3, 4, ..., 15, 16}`
  Figure 155 WGMMA .m64nNk256 register fragment layout for accumulator matrix D.
