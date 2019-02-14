def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    dd = pol.degree()
    nn = dd * mm + tt

    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    BB = BB.LLL()

    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    potential_roots = new_pol.roots()

    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots


def solve(e, n, c, k):
    ZmodN = Zmod(n);

    P.<x> = PolynomialRing(ZmodN)
    pol = (k + x)^e - c
    dd = pol.degree()

    beta = 1
    epsilon = beta / 30
    mm = ceil(beta**2 / (dd * epsilon))
    tt = floor(dd * mm * ((1/beta) - 1))
    XX = ceil(n**((beta**2/dd) - epsilon))

    return coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX)


exponent = 3
modulus = 4158933398832304390357360708556050233042862492737950725623500889120525019555544776488744969302955892929012277502408629621979491634510030058439185936125472689494652252993688393085084957259941284893864408150826652709820047963127021651197332297431158381328648003095465171976
ciphertext = 822129457101344823616420057503754367199836907649930409634851166644641882897520145685300059607492641029422751011260952803393719529884133890643227427271750915243303910686544529719662398829424945907813835396702553284777085362849116313552687322735584806884934593789476851255
known_part = 0x52754354465f0000000000000000000000000000000000000000000000000000000000000000
    
unknown_part = solve(exponent, modulus, ciphertext, known_part)[0]
  
result = known_part + unknown_part
print result.hex().decode('hex')
