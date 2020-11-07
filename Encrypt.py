import pickle
import random

__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

keys = {16: "M2~A10~S4:20408", 32: "M4~A12~S16~A4:141002", 64: "M8~A12~S32:21276", 128: "M16~A12~S64~A16:150575"}
d_key = keys.get(random.choice([16, 32, 64, 128]))


def to_encrypt(filename):
    def key_define(get_key):
        key_s1 = get_key.split(":")
        site = key_s1[1].strip()
        alg = key_s1[0].strip().split("~")
        return alg, int(site)

    algorithm, scepter = key_define(d_key)
    s_data = []
    try:
        with open(filename, 'r') as dta:
            us_data = dta.read()
    except:
        return "Error : Non Text File Selected"
    counter = 0
    for char in us_data:
        if char != " ":
            if counter == len(algorithm):
                counter = 0
            method = algorithm[counter][0]
            m_value = int(algorithm[counter][1])
            if method == "M":
                s_data.append(str(ord(char) * m_value))
            elif method == "A":
                s_data.append(str(ord(char) + m_value))
            elif method == "S":
                s_data.append(str(ord(char) - m_value))
            counter += 1
            continue
        s_data.append(chr(scepter))
    for temp in range(len(s_data)):
        if s_data[temp] != chr(scepter) and s_data[temp].isdigit():
            s_data[temp] = str((int(s_data[temp]) * 9) + 32)
            s_data[temp] = str((int(s_data[temp]) * 5) - 32)

    new_file = filename[::-1]
    xp = new_file.find(".")
    s_data.append(" \n{} {}".format(d_key, new_file[:xp:][::-1]))
    new_file = new_file[xp + 1::][::-1]
    # print(s_data)
    with open(f"{new_file} Encrypted.skpe", "wb") as final:
        pickle.dump("`".join(s_data), final)
    return "Done!"

# to_encrypt("E:/Python Projects/Encryption/Test Data.txt")
