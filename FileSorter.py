import os
import shutil

def main():
    path = input("Enter a path: ")
    try:
        files = os.listdir(path) #Gets list of all files in a directory
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if not(os.path.exists(path+"/"+extension)):
                os.mkdir(path+"/"+extension)
            shutil.move(path+"/"+ file, path+"/"+extension+"/"+file)
        print("Done")
    except Exception as e:
        print("An error occured: ", e)



if __name__ == "__main__":
    main()

