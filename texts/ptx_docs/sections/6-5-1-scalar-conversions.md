### 6.5.1. Scalar Conversions

[Table 15](#scalar-conversions-convert-instruction-precision-and-format-t1) and [Table 16](#scalar-conversions-convert-instruction-precision-and-format-t2) show what precision and format the cvt instruction uses given operands of differing types. For example, if a `cvt.s32.u16` instruction is given a `u16` source operand and `s32` as a destination operand, the `u16` is zero-extended to `s32`.

Conversions to floating-point that are beyond the range of floating-point numbers are represented with the maximum floating-point value (IEEE 754 Inf for `f32` and `f64`, and ~131,000 for `f16`).

**Table 15 Convert Instruction Precision and Format Table 1**

|  |  | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | **s8** | **s16** | **s32** | **s64** | **u8** | **u16** | **u32** | **u64** | **f16** | **f32** | **f64** | **bf16** | **tf32** |
| **Source Format** | **s8** | â | sext | sext | sext | â | sext | sext | sext | s2f | s2f | s2f | s2f | â |
| **Source Format** | **s16** | chop1 | â | sext | sext | chop1 | â | sext | sext | s2f | s2f | s2f | s2f | â |
| **Source Format** | **s32** | chop1 | chop1 | â | sext | chop1 | chop1 | â | sext | s2f | s2f | s2f | s2f | â |
| **Source Format** | **s64** | chop1 | chop1 | chop1 | â | chop1 | chop1 | chop1 | â | s2f | s2f | s2f | s2f | â |
| **Source Format** | **u8** | â | zext | zext | zext | â | zext | zext | zext | u2f | u2f | u2f | u2f | â |
| **Source Format** | **u16** | chop1 | â | zext | zext | chop1 | â | zext | zext | u2f | u2f | u2f | u2f | â |
| **Source Format** | **u32** | chop1 | chop1 | â | zext | chop1 | chop1 | â | zext | u2f | u2f | u2f | u2f | â |
| **Source Format** | **u64** | chop1 | chop1 | chop1 | â | chop1 | chop1 | chop1 | â | u2f | u2f | u2f | u2f | â |
| **Source Format** | **f16** | f2s | f2s | f2s | f2s | f2u | f2u | f2u | f2u | â | f2f | f2f | f2f | â |
| **Source Format** | **f32** | f2s | f2s | f2s | f2s | f2u | f2u | f2u | f2u | f2f | â | f2f | f2f | f2f |
| **Source Format** | **f64** | f2s | f2s | f2s | f2s | f2u | f2u | f2u | f2u | f2f | f2f | â | f2f | â |
| **Source Format** | **bf16** | f2s | f2s | f2s | f2s | f2u | f2u | f2u | f2u | f2f | f2f | f2f | f2f | â |
| **Source Format** | **tf32** | â | â | â | â | â | â | â | â | â | â | â | â | â |

**Table 16 Convert Instruction Precision and Format Table 2**

|  |  | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** | **Destination Format** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | **f16** | **f32** | **bf16** | **e4m3** | **e5m2** | **e2m3** | **e3m2** | **e2m1** | **ue8m0** | **s2f6** |
| **Source Format** | **f16** | â | f2f | f2f | f2f | f2f | f2f | f2f | f2f | â | â |
| **Source Format** | **f32** | f2f | â | f2f | f2f | f2f | f2f | f2f | f2f | f2f | f2f |
| **Source Format** | **bf16** | f2f | f2f | â | f2f | f2f | f2f | f2f | f2f | f2f | f2f |
| **Source Format** | **e4m3** | f2f | â | f2f | â | â | â | â | â | â | â |
| **Source Format** | **e5m2** | f2f | â | f2f | â | â | â | â | â | â | â |
| **Source Format** | **e2m3** | f2f | â | f2f | â | â | â | â | â | â | â |
| **Source Format** | **e3m2** | f2f | â | f2f | â | â | â | â | â | â | â |
| **Source Format** | **e2m1** | f2f | â | f2f | â | â | â | â | â | â | â |
| **Source Format** | **ue8m0** | â | â | f2f | â | â | â | â | â | â | â |
| **Source Format** | **s2f6** | â | â | f2f | â | â | â | â | â | â | â |

**Notes**

sext = sign-extend; zext = zero-extend; chop = keep only low bits that fit;

s2f = signed-to-float; f2s = float-to-signed; u2f = unsigned-to-float;

f2u = float-to-unsigned; f2f = float-to-float.

1 If the destination register is wider than the destination format, the result is extended to the destination register width after chopping. The type of extension (sign or zero) is based on the destination format. For example, cvt.s16.u32 targeting a 32-bit register first chops to 16-bit, then sign-extends to 32-bit.
