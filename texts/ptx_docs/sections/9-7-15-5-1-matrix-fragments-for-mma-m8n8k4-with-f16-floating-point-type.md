##### 9.7.15.5.1. Matrix Fragments for `mma.m8n8k4` with `.f16` floating point type

A warp executing `mma.m8n8k4` with `.f16` floating point type will compute 4 MMA operations of shape `.m8n8k4`.

Elements of 4 matrices need to be distributed across the threads in a warp. The following table shows distribution of matrices for MMA operations.

| MMA Computation | Threads participating in MMA computation |
| --- | --- |
| MMA computation 1 | Threads with `%laneid` 0-3 (low group) and 16-19 (high group) |
| MMA computation 2 | Threads with `%laneid` 4-7 (low group) and 20-23 (high group) |
| MMA computation 3 | Threads with `%laneid` 8-11 (low group) and 24-27 (high group) |
| MMA computation 4 | Threads with `%laneid` 12-15 (low group) and 28-31 (high group) |

For each of the individual MMA computation shown above, each of the required thread holds a fragment of the matrix for performing mma operation as follows:

- Multiplicand A: The layout of the fragments held by different threads is shown below:
  .atype
  
  Fragment
  
  Elements (low to high)
  
  `.f16`
  
  A vector expression containing two `.f16x2` registers, with each register containing two `.f16` elements from the matrix A.
  
  a0, a1, a2, a3
  - Fragment layout for Row Major matrix A is shown in [Figure 46](#mma-884-a-row-f16). The row and column of a matrix fragment can be computed as:
    Figure 46 MMA .m8n8k4 fragment layout for row-major matrix A with `.f16` type
    ```
    row =            %laneid % 4          if %laneid < 16
                    (%laneid % 4) + 4     otherwise
    
    col =            i                    for ai where i = {0,..,3}
    ```
  - Fragment layout for Column Major matrix A is shown in [Figure 47](#mma-884-a-col-f16). The layout of the fragments held by different threads is shown below: The row and column of a matrix fragment can be computed as:
    Figure 47 MMA .m8n8k4 fragment layout for column-major matrix A with `.f16` type
    ```
    row =        i % 4            for ai  where i = {0,..,3}   if %laneid < 16
                (i % 4) + 4       for ai  where i = {0,..,3}   otherwise
    
    col =        %laneid % 4
    ```
- Multiplicand B: The layout of the fragments held by different threads is shown below:
  .btype
  
  Fragment
  
  Elements (low to high)
  
  `.f16`
  
  A vector expression containing two `.f16x2` registers, with each register containing two `.f16` elements from the matrix B.
  
  b0, b1, b2, b3
  - Fragment layout for Row Major matrix B is shown in [Figure 48](#mma-884-b-row-f16). The row and column of a matrix fragment can be computed as:
    Figure 48 MMA .m8n8k4 fragment layout for row-major matrix B with `.f16` type
    ```
    row =        %laneid % 4
    
    col =         i      for bi   where i = {0,..,3}   if %laneid < 16
                 i+4     for bi   where i = {0,..,3}   otherwise
    ```
  - Fragment layout for Column Major matrix B is shown in [Figure 49](#mma-884-b-col-f16). The row and column of a matrix fragment can be computed as:
    Figure 49 MMA .m8n8k4 fragment layout for column-major matrix B with `.f16` type
    ```
    row =       i                 for bi   where i = {0,..,3}
    
    col =      %laneid % 4        if %laneid < 16
              (%laneid % 4) + 4   otherwise
    ```
- Accumulators C (or D): The layout of the fragments held by different threads is shown below:
  .ctype / .dtype
  
  Fragment
  
  Elements (low to high)
  
  `.f16`
  
  A vector expression containing four `.f16x2` registers, with each register containing two `.f16` elements from the matrix C (or D).
  
  c0, c1, c2, c3, c4, c5, c6, c7
  
  `.f32`
  
  A vector expression of eight `.f32` registers.
  - Fragment layout for accumulator matrix when `.ctype` is `.f16` is shown in [Figure 50](#mma-884-c-f16). The row and column of a matrix fragment can be computed as:
    Figure 50 MMA .m8n8k4 fragment layout for matrix C/D with `.ctype` = `.f16`
    ```
    row =       %laneid % 4         if %laneid < 16
               (%laneid % 4) + 4    otherwise
    
    col =          i                for ci   where i = {0,..,7}
    ```
  - Fragment layout for accumulator matrix when `.ctype` is `.f32` is shown in [Figure 51](#mma-884-c-f32-1) and [Figure 52](#mma-884-c-f32-2). The row and column of a matrix fragment can be computed as:
    Figure 51 MMA .m8n8k4 computation 1 and 2 fragment layout for matrix C/D with `.ctype` = `.f32`
    Figure 52 MMA .m8n8k4 computation 3 and 4 fragment layout for matrix C/D with `.ctype` = `.f32`
    ```
    row =     X           if %laneid < 16
            X + 4         otherwise
    
              where X = (%laneid & 0b1) + (i & 0b10)  for ci where i = {0,..,7}
    
    col = (i & 0b100) + (%laneid & 0b10) + (i & 0b1)  for ci where i = {0,..,7}
    ```
