import pickle

__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

extension = ""


def to_decrypt(filename):
    if not filename.endswith(".skpe"):
        return "Error : Wrong File Type Selected"

    def key_define(f_data):
        global extension
        dt_div1 = f_data.split()
        key_s1 = dt_div1[1].split(":")
        site = key_s1[1].strip()
        alg = key_s1[0].strip().split("~")
        data = dt_div1[0].split("`")
        extension = dt_div1[2].strip()
        return alg, int(site), data

    with open(filename, 'rb') as ts_data:
        s_data = pickle.load(ts_data)

    algorithm, scepter, s_data = key_define(s_data)
    us_data = ""
    # print(algorithm, scepter, s_data, type(chr(scepter)))
    for temp in range(len(s_data)):
        if s_data[temp] != chr(scepter) and s_data[temp].isdigit():
            s_data[temp] = str((int(s_data[temp]) + 32) // 5)
            s_data[temp] = str((int(s_data[temp]) - 32) // 9)

    # print(s_data)

    counter = 0
    for char in s_data:
        if char == '':
            continue
        if char != chr(scepter):
            if counter == len(algorithm):
                counter = 0
            method = algorithm[counter][0]
            m_value = int(algorithm[counter][1])
            if method == "M":
                us_data += chr(int(char) // m_value)
                pass
            elif method == "A":
                us_data += chr(int(char) - m_value)
                pass
            elif method == "S":
                us_data += chr(int(char) + m_value)
                pass
            counter += 1
            continue
        us_data += " "
    # print(us_data)

    new_file = filename[::-1]
    xp = new_file.find(".")
    new_file = new_file[xp+1::].replace("detpyrcnE", "")[::-1]
    with open(f"{new_file} Decrypted.{extension}", "w") as final:
        final.write(us_data)
    return "Done!"


# to_decrypt("E:/Python Projects/Encryption/Test Data Encrypted.txt")
