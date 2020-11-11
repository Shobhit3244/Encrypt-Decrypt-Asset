import Encrypt
import Decrypt
import sys
import _tkinter
import tkinter as data_frame
from tkinter.constants import *
from tkinter.filedialog import askopenfilename

__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.4"

filename = ""


def ext():
    sys.exit()


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
        alpha = Decrypt.to_decrypt(filename)
        if alpha != 'Done!':
            text_box2_de.configure(text=f"{alpha}")
            return
        text_box2_de.configure(text=f"{alpha}")
        done_btn_de.configure(state=ACTIVE)
    elif process == 'e':
        text_box_en.configure(text=f"Selected File: {fn}")
        alpha = Encrypt.to_encrypt(filename)
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
exit_btn = data_frame.Button(main_window, text="Exit", state=NORMAL, command=ext, width=9, height=1)
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
exit_btn_en = data_frame.Button(encrypt_window, text="Exit", state=NORMAL, command=ext, width=9, height=1)
exit_btn_en.grid(row=5, column=4, sticky=SW)
spacer_en = data_frame.Label(encrypt_window)
spacer_en.grid(row=6, column=0, columnspan=5)
cclabel_en = data_frame.Label(encrypt_window, text=f"Software CC: {Encrypt.__copyright__}, Creator: {Encrypt.__author__}, Version: {Encrypt.__version__}", background= "Yellow")
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
exit_btn_de = data_frame.Button(decrypt_window, text="Exit", state=NORMAL, command=ext, width=9, height=1)
exit_btn_de.grid(row=5, column=4, sticky=SW)
spacer_de = data_frame.Label(decrypt_window)
spacer_de.grid(row=6, column=0, columnspan=5)
cclabel_de = data_frame.Label(decrypt_window, text=f"Software CC: {Decrypt.__copyright__}, Creator: {Decrypt.__author__}, Version: {Decrypt.__version__}", background= "Yellow")
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
