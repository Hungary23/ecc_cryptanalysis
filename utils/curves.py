from sage.all import EllipticCurve, GF

# define the most common curves
Fsec256r1 = GF(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF)
sec256r1 = EllipticCurve(Fsec256r1, [Fsec256r1(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC), Fsec256r1(0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B)])
gen_sec256r1 = sec256r1(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296, 0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)

Fsec256k1 = GF(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)
sec256k1 = EllipticCurve(Fsec256k1, [Fsec256k1(0), Fsec256k1(7)])
gen_sec256k1 = sec256k1(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)

# TODO: add more curves

def from_str(curve): # sketchy python hack
    return (globals()[curve], globals()["gen_" + curve])