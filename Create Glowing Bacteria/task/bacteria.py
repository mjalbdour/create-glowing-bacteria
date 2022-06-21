# write your program here

nitrogenous_bases = {
    "A": "T",
    "C": "G",
    "T": "A",
    "G": "C"
}

strand = input()
# strand = "GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTGTGCACTACCTCCTT"


def create_complementary_strand(s):
    c = ""
    for i in range(len(s)):
        c += nitrogenous_bases[s[i]]
    return c


complementary_strand = create_complementary_strand(strand)
print(complementary_strand)
