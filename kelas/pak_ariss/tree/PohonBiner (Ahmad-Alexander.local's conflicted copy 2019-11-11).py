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


def IsOneElmtPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False


def IsUnerLeftPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False


def IsUnerRightPB(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False

def IsBiner(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P)))
        return True
    else:
        return False


