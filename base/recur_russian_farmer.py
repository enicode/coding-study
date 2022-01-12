def rrf(nl,nr):
    if nl==1:
        return nr
    elif nl%2 == 1:
        return nr + rrf(nl//2,2*nr)
    else: 
        return rrf(nl//2,2*nr)

print(rrf(12,12))