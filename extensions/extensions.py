filetype = input("File name:" ).strip().lower()

if filetype.endswith(".gif"):
    print("image/gif")
elif filetype.endwith(".jpg"):
    print("image/jpg")
elif filetype.endwith(".jpeg"):
    print("image/jpeg")
elif filetype.endwith(".png"):
    print("image/png")
elif filetype.endwith(".pdf"):
    print("application/pdf")
elif filetype.endwith(".txt"):
    print("text/plain")
elif filetype.endswith(".zip")
    print("application/zip")
else:
    print("application/octet-stream")
