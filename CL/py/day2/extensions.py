'''
In a file called extensions.py,
implement a program that prompts the user for the name of a file and
then outputs that file’s media type if the file’s name ends,
case-insensitively, in any of these suffixes:
'''
def extensions(s):

    s = s.split('.')[1]
    match s:
        case "gif":
            ret = "image/gif"
        case "jpg":
            ret = "image/jpg"
        case "jpeg":
            ret = "image/jpeg"
        case "png":
            ret = "image/png"
        case "pdf":
            ret = "application/pdf"
        case "txt":
            ret = "text/plain"
        case "zip":
            ret = "application/zip"
        case _:
            ret = "application/octet-stream"
    return ret

def main():
    s = input("File name: ")
    print(extensions(s))

main()
