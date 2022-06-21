
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


def cut_plasmid(s, c_s, rs):
    c_rs = create_complementary_bases(rs)
    s_cut = f'{s[:s.index(rs) + 1]} {s[s.index(rs) + 1:]}'
    c_cut = f'{c_s[:c_s.rindex(c_rs) + 5]} {c_s[c_s.rindex(c_rs) + 5:]}'
    return s_cut, c_cut


def cut_gfp(g, rs1, rs2):
    return g[g.index(rs1) + 1: g.rindex(rs2) + 1]


def cut_c_gfp(g, rs1, rs2):
    return g[g.index(rs1) + len(rs1) - 1: g.rindex(rs2) + len(rs2) - 1]


def ligate(pt, pb, gt, gb):
    top = pt[0] + gt + pt[1]
    bottom = pb[0] + gb + pb[1]
    return top, bottom


# gfp = input()
# restriction_site_1, restriction_site_2 = input().split()

# c_gfp = create_complementary_bases(gfp)
# c_restriction_site_1 = create_complementary_bases(restriction_site_1)
# c_restriction_site_2 = create_complementary_bases(restriction_site_2)

# print(cut_gfp(gfp, restriction_site_1, restriction_site_2), cut_c_gfp(c_gfp, c_restriction_site_1, c_restriction_site_2))

def parse_data(filename='example.txt'):
    file = open(filename, 'rt')
    lines = file.readlines()[:2]
    first_line = lines[0].split()
    plasmid_top = (first_line[0], first_line[1])
    plasmid_bottom = (first_line[2], first_line[3])
    second_line = lines[1].split()
    gfp = (second_line[0], second_line[1])
    file.close()

    return plasmid_top, plasmid_bottom, gfp


file_name = input()
ptop, pbottom, gfp_ = parse_data(file_name)

upper, lower = ligate(ptop, pbottom, gfp_[0], gfp_[1])
print(upper)
print(lower)
