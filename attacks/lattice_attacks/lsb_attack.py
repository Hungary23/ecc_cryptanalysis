from sage.all import vector, matrix, EllipticCurve
from sage.modules.free_module_integer import IntegerLattice

def lsb_attack(signatures, pubkey, curve: EllipticCurve, generator, know_part_length: int):
    if "kp" not in signatures:
        signatures["kp"] = [0] * len(signatures["r"])

    order = curve.order()
    sample_size = len(signatures["r"])
    s_inverse = [pow(s, -1, order) for s in signatures["s"]]
    unknown_nonce_bits = curve.order().nbits() - know_part_length

    offset = 2**(unknown_nonce_bits-1)
    offset_vec = vector([offset] * sample_size)

    A = vector([((pow(2**know_part_length, -1, order)) * (s_inv * r)) % order for (s_inv, r) in zip(s_inverse, signatures["r"])])
    B = vector([((pow(2**know_part_length, -1, order)) * (kp - s_inv * h)) % order for (s_inv, h, kp) in zip(s_inverse, signatures["h"], signatures["kp"])])

    m = matrix((matrix.identity(sample_size) * order).rows() + [A] + [B - offset_vec])

    lattice = IntegerLattice(m)
    shortest = lattice.shortest_vector(preprocess=2, pruning=False) + offset_vec # preprocess=2 means run the LLL algorithm
    sig_k = [(kp - k * 2**know_part_length) % order for (k, kp) in zip(shortest, signatures["kp"])]

    privkeys = [(s * k - h) * pow(r, -1, order) % order for r, s, h, k in zip(signatures["r"], signatures["s"], signatures["h"], sig_k)]

    for privkey in privkeys:
        if pubkey == privkey * generator:
            return privkey
    
    return None
