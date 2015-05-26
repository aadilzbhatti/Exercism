__author__ = 'aadil'

def to_rna(base):
    base = list(base)
    for i in range(len(base)):
        if base[i] == 'G':
            base[i] = 'C'
        else:
            if base[i] == 'C':
                base[i] = 'G'
            else:
                if base[i] == 'A':
                    base[i] = 'U'
                else:
                    base[i] = 'A'
    return "".join(base)
