def calc(pa=list):
    pas = list(map(int,pa))
    if 1 in pas:
        PAN=True
    else:
        PAN=False
    if 2 in pas:
        LIC=True
    else:
        LIC=False
    if 3 in pas:
        PAS=True
    else:
        PAS=False
    if 4 in pas:
        VOT=True
    else:
        VOT=False
    return(PAN,LIC,PAS,VOT)
