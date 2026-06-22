##### 9.7.15.5.2. Matrix Fragments for `mma.m8n8k4` with `.f64` floating point type

A warp executing `mma.m8n8k4` with `.f64` floating point type will compute an MMA operation of shape `.m8n8k4`.

Elements of the matrix are distributed across the threads in a warp so each thread of the warp holds a fragment of the matrix.

- Multiplicand A: The layout of the fragments held by different threads is shown in [Figure 53](#mma-884-a-f64). The row and column of a matrix fragment can be computed as:
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.f64`
  
  A vector expression containing a single `.f64` register, containing single `.f64` element from the matrix A.
  
  a0
  Figure 53 MMA .m8n8k4 fragment layout for matrix A with `.f64` type
  ```
  row =        %laneid >> 2
  
  col =        %laneid % 4
  ```
- Multiplicand B: The layout of the fragments held by different threads is shown in [Figure 54](#mma-884-b-f64). The row and column of a matrix fragment can be computed as:
  .btype
  
  Fragment
  
  Elements (low to high)
  
  `.f64`
  
  A vector expression containing a single `.f64` register, containing a single `.f64` element from the matrix B.
  
  b0
  Figure 54 MMA .m8n8k4 fragment layout for matrix B with `.f64` type
  ```
  row =        %laneid % 4
  
  col =        %laneid >> 2
  ```
- Accumulators (C or D): The layout of the fragments held by different threads is shown in [Figure 55](#mma-884-c-f64). The row and column of a matrix fragment can be computed as:
  .ctype / .dtype
  
  Fragment
  
  Elements (low to high)
  
  `.f64`
  
  A vector expression containing of two `.f64` registers containing two `.f64` elements from the matrix C.
  
  c0, c1
  Figure 55 MMA .m8n8k4 fragment layout for accumulator matrix C/D with `.f64` type
  ```
  groupID           = %laneid >> 2
  threadID_in_group = %laneid % 4
  
  row =      groupID
  
  col =      (threadID_in_group * 2) + (i & 0x1)       for ci   where i = {0, 1}
  ```
