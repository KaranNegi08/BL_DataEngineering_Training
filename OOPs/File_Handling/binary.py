with open("ss.png", "rb") as f:
    with open("ss_copy2.jpeg", "wb") as wf:
        wf.write(f.read())
