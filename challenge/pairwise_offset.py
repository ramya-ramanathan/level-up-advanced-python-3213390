def pairwise_offset(sequence, fillvalue='*', offset=0):
    ret = []
    # x1 in seq1
    # x2 asterisk
    for i in range(0,min(len(sequence),offset)):
        ret.append((sequence[i], fillvalue))
    
    if offset>len(sequence):
        # x1 asterisk
        # x2 asterisk
        remaining_off=offset-len(sequence)
        for _ in range(0,remaining_off):
            ret.append((fillvalue,fillvalue))
    else:
        # x1 in seq1
        # x2 in seq2
        seq1_start = offset
        for i in range(seq1_start,len(sequence)):
            ret.append((sequence[i], sequence[i-offset]))

    print(ret)
    # x1 asterisk
    # x2 in seq2
    for i in range(0,min(offset,len(sequence))):
        ret.append((fillvalue,sequence[i-min(offset,len(sequence))]))

    return ret

