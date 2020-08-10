import os
import pdftotext
import string

workingFolder = "Kadencja_IX_Posiedzenie_11"
for folder in os.listdir(f"{os.getcwd()}/{workingFolder}"):
    i = 0
    if folder == ".directory":continue
    folder_location = f"{os.getcwd()}/{workingFolder}/{folder}"
    for plik in os.listdir(folder_location):
        if not (os.path.isfile(f"{folder_location}/{plik}")):continue
        with open(f"{folder_location}/{plik}", "rb") as f:
            try:
                pdf = pdftotext.PDF(f)
            except:
                continue
        if not os.path.exists(f"{folder_location}/txt/"):os.mkdir(f"{folder_location}/txt/")
        with open(f"{folder_location}/txt/{plik[:-4]}.txt", "w") as tmp:
            tekst = ("\n\n".join(pdf))
            tmp.write(tekst)
        i += 1


    for fileToStrip in os.listdir(f"{folder_location}/txt"):
        location = f"{folder_location}/txt/{fileToStrip}"
        baza = ["Stranica"]
        letters = list(string.ascii_letters)
        for i in range(0,10):
            letters.append(str(i))
        
        tmp = 0
        os.rename(f"{location}", f"{folder_location}/txt/tekst{tmp}.txt")
        with open(f'{folder_location}/txt/tekst{tmp}.txt', "r") as f, open(f'{folder_location}/txt/tekst{tmp+1}.txt', 'w') as newfile:
            for line in f:
                if not any(phrase in line for phrase in baza):
                    newfile.write(line)
        tmp += 1

        with open(f'{folder_location}/txt/tekst{tmp}.txt', "r") as f:
            content = f.readlines()
        with open(f'{folder_location}/txt/tekst{tmp+1}.txt', "w") as newfile:
            for line in content:
                first23 = line[:23]
                if not any(letter in first23[-1] for letter in letters):
                    newfile.write(line)
        tmp += 1


        with open(f'{folder_location}/txt/tekst{tmp}.txt', "r") as f:
            content = f.readlines()
        with open(f'{folder_location}/txt/tekst{tmp+1}.txt', "w") as newfile:
            for line in content:
                newLine = line[23:]
                newfile.write(newLine)
        tmp += 1

        for i in range(0,tmp):
            os.remove(f"{folder_location}/txt/tekst{i}.txt")
        os.rename(f"{folder_location}/txt/tekst{tmp}.txt", f"{location}")