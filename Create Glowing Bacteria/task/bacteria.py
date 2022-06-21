
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


def cut_plasmid(s, c_s, rs, c_rs):
    s_cut = f'{s[:s.index(rs) + 1]} {s[s.index(rs) + 1:]}'
    c_cut = f'{c_s[:c_s.rindex(c_rs) + 5]} {c_s[c_s.rindex(c_rs) + 5:]}'
    return s_cut, c_cut


def cut_gfp(g, rs1, rs2):
    return g[g.index(rs1) + 1: g.rindex(rs2) + 1]


def cut_c_gfp(g, rs1, rs2):
    return g[g.index(rs1) + len(rs1) - 1: g.rindex(rs2) + len(rs2) - 1]


def ligate(p_cut, gfp_cut, c_gfp_cut):
    pt = p_cut[0].split()
    pb = p_cut[1].split()
    top = pt[0] + gfp_cut + pt[1]
    bottom = pb[0] + c_gfp_cut + pb[1]
    return top, bottom


def print_results(top, bottom):
    print(top)
    print(bottom)


def parse_data(filename):
    file = open(filename, 'rt')
    lines = file.readlines()
    file.close()

    plasmid = lines[0].rstrip("\n")
    rs = lines[1].rstrip("\n")
    gfp = lines[2].rstrip("\n")
    rs1_gfp, rs2_gfp = lines[3].split()

    return plasmid, rs, gfp, rs1_gfp, rs2_gfp


def complement_and_cut_data(plasmid, rs, gfp, rs1_gfp, rs2_gfp):
    c_plasmid = create_complementary_bases(plasmid)
    c_rs = create_complementary_bases(rs)
    c_gfp = create_complementary_bases(gfp)
    c_rs1_gfp = create_complementary_bases(rs1_gfp)
    c_rs2_gfp = create_complementary_bases(rs2_gfp)

    p_cut = cut_plasmid(plasmid, c_plasmid, rs, c_rs)
    gfp_cut = cut_gfp(gfp, rs1_gfp, rs2_gfp)
    c_gfp_cut = cut_c_gfp(c_gfp, c_rs1_gfp, c_rs2_gfp)

    return p_cut, gfp_cut, c_gfp_cut


def process_data(filename):
    plasmid, rs, gfp, rs1_gfp, rs2_gfp = parse_data(filename)
    p_cut, gfp_cut, c_gfp_cut = complement_and_cut_data(plasmid, rs, gfp, rs1_gfp, rs2_gfp)
    top, bottom = ligate(p_cut, gfp_cut, c_gfp_cut)
    print_results(top, bottom)


file_name = input()
process_data(file_name)
