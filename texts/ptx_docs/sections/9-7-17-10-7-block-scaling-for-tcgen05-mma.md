##### 9.7.17.10.7. Block Scaling for `tcgen05.mma`

The `tcgen05.mma` instructions with the following `.kind` qualifier:

- `.kind::mxf8f6f4`
- `.kind::mxf4`
- `.kind::mxf4nvf4`

perform matrix multiplication with block scaling. This operation has the following form:

`(A * scale_A)Â  * (B * scale_B) + D`

where `scale_A` and `scale_B` are matrices residing in [Tensor Memory](#tensor-memory).

For a `scale_A` matrix of shape *M x SFA_N*, each row of matrix `A` is divided into *SFA_N* number of chunks and each chunk of a row is multiplied with the corresponding element in the *SF_A* of the same row.

Similarly, for a `scale_B` matrix of shape *SFB_M x N*, each column of matrix `B` is divided into the *SFB_M* number of chunks and each chunk of a column is multiplied with the corresponding element in the *SF_B* of the same column.

Scale factors for `A` and `B` matrices need to be duplicated to all 32 lane partitions of tensor memory.

[Figure 230](#tcgen05-mma-block-scaling) shows an example of `tcgen05.mma` with block scaling of `scale_vec::2X`.

Figure 230 `tcgen05.mma` with block scaling of `scale_vec::2X`
