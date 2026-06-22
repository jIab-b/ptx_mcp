##### 9.7.17.2.2. Specifying Matrix Shape

*M* and *N* can be specified in the [Instruction descriptor](#tcgen05-instruction-descriptor).

*K* can be specified explicitly if there are multiple values of *K* supported for a given MMA variant. Otherwise, if *K* can be uniquely determined as per the [Table 42](#tcgen05-kind-shapes), then *K* cannot be explicitly specified.
