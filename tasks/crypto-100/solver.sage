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
modulus = 5873474411389687066479752710905805093792643888236819680112457467218799802874182862433030599419460928535677043337352388859166158041255159777167915134883924035063744305085255475605249226347404450500767162166526992543131130396198211662993797861048894946568767452108927191507
ciphertext = 5804629700103300312931165698547920769757407794383574830926434767265835955999126972682404039614888882302135402559791771317125417837661173811825551232904047722262746446221844588744432153001829848251755516687221468161048861457311649399626685243014205288770658840979065125211
known_part = 0x52754354465f0000000000000000000000000000000000000000000000000000000000000000
    
unknown_part = solve(exponent, modulus, ciphertext, known_part)[0]
  
result = known_part + unknown_part
print result.hex().decode('hex')
