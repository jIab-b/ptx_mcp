###### 9.7.15.6.2.3. Matrix Fragments for sparse `mma.m16n8k16` with `.tf32` floating point type

A warp executing sparse `mma.m16n8k16` with `.tf32` floating point type will compute an MMA operation of shape `.m16n8k16`.

Elements of the matrix are distributed across the threads in a warp so each thread of the warp holds a fragment of the matrix.

- Multiplicand A: The layout of the fragments held by different threads is shown in [Figure 123](#sparse-mma-16816-tf32-a). The row and column of a matrix fragment can be computed as:
  .atype
  
  Fragment
  
  Elements
  
  `.tf32`
  
  A vector expression containing four `.b32` registers, with each register containing one non-zero `.tf32` element out of 2 consecutive elements from matrix A.
  
  Mapping of the non-zero elements is as described in [Sparse matrix storage](#warp-level-sparse-matrix-storage).
  Figure 123 Sparse MMA .m16n8k16 fragment layout for matrix A with `.tf32` type.
  ```
  groupID = %laneid >> 2
  threadID_in_group = %laneid % 4
  
  row =      groupID            for a0 and a2
             groupID + 8        for a1 and a3
  
  col = [firstcol ... lastcol]  // As per the mapping of non-zero elements
                                // as described in Sparse matrix storage
  
  Where
  firstcol = threadID_in_group * 2          for a0 and a1
             (threadID_in_group * 2) + 8    for a2 and a3
  lastcol  = firstcol + 1
  ```
- Multiplicand B: The layout of the fragments held by different threads is shown in [Figure 124](#sparse-mma-16816-tf32-b).
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.tf32`
  
  A vector expression containing four `.b32` registers, each containing four `.tf32` elements from matrix B.
  
  b0, b1, b2, b3
  Figure 124 Sparse MMA .m16n8k16 fragment layout for matrix B with `.tf32` type.
- Matrix fragments for accumulators C and D are the same as in case of [Matrix Fragments for mma.m16n8k16 with floating point type](#warp-level-matrix-fragment-mma-16816-float).
- Metadata: A `.b32` register containing 8 4-bit vectors each storing the index of a non-zero element of a 2-wide chunk of matrix A as shown in [Figure 125](#sparse-mma-metadata-16816-tf32).
  Figure 125 Sparse MMA .m16n8k16 metadata layout for `.tf32` type.
