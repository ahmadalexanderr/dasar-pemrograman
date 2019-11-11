class PohonBiner:
    def __init__(self, A, L, R):
        self.A = A
        self.L = L
        self.R = R


def buat_pohon(A, L, R):
    return PohonBiner


def Akar(P):
    return P.A


def Left(P):
    return P.L


def Right(P):
    return P.R


def IsTreeEmpty(P):
    if P == None:
        return True
    else:
        return False


def IsOneElmt(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False


def IsUnerLeft(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False


def IsUnerRight(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False


def IsBiner(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False


# Number of element
def NbElement(P):
    if IsOneElmnt(P):
        return 1
    else:
        if IsBiner(P):
            return NbElement(Left(P)) + 1 + NbElement(Right(P))
        elif IsUnerLeft(P):
            return NbElement(Left(P)) + 1
        elif IsUnerRight(P):
            return 1 + NbElement(Right(P))


def NbDaun(P):
    if IsOneElmt(P):
        return 1
    else:
        if IsBiner(P):
            return NbDaun(Left(P)) + NbDaun(Right(P))
        elif IsUnerLeft(P):
            return NbDaun(Left(P))
        elif IsUnerRight(P):
            return NbDaun(Right(P))


def RepPrefix(P):
    if IsOneElmt(P):
        return [Akar(P)]
    else:
        if IsBiner(P):
            return [Akar(P)] + [RepPrefix(Left(P))] + [RepPrefix(Right(P))]
        elif IsUnerLeft(P):
            return [Akar(P)] + [RepPrefix(Left(P))]
        else:
            return [Akar(P)] + [RepPrefix(Right(P))]
