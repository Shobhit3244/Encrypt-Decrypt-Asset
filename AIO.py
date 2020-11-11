import pickle
import random
import sys
import _tkinter
import tkinter as data_frame
from tkinter.constants import *
from tkinter.filedialog import askopenfilename

__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.5"

extension = ""
filename = ""


def ext():
    sys.exit()


def to_encrypt(file_name):
    """__author__ = "Shobhit Kundu"
    __copyright__ = "Copyright (C) 2020 Shobhit Kundu"
    __license__ = "Public Demo"
    __version__ = "1.3"""

    keys = {16: "M2~A10~S4:20408", 32: "M4~A12~S16~A4:141002", 64: "M8~A12~S32:21276", 128: "M16~A12~S64~A16:150575"}
    d_key = keys.get(random.choice([16, 32, 64, 128]))

    def key_define(get_key):
        key_s1 = get_key.split(":")
        site = key_s1[1].strip()
        alg = key_s1[0].strip().split("~")
        return alg, int(site)

    algorithm, scepter = key_define(d_key)
    s_data = []
    try:
        with open(file_name, 'r') as dta:
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

    new_file = file_name[::-1]
    xp = new_file.find(".")
    s_data.append(" \n{} {}".format(d_key, new_file[:xp:][::-1]))
    new_file = new_file[xp + 1::][::-1]
    # print(s_data)
    with open(f"{new_file} Encrypted.skpe", "wb") as final:
        pickle.dump("`".join(s_data), final)
    return "Done!"


def to_decrypt(file_name):
    """__author__ = "Shobhit Kundu"
    __copyright__ = "Copyright (C) 2020 Shobhit Kundu"
    __license__ = "Public Demo"
    __version__ = "1.2"""

    if not file_name.endswith(".skpe"):
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

    with open(file_name, 'rb') as ts_data:
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

    new_file = file_name[::-1]
    xp = new_file.find(".")
    new_file = new_file[xp+1::].replace("detpyrcnE", "")[::-1]
    with open(f"{new_file} Decrypted.{extension}", "w") as final:
        final.write(us_data)
    return "Done!"


def encrypt():
    main_window.withdraw()
    encrypt_window.deiconify()
    encrypt_window.mainloop()
    main_window.deiconify()
    encrypt_window.withdraw()


def decrypt():
    main_window.withdraw()
    decrypt_window.deiconify()
    decrypt_window.mainloop()
    main_window.deiconify()
    decrypt_window.withdraw()


def main():
    main_window.deiconify()
    encrypt_window.withdraw()
    decrypt_window.withdraw()
    done_btn_en.configure(state=DISABLED)
    done_btn_de.configure(state=DISABLED)


def get_filename(process):
    global filename
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    fn = filename[::-1][:filename[::-1].find('/'):][::-1]
    if process == 'd':
        text_box_de.configure(text=f"Selected File: {fn}")
        alpha = to_decrypt(filename)
        if alpha != 'Done!':
            text_box2_de.configure(text=f"{alpha}")
            return
        text_box2_de.configure(text=f"{alpha}")
        done_btn_de.configure(state=ACTIVE)
    elif process == 'e':
        text_box_en.configure(text=f"Selected File: {fn}")
        alpha = to_encrypt(filename)
        if alpha != 'Done!':
            text_box2_en.configure(text=f"{alpha}")
            return
        text_box2_en.configure(text=f"{alpha}")
        done_btn_en.configure(state=ACTIVE)
    return


main_window = data_frame.Tk()
main_window.wm_title("Shobhit's Encryption Decryption Asset")
main_window.geometry('605x225')
label_top = data_frame.Label(main_window, text="Encrypted Data Protector", font=('ARIAL', 30))
label_top.grid(row=0, column=1, sticky=N, columnspan=3)
encrypt_btn = data_frame.Button(main_window, text="Encrypt File", state=NORMAL, command=encrypt, width=20, height=2)
encrypt_btn.grid(row=1, column=2, sticky=N)
decrypt_btn = data_frame.Button(main_window, text="Decrypt File", state=NORMAL, command=decrypt, width=20, height=2)
decrypt_btn.grid(row=2, column=2, sticky=N)
spacer_main = data_frame.Label(main_window)
spacer_main.grid(row=3, column=0, columnspan=5)
back_btn = data_frame.Button(main_window, text="Back", state=DISABLED, command=main, width=9, height=1)
back_btn.grid(padx=3, row=4, column=0, sticky=SE)
exit_btn = data_frame.Button(main_window, text="Exit", state=NORMAL, command=exit, width=9, height=1)
exit_btn.grid(row=4, column=4, sticky=SW)
spacer_main1 = data_frame.Label(main_window)
spacer_main1.grid(row=5, column=0, columnspan=5)
cclabel_main = data_frame.Label(main_window, text=f"Software CC: {__copyright__}, Creator: {__author__}, Version: {__version__}", background= "Yellow")
cclabel_main.grid(row=6, column=0, columnspan=5)

