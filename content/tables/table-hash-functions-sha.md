| Hash function | Output size d (bits) | Rate r (bits) | Capacity c (bits) | Collision resistance (bits) |
|---|---|---|---|---|
| SHA3-224 | 224 | 1152 | 448 | $\frac{d}{2} = 112$ |
| SHA3-256 | 256 | 1088 | 512 | $\frac{d}{2} = 128$ |
| SHA3-384 | 384 | 832 | 768 | $\frac{d}{2} = 192$ |
| SHA3-512 | 512 | 576 | 1,024 | $\frac{d}{2} = 256$ |
| SHAKE128 | $d$ | 1,344 | 256 | $min(\frac{d}{2}, \frac{c}{2}) = min(\frac{d}{2}, 128)$ |
| SHAKE256 | $d$ | 1,088 | 512 | $min(\frac{d}{2}, \frac{c}{2}) = min(\frac{d}{2}, 256)$ |