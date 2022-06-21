
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


def cut_gfp(g, rs1, rs2):
    return g[g.index(rs1) + 1: g.rindex(rs2) + 1]


def cut_c_gfp(g, rs1, rs2):
    return g[g.index(rs1) + len(rs1) - 1: g.rindex(rs2) + len(rs2) - 1]


gfp = input()
restriction_site_1, restriction_site_2 = input().split()

c_gfp = create_complementary_bases(gfp)
c_restriction_site_1 = create_complementary_bases(restriction_site_1)
c_restriction_site_2 = create_complementary_bases(restriction_site_2)


# def cut_plasmid(s: str, c_s: str):
#     s_cut = f'{s[:s.index(restriction_seq) + 1]} {s[s.index(restriction_seq) + 1:]}'
#     c_cut = f'{c_s[:c_s.rindex(c_restriction_seq) + 5]} {c_s[c_s.rindex(c_restriction_seq) + 5:]}'
#     return s_cut, c_cut


print(cut_gfp(gfp, restriction_site_1, restriction_site_2), cut_c_gfp(c_gfp, c_restriction_site_1, c_restriction_site_2))
