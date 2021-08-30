import sys

table = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G"""
table = dict(zip(table.split()[::2],table.split()[1::2]))

dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

def find_starts(seq):
    start = 0
    starts = []
    while(True):
        ATG_index = seq.find('ATG', start)
        if(ATG_index>-1):
            starts.append(ATG_index)
            start = ATG_index+3
        else:
            break
    return starts
starts = find_starts(dna)
starts.sort()
print(starts)

def find_ends(seq):
    end = 0
    ends = []
    while(True):
        end_index = seq.find('TAA', end)
        if end_index>-1:
            ends.append(end_index)
            end = end_index+3
        else:
            break
    end = 0
    while(True):
        end_index = seq.find('TGA', end)
        if end_index>-1:
            ends.append(end_index)
            end = end_index+3
        else:
            break
    end = 0
    while(True):
        end_index = seq.find('TAG', end)
        if end_index>-1:
            ends.append(end_index)
            end = end_index+3
        else:
            break
    
    return ends
ends = find_ends(dna)
ends.sort()
print(ends)

def translate(seq):
    aa = []
    for i in range(0,len(seq),3):
        condon = seq[i:i+3]
        aa.append(table[condon])
    aa = ''.join(aa)
    print(aa)
    return aa

results = []
for i in starts:
    for j in ends:
        if (j>i) and (j-i)%3==0:
#             print(dna[i:j])
            results.append(translate(dna[i:j]))
            break
print(results)

def reverse(seq):
    result = []
    for i in range(len(seq)-1, -1, -1):
        if seq[i] == 'A':
            result.append('T')
        elif seq[i] == 'T':
            result.append('A')
        elif seq[i] == 'G':
            result.append('C')
        elif seq[i] == 'C':
            result.append('G')
        else:
            result.append('N')
    result = ''.join(result)
    return result

rev_dna = reverse(dna)
print(rev_dna)

rev_starts = find_starts(rev_dna)
print(rev_starts)

rev_ends = find_ends(rev_dna)
print(rev_ends)

for i in rev_starts:
    for j in rev_ends:
        if (j>i) and (j-i)%3==0:
#             print(dna[i:j])
            results.append(translate(rev_dna[i:j]))
            break
print(results)

results = set(results)
print(results)