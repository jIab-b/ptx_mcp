###### 9.7.17.10.7.1. Valid combinations of scale_vectorsize with types and MMA-Kind

The shape of *scale_A* and *scale_B* matrices depend on the `.scale_vectorsize` as shown in [Table 59](#tcgen05-mma-scale-valid-comb).

**Table 59 Valid combinations of scale_vectorsize and shapes**

| .scale_vectorsize | .kind::* | K | Shape of scale_A | Shape of scale_B |
| --- | --- | --- | --- | --- |
| `.scale_vec::1X` | `.kind::mxf8f6f4` | All supported values of K | M x 1 | 1 x N |
| `.scale_vec::2X` | `.kind::mxf4`, `.kind::mxf4nvf4` | All supported values of K | M x 2 | 2 x N |
| `.scale_vec::4X` | `.kind::mxf4nvf4` | All supported values of K | M x 4 | 4 x N |
| `.block16` | `.kind::mxf4nvf4` | K = 96 | M x 6 | 6 x N |
| `.block16` | `.kind::mxf4nvf4` | All supported values of K except 96 | M x 4 | 4 x N |
| `.block32` | `.kind::mxf4`, `.kind::mxf4nvf4` | K = 96 | M x 3 | 3 x N |
| `.block32` | `.kind::mxf4`, `.kind::mxf4nvf4` | All supported values of K except 96 | M x 2 | 2 x N |
| `.block32` | `.kind::mxf8f6f4` | All supported values of K | M x 1 | 1 x N |

The valid combination of the exact element types and the `.scale_vectorsize` are listed in [Table 60](#tcgen05-mma-scale-valid-comb-detail).

**Table 60 Valid combinations of scale_vectorsize with types and MMA-Kind**

| .kind::* | Element Data Type | Scale Data Type | .scale_vectorsize |
| --- | --- | --- | --- |
| `.kind::mxf8f6f4` | E4M3, E5M2, E2M3 E3M2, E2M1 | UE8M0 | `.scale_vec::1X` / `.block32` |
| `.kind::mxf4` | E2M1 | UE8M0 | `.scale_vec::2X` / `.block32` |
| `.kind::mxf4nvf4` | E2M1 | UE8M0 | `.scale_vec::2X` / `.block32`, `.scale_vec::4X` / `.block16` |
| `.kind::mxf4nvf4` | E2M1 | UE4M3 | `.scale_vec::4X` / `.block16` |

New `.blockN` qualifiers are aliases for `.scale_vec::NX` qualifiers as:

- `.block32` is alias for `.scale_vec::1X` or `.scale_vec::2X` based on `.kind` and K dimension
- `.block16` is alias for `.scale_vec::4X`
