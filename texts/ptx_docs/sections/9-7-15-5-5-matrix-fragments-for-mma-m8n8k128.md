##### 9.7.15.5.5. Matrix Fragments for `mma.m8n8k128`

A warp executing `mma.m8n8k128` will compute an MMA operation of shape `.m8n8k128`.

Elements of the matrix are distributed across the threads in a warp so each thread of the warp holds a fragment of the matrix.

- Multiplicand A: The layout of the fragments held by different threads is shown in [Figure 62](#mma-88128-a). The row and column of a matrix fragment can be computed as:
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.b1`
  
  A vector expression containing a single `.b32` register, containing thirty two `.b1` elements from the matrix A.
  
  a0, a1, â¦ a30, a31
  Figure 62 MMA .m8n8k128 fragment layout for matrix A with `.b1` type.
  ```
  groupID           = %laneid >> 2
  threadID_in_group = %laneid % 4
  
  row =  groupID
  
  col =  (threadID_in_group * 32) + i       for ai where i = {0,..,31}
  ```
- Multiplicand B: The layout of the fragments held by different threads is shown in [Figure 63](#mma-88128-b). The row and column of a matrix fragment can be computed as:
  .btype
  
  Fragment
  
  Elements (low to high)
  
  `.b1`
  
  A vector expression containing a single `.b32` register, containing thirty two `.b1` elements from the matrix B.
  
  b0, b1, â¦, b30, b31
  Figure 63 MMA .m8n8k128 fragment layout for matrix B with `.b1` type.
  ```
  groupID           = %laneid >> 2
  threadID_in_group = %laneid % 4
  
  row = (threadID_in_group * 32) + i         for bi where i = {0,..,31}
  
  col = groupID
  ```
- Accumulators (C or D): The layout of the fragments held by different threads is shown in [Figure 64](#mma-88128-c). The row and column of a matrix fragment can be computed as:
  .ctype / .dtype
  
  Fragment
  
  Elements (low to high)
  
  `.s32`
  
  A vector expression containing two `.s32` registers, containing two `.s32` elements from the matrix C (or D).
  
  c0, c1
  Figure 64 MMA .m8n8k128 fragment layout for accumulator matrix C/D with `.s32` type
  ```
  groupID = %laneid >> 2
  threadID_in_group = %laneid % 4
  
  row =      groupID
  
  col =  (threadID_in_group * 2) + i    for ci where i = {0, 1}
  ```
