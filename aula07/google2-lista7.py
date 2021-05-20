def albania():
    popa = 80000
    popb = 200000
    anos = 0
    while popa < popb:
        popa = popa*1.03
        popb = popb*1.015
        anos = anos + 1
    return anos


def cresc (popa,popb,txa,txb):
    if popa < popb and txa <= txb:
        return -1
    anos =0
    while popa < popb:
        popa = popa + popa*(txa/100.0)
        popb = popb + popb*(txb/100.0)
        anos = anos +1
    return anos



def divi(n):
    d=2
    while n%d!=0:
        d=d+1
    return d




def vogal(plv):
    i=0
    vg=''
    while i<len(plv):
        if plv[i] in 'AEIOUaeiou':
            vg=plv[i]
        i=i+1
    return vg






def f1(plv):
    i=0
    while i<len(plv):
        if plv[i] in 'AEIOUaeiou':
            return plv[i]
        i=i+1
    return ''