encrypt_window = data_frame.Tk()
encrypt_window.wm_title("Shobhit's Encryption Asset")
encrypt_window.geometry('605x225')
label_top_enc = data_frame.Label(encrypt_window, text="Data Encryption Software", font=('ARIAL', 30))
label_top_enc.grid(row=0, column=1, sticky=N, columnspan=3)
gf_btn_en = data_frame.Button(encrypt_window, text="Select File", state=NORMAL, command=lambda: get_filename("e"), width=20, height=2)
gf_btn_en.grid(row=1, column=2, sticky=N)
text_box_en = data_frame.Label(encrypt_window, text="", anchor=CENTER)
text_box_en.grid(row=2, column=0, columnspan=5)
text_box2_en = data_frame.Label(encrypt_window, text="", anchor=CENTER)
text_box2_en.grid(row=3, column=0, columnspan=5)
text_box1_en = data_frame.Label(encrypt_window, text="Only Test based on UTF-8 Files Supported", anchor=CENTER)
text_box1_en.grid(row=4, column=0, columnspan=5)
back_btn_en = data_frame.Button(encrypt_window, text="Back", state=NORMAL, command=main, width=9, height=1)
back_btn_en.grid(padx=2, row=5, column=0, sticky=SE)
done_btn_en = data_frame.Button(encrypt_window, text="Done", state=DISABLED, command=main, width=9, height=1)
done_btn_en.grid(row=5, column=2)
exit_btn_en = data_frame.Button(encrypt_window, text="Exit", state=NORMAL, command=exit, width=9, height=1)
exit_btn_en.grid(row=5, column=4, sticky=SW)
spacer_en = data_frame.Label(encrypt_window)
spacer_en.grid(row=6, column=0, columnspan=5)
cclabel_en = data_frame.Label(encrypt_window, text=f"Software CC: {__copyright__}, Creator: {__author__}, Version: {__version__}", background= "Yellow")
cclabel_en.grid(row=7, column=0, columnspan=5)

decrypt_window = data_frame.Tk()
decrypt_window.wm_title("Shobhit's Decryption Asset")
decrypt_window.geometry('605x225')
label_top_enc = data_frame.Label(decrypt_window, text="Data Decryption Software", font=('ARIAL', 30))
label_top_enc.grid(row=0, column=1, sticky=N, columnspan=3)
gf_btn_de = data_frame.Button(decrypt_window, text="Select File", state=NORMAL, command=lambda: get_filename("d"), width=20, height=2)
gf_btn_de.grid(row=1, column=2, sticky=N)
text_box_de = data_frame.Label(decrypt_window, text="", anchor=CENTER)
text_box_de.grid(row=2, column=0, columnspan=5)
text_box2_de = data_frame.Label(decrypt_window, text="", anchor=CENTER)
text_box2_de.grid(row=3, column=0, columnspan=5)
text_box1_de = data_frame.Label(decrypt_window, text="Only SKPE Encrypted files with .skpe extension Supported", anchor=CENTER)
text_box1_de.grid(row=4, column=0, columnspan=5)
back_btn_de = data_frame.Button(decrypt_window, text="Back", state=NORMAL, command=main, width=9, height=1)
back_btn_de.grid(padx=1, row=5, column=0, sticky=SE)
done_btn_de = data_frame.Button(decrypt_window, text="Done", state=DISABLED, command=main, width=9, height=1)
done_btn_de.grid(row=5, column=2)
exit_btn_de = data_frame.Button(decrypt_window, text="Exit", state=NORMAL, command=exit, width=9, height=1)
exit_btn_de.grid(row=5, column=4, sticky=SW)
spacer_de = data_frame.Label(decrypt_window)
spacer_de.grid(row=6, column=0, columnspan=5)
cclabel_de = data_frame.Label(decrypt_window, text=f"Software CC: {__copyright__}, Creator: {__author__}, Version: {__version__}", background= "Yellow")
cclabel_de.grid(row=7, column=0, columnspan=5)

try:
    main_window.wm_iconbitmap("icon.ico")
    encrypt_window.wm_iconbitmap("icon.ico")
    decrypt_window.wm_iconbitmap("icon.ico")
except _tkinter.TclError:
    pass


if __name__ == '__main__':
    encrypt_window.withdraw()
    decrypt_window.withdraw()
    main_window.mainloop()
