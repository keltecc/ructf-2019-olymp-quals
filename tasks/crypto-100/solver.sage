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

    beta = 1                                # b = N
    epsilon = beta / 15                      # <= beta / 7
    mm = ceil(beta**2 / (dd * epsilon))     # optimized value
    tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
    XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value

    return coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX)


exponent = 3
modulus = 3134997578144240333925385482843843855577797420632253515417549090714777320489642879333389145094276861160290872764107052796433587483236345186190233396538924890946327743610666403993979788488178076731917740119446065550574974240137022579003886435408484062431645753745048666271021195939950657755191233801091793994469593444302377789033451052481631229430882692196873472070595400208738376344120
ciphertext = 3043104980153297473256289689572672311797722805105440774047989729540922674697433266572987137832563652431739690269171915120533639346217017787031002946374441350252152416993325361384647060599373530833899474059766881519612075427040713565788804661151036241215248164360816793840701419914866830329027353445034176986601691424475399934837662225209309604708536573846476484854798634363591371165008
known_part = 0x5b2a5d20596f75722073656372657420666c61672069732052754354465f0000000000000000000000000000000000000000000000000000000000000000
    
unknown_part = solve(exponent, modulus, ciphertext, known_part)[0]
  
result = known_part + unknown_part
print result.hex().decode('hex')
