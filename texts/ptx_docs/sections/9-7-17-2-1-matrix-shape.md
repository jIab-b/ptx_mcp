##### 9.7.17.2.1. Matrix Shape

The matrix multiply and accumulate operations support a limited set of shapes for the operand matrices `A`, `B` and `D`. The shapes of all three matrix operands are collectively described by the tuple *MxNxK* where `A` is *MxK* matrix, `B` is a *KxN* matrix, and `D` is a *MxN* matrix.

[Table 42](#tcgen05-kind-shapes) shows matrix shapes that are supported for the specified types for the `tcgen05.mma` operation.

**Table 42 Various combinations of .kind and shapes**

| Various Combinations | Various Combinations | Various Combinations | Various Combinations | Various Combinations | Various Combinations | Shapes Supported | Shapes Supported | Shapes Supported |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .kind::* | Has .ws | CTA Group | Sparsity | dtype | atype/btype | Shapes Supported | Shapes Supported | Shapes Supported |
| `kind::f16` | No `.ws` | 1 | Dense | `.f16` | `.f16` | 64xNxK 128xNxK | N = {8, 16, 24, â¦ 256} steps of 8 | K = 16 |
| `kind::f16` | No `.ws` | 1 | Dense | `.f32` | `.f16`, `.bf16` | 64xNxK 128xNxK | N = {8, 16, 24, â¦ 256} steps of 8 | K = 16 |
| `kind::f16` | No `.ws` | 1 | Sparse | `.f16` | `.f16` | 64xNxK 128xNxK | N = {8, 16, 24, â¦ 256} steps of 8 | K = 32 |
| `kind::f16` | No `.ws` | 1 | Sparse | `.f32` | `.f16`, `.bf16` | 64xNxK 128xNxK | N = {8, 16, 24, â¦ 256} steps of 8 | K = 32 |
| `kind::f16` | No `.ws` | 2 | Dense | `.f16` | `.f16` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 16 |
| `kind::f16` | No `.ws` | 2 | Dense | `.f32` | `.f16`, `.bf16` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 16 |
| `kind::f16` | No `.ws` | 2 | Sparse | `.f16` | `.f16` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 32 |
| `kind::f16` | No `.ws` | 2 | Sparse | `.f32` | `.f16`, `.bf16` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 32 |
| `kind::f16` | `.ws` | 1 | Dense | `.f16` | `.f16` | 32xNxK 64xNxK 128xNxK | N = {64, 128, 256} | K = 16 |
| `kind::f16` | `.ws` | 1 | Dense | `.f32` | `.f16`, `.bf16` | 32xNxK 64xNxK 128xNxK | N = {64, 128, 256} | K = 16 |
| `kind::f16` | `.ws` | 1 | Sparse | `.f16` | `.f16` | 32xNxK 64xNxK 128xNxK | N = {64, 128} | K = 32 |
| `kind::f16` | `.ws` | 1 | Sparse | `.f32` | `.f16`, `.bf16` | 32xNxK 64xNxK 128xNxK | N = {64, 128} | K = 32 |
| `kind::f16` | `.ws` | 2 | Either | `.f16` | `.f16` | Invalid | Invalid | Invalid |
| `kind::f16` | `.ws` | 2 | Either | `.f32` | `.f16`, `.bf16` | Invalid | Invalid | Invalid |
| `.kind::tf32` | No `.ws` | 1 | Dense | `.f32` | `.tf32` | 64xNxK 128xNxK | N = {8, 16, 24, â¦ 256} steps of 8 | K = 8 |
| `.kind::tf32` | No `.ws` | 1 | Sparse | `.f32` | `.tf32` | 64xNxK 128xNxK | N = {8, 16, 24, â¦ 256} steps of 8 | K = 16 |
| `.kind::tf32` | No `.ws` | 2 | Dense | `.f32` | `.tf32` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 8 |
| `.kind::tf32` | No `.ws` | 2 | Sparse | `.f32` | `.tf32` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 16 |
| `.kind::tf32` | `.ws` | 1 | Dense | `.f32` | `.tf32` | 32xNxK 64xNxK 128xNxK | N = {64, 128, 256} | K = 8 |
| `.kind::tf32` | `.ws` | 1 | Sparse | `.f32` | `.tf32` | 32xNxK 64xNxK 128xNxK | N = {64, 128} | K = 16 |
| `.kind::tf32` | `.ws` | 2 | Dense | `.f32` | `.tf32` | Invalid | Invalid | Invalid |
| `.kind::tf32` | `.ws` | 2 | Sparse | `.f32` | `.tf32` | Invalid | Invalid | Invalid |
| `.kind::f8f6f4` | No `.ws` | 1 | Dense | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | 64xNxK 128xNxK | N = {8, 16, â¦ 256} steps of 8 OR N = {16, 32, â¦ 256} steps of 16 | K = 32 |
| `.kind::f8f6f4` | No `.ws` | 1 | Sparse | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | 64xNxK 128xNxK | N = {8, 16, â¦ 256} steps of 8 OR N = {16, 32, â¦ 256} steps of 16 | K = 64 |
| `.kind::f8f6f4` | No `.ws` | 2 | Dense | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 32 |
| `.kind::f8f6f4` | No `.ws` | 2 | Sparse | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 64 |
| `.kind::f8f6f4` | `.ws` | 1 | Dense | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | 32xNxK 64xNxK 128xNxK | N = {64, 128, 256} | K = 32 |
| `.kind::f8f6f4` | `.ws` | 1 | Sparse | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | 32xNxK 64xNxK 128xNxK | N = {64, 128} | K = 64 |
| `.kind::f8f6f4` | `.ws` | 2 | Dense | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | Invalid | Invalid | Invalid |
| `.kind::f8f6f4` | `.ws` | 2 | Sparse | `.f32` `.f16` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` | Invalid | Invalid | Invalid |
| `.kind::mxf8f6f4` | No `.ws` | 1 | Dense | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | 128xNxK | N = {8, 16, â¦ 256} steps of 8 | K = 32 |
| `.kind::mxf8f6f4` | No `.ws` | 1 | Sparse | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | 128xNxK | N = {8, 16, â¦ 256} steps of 8 | K = 64 |
| `.kind::mxf8f6f4` | No `.ws` | 2 | Dense | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 32 |
| `.kind::mxf8f6f4` | No `.ws` | 2 | Dense | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | 128xNxK 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 32 |
| `.kind::mxf8f6f4` | No `.ws` | 2 | Sparse | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 64 |
| `.kind::mxf8f6f4` | `.ws` | 1 | Dense | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | Invalid | Invalid | Invalid |
| `.kind::mxf8f6f4` | `.ws` | 1 | Sparse | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | Invalid | Invalid | Invalid |
| `.kind::mxf8f6f4` | `.ws` | 2 | Dense | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | Invalid | Invalid | Invalid |
| `.kind::mxf8f6f4` | `.ws` | 2 | Sparse | `.f32` | `.e4m3`, `.e5m2`, `.e2m3`, `.e3m2`, `.e2m1` X (Scale) `.ue8m0` | Invalid | Invalid | Invalid |
| `.kind::i8` | No `.ws` | 1 | Dense | `.s32` | `.s8`, `.u8` | 64xNxK 128xNxK | N = {8, 16, 24, 32, 48, â¦ 256} steps of 16 after N > 32 | K = 32 |
| `.kind::i8` | No `.ws` | 1 | Sparse | `.s32` | `.s8`, `.u8` | 64xNxK 128xNxK | N = {8, 16, 24, 32, 48, â¦ 256} steps of 16 after N > 32 | K = 64 |
| `.kind::i8` | No `.ws` | 2 | Dense | `.s32` | `.s8`, `.u8` | 128xNxK 256xNxK | N = {32, 64, â¦ 256} steps of 32 | K = 32 |
| `.kind::i8` | No `.ws` | 2 | Sparse | `.s32` | `.s8`, `.u8` | 128xNxK 256xNxK | N = {32, 64, â¦ 256} steps of 32 | K = 64 |
| `.kind::i8` | `.ws` | 1 | Dense | `.s32` | `.s8`, `.u8` | 32xNxK 64xNxK 128xNxK | N = {64, 128, 256} | K = 32 |
| `.kind::i8` | `.ws` | 1 | Sparse | `.s32` | `.s8`, `.u8` | 32xNxK 64xNxK 128xNxK | N = {64, 128} | K = 64 |
| `.kind::i8` | `.ws` | 2 | Dense | `.s32` | `.s8`, `.u8` | Invalid | Invalid | Invalid |
| `.kind::i8` | `.ws` | 2 | Sparse | `.s32` | `.s8`, `.u8` | Invalid | Invalid | Invalid |
| `.kind::mxf4` | No `.ws` | 1 | Dense | `.f32` | `.e2m1` X (Scale) `.ue8m0` | 128xNxK | N = {8, 16, â¦ 256} steps of 8 | K = 64 |
| `.kind::mxf4` | No `.ws` | 1 | Sparse | `.f32` | `.e2m1` X (Scale) `.ue8m0` | 128xNxK | N = {8, 16, â¦ 256} steps of 8 | K = 128 |
| `.kind::mxf4` | No `.ws` | 2 | Dense | `.f32` | `.e2m1` X (Scale) `.ue8m0` | 128xNxK 256xNxK 256xNxK1 | N = {16, 32, â¦ 256} steps of 16 | K = 64, K1 = 96 |
| `.kind::mxf4` | No `.ws` | 2 | Dense | `.f32` | `.e2m1` X (Scale) `.ue8m0` | 128xNxK 256xNxK 256xNxK1 | N = {16, 32, â¦ 256} steps of 16 | K = 64, K1 = 96 |
| `.kind::mxf4` | No `.ws` | 2 | Sparse | `.f32` | `.e2m1` X (Scale) `.ue8m0` | 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 128 |
| `.kind::mxf4` | `.ws` | 1 / 2 | Either | `.f32` | `.e2m1` X (Scale) `.ue8m0` | Invalid | Invalid | Invalid |
| `.kind::mxf4nvf4` | No `.ws` | 1 | Dense | `.f32` | `.e2m1` X (Scale) `.ue8m0`, `.ue4m3` | 128xNxK | N = {8, 16, â¦ 256} steps of 8 | K = 64 |
| `.kind::mxf4nvf4` | No `.ws` | 1 | Sparse | `.f32` | `.e2m1` X (Scale) `.ue8m0`, `.ue4m3` | 128xNxK | N = {8, 16, â¦ 256} steps of 8 | K = 128 |
| `.kind::mxf4nvf4` | No `.ws` | 2 | Dense | `.f32` | `.e2m1` X (Scale) `.ue8m0`, `.ue4m3` | 128xNxK 256xNxK 256xNxK1 | N = {16, 32, â¦ 256} steps of 16 | K = 64, K1 = 96 |
| `.kind::mxf4nvf4` | No `.ws` | 2 | Dense | `.f32` | `.e2m1` X (Scale) `.ue8m0`, `.ue4m3` | 128xNxK 256xNxK 256xNxK1 | N = {16, 32, â¦ 256} steps of 16 | K = 64, K1 = 96 |
| `.kind::mxf4nvf4` | No `.ws` | 2 | Sparse | `.f32` | `.e2m1` X (Scale) `.ue8m0`, `.ue4m3` | 256xNxK | N = {16, 32, â¦ 256} steps of 16 | K = 128 |
| `.kind::mxf4nvf4` | `.ws` | 1 / 2 | Either | `.f32` | `.e2m1` X (Scale) `.ue8m0`, `.ue4m3` | Invalid | Invalid | Invalid |
