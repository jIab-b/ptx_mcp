###### 9.7.17.10.7.3. Scale Factor B ID

The value of the scale factor `B ID` selects the sub-columns in the Tensor Memory to form the scale factor `B` matrix, which is used to scale the matrix `B`.

The following shows the scale factor matrix layout for various scale vector sizes:

9.7.17.10.7.3.1.

Layout of the Scale Factor B Matrix for scale_vec::1X/block32 with K=32/K=64

ï

There is one scale factor per row of the `B` matrix with block size as 32 and the scale factor must be provided in 1-byte aligned sub-column of the Tensor Memory. *SFB_ID* specifies the byte offset in the Tensor Memory word that must be used for the scale factor matrix. [Figure 240](#tcgen05-mma-scale-factor-b-1x-dig) shows which sub-columns get selected for different values of *SFB_ID*.

Figure 240 Layout of scale factor B matrix with scale_vec::1X/block32 with K=32/K=64

For example, if *SFB_ID* is 0, then all the green columns are selected to form the scale factor matrix. Similarly, *SFB_ID* values of 1, 2 and 3 would select the blue, yellow, and red columns, respectively.

9.7.17.10.7.3.2.

Layout of the Scale Factor B Matrix for scale_vec::2X/block32 with K=64/K=128

ï

There are two scale factors per row of the `B` matrix with block size as 32 and the scale factor must be provided in 2-byte aligned sub-column of the Tensor Memory. *SFB_ID* specifies the half word offset in the Tensor Memory word that must be used for the scale factor matrix. [Figure 241](#tcgen05-mma-scale-factor-b-2x-dig) shows which sub-columns get selected for different values of *SFB_ID*.

Figure 241 Layout of scale factor B matrix with scale_vec::2X/block32 with K=64/K=128

For example, if *SFB_ID* is 0, then all the green columns are selected to form the scale factor matrix. Similarly, if *SFB_ID* is 2, then all of the blue columns are selected to form the scale factor matrix.

9.7.17.10.7.3.3.

Layout of the Scale Factor B Matrix for scale_vec::4X/block16 with K=64/K=128

ï

There are four scale factors per row of the `B` matrix with block size as 16 and the scale factor must be provided in 4-byte aligned sub-column of the Tensor Memory. The *SFB_ID* value must be 0 and this specifies that all of the columns (in green) will be used for the scale factor matrix. [Figure 242](#tcgen05-mma-scale-factor-b-4x-dig) shows which sub-columns get selected for different values of *SFB_ID*.

Figure 242 Layout of scale factor B matrix with scale_vec::4X/block16 with K=64/K=128

9.7.17.10.7.3.4.

Layout of the Scale Factor B Matrix for block32 with K=96 (Semantically equivalent to scale_vec::3X)

ï

There are three scale factors per row of the `B` matrix with block size as 32 and the scale factor must be provided in 4-byte aligned sub-column of the Tensor Memory. *SFB_ID* specifies the byte offset in the Tensor Memory word that must be used for the scale factor matrix.

For N<=128, [Figure 243](#tcgen05-mma-scale-factor-b-block32-k96-nlt128-dig1), [Figure 244](#tcgen05-mma-scale-factor-b-block32-k96-nlt128-dig2), [Figure 245](#tcgen05-mma-scale-factor-b-block32-k96-nlt128-dig3) and [Figure 246](#tcgen05-mma-scale-factor-b-block32-k96-nlt128-dig4) show which sub-columns get selected for different values of *SFB_ID*.

Figure 243 Layout of scale factor B matrix with block32 with K=96 and N<=128 with SFB_ID=00

Figure 244 Layout of scale factor B matrix with block32 with K=96 and N<=128 with SFB_ID=01

Figure 245 Layout of scale factor B matrix with block32 with K=96 and N<=128 with SFB_ID=10

Figure 246 Layout of scale factor B matrix with block32 with K=96 and N<=128 with SFB_ID=11

For N>128, [Figure 247](#tcgen05-mma-scale-factor-b-block32-k96-ngt128-dig1), [Figure 248](#tcgen05-mma-scale-factor-b-block32-k96-ngt128-dig2), [Figure 249](#tcgen05-mma-scale-factor-b-block32-k96-ngt128-dig3), [Figure 250](#tcgen05-mma-scale-factor-b-block32-k96-ngt128-dig4), [Figure 251](#tcgen05-mma-scale-factor-b-block32-k96-ngt128-dig5) and [Figure 252](#tcgen05-mma-scale-factor-b-block32-k96-ngt128-dig6) show which sub-columns get selected for different values of *SFB_ID*.

Figure 247 Layout of scale factor B matrix with block32 with K=96 and N>128 with SFB_ID=00

Figure 248 Layout of scale factor B matrix with block32 with K=96 and N>128 with SFB_ID=01

Figure 249 Layout of scale factor B matrix with block32 with K=96 and N>128 with SFB_ID=10

Figure 250 Layout of scale factor B matrix with block32 with K=96 and N>128 with SFB_ID=10

Figure 251 Layout of scale factor B matrix with block32 with K=96 and N>128 with SFB_ID=11

Figure 252 Layout of scale factor B matrix with block32 with K=96 and N>128 with SFB_ID=11

For example, if *SFB_ID* is 0, then all the green columns are selected to form the scale factor matrix. Similarly, *SFB_ID* values of 1, 2 and 3 would select the blue, yellow, and red columns, respectively.

9.7.17.10.7.3.5.

Layout of the Scale Factor B Matrix for block16 with K=96 (Semantically equivalent to scale_vec::6X)

ï

There are six scale factors per row of the `B` matrix with block size as 16 and the scale factor must be provided in 4-byte aligned sub-column of the Tensor Memory. *SFB_ID* specifies the byte offset in the Tensor Memory word that must be used for the scale factor matrix.

For N<=128, [Figure 253](#tcgen05-mma-scale-factor-b-block16-k96-nlt128-dig1) and [Figure 254](#tcgen05-mma-scale-factor-b-block16-k96-nlt128-dig2) show which sub-columns get selected for different values of *SFB_ID*.

Figure 253 Layout of scale factor B matrix with block16 with K=96 and N<=128 with SFB_ID=00

Figure 254 Layout of scale factor B matrix with block16 with K=96 and N<=128 with SFB_ID=10

For N>128, [Figure 255](#tcgen05-mma-scale-factor-b-block16-k96-ngt128-dig1), [Figure 256](#tcgen05-mma-scale-factor-b-block16-k96-ngt128-dig2), [Figure 257](#tcgen05-mma-scale-factor-b-block16-k96-ngt128-dig3) and [Figure 258](#tcgen05-mma-scale-factor-b-block16-k96-ngt128-dig4) show which sub-columns get selected for different values of *SFB_ID*.

Figure 255 Layout of scale factor B matrix with block16 with K=96 and N>128 with SFB_ID=00

Figure 256 Layout of scale factor B matrix with block16 with K=96 and N>128 with SFB_ID=00

Figure 257 Layout of scale factor B matrix with block16 with K=96 and N>128 with SFB_ID=10

Figure 258 Layout of scale factor B matrix with block16 with K=96 and N>128 with SFB_ID=10

For example, if *SFB_ID* is 0, then all the green columns are selected to form the scale factor matrix. Similarly, if *SFB_ID* is 2, then all of the blue columns are selected to form the scale factor matrix.
