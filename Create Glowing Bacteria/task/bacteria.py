
nitrogenous_bases = {
    "A": "T",
    "C": "G",
    "T": "A",
    "G": "C"
}


def create_complementary_bases(s):
    c = ""
    for i in range(len(s)):
        c += nitrogenous_bases[s[i]]
    return c


restriction_seq = "CTGCAG"
c_restriction_seq = create_complementary_bases(restriction_seq)

# strand, c_strand = input().split()
# strand, c_strand = "TGACTGCAGTTAG ACTGACGTCAATC".split()
strand = input()
c_strand = create_complementary_bases(strand)


def cut_plasmid(s: str, c_s: str):
    s_cut = f'{s[:s.index(restriction_seq) + 1]} {s[s.index(restriction_seq) + 1:]}'
    c_cut = f'{c_s[:c_s.rindex(c_restriction_seq) + 5]} {c_s[c_s.rindex(c_restriction_seq) + 5:]}'
    return s_cut, c_cut


# result_cut = cut_plasmid(strand, c_strand)
# print(result_cut[0])
# print(result_cut[1])

print(strand, c_strand)
