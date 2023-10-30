from msilib.schema import File
import wget
import random
import os
import linecache

'''
The Plan:
1. Download all the files (done)
2. Generate a random number between 1 and 1404 (done)
3. Use the number to select a question (done)
4. Create a temporary Latex file with the question (done)
5. Compile the Latex file and open with TexWorks (?) (command line?)
6. Delete the temporary Latex file (done)

Once this is done, further functionality can be added, such as:
- Selecting a specific question
- Selecting a specific paper
- Filtering by topic
- Filtering by difficulty
- Marking questions as done
'''

#33 years (including spec)

def Download():
    for i in range(87,119):
        for j in range(1,4):
            i = i%100
            url = f"https://stepdatabase.maths.org/database/db/{i:02}/{i:02}-S{j}.tex"
            print(url)
            wget.download(url)
    wget.download("https://stepdatabase.maths.org/database/db/Spec/Spec-S1.tex")
    wget.download("https://stepdatabase.maths.org/database/db/Spec/Spec-S2.tex")
    wget.download("https://stepdatabase.maths.org/database/db/Spec/Spec-S3.tex")

    for i in range(87,119):
        for j in range(1,4):
            i = i%100
            url = f"https://stepdatabase.maths.org/database/db/{i:02}/{i:02}-S{j}.pdf"
            print(url)
            wget.download(url)
    wget.download("https://stepdatabase.maths.org/database/db/Spec/Spec-S1.pdf")
    wget.download("https://stepdatabase.maths.org/database/db/Spec/Spec-S2.pdf")
    wget.download("https://stepdatabase.maths.org/database/db/Spec/Spec-S3.pdf")

def GenerateQuestion():
    num = random.randint(1,1404)
    line = linecache.getline(r"Index.txt", num)
    print(line)
    question = line.split()[0]
    return(question)
    
def Compile(question):
    filename = question.split('-')[0] + '-' + question.split('-')[1]
    qNum = question.split('-')[2]
    f = open(f"{filename}.tex", "r")
    t = open("Template.txt", "r")
    lines = f.readlines()
    template = t.readlines()
    writing = False
    text = ""   
    
    for string in template:
        text = text + string
        
    for line in lines:        
        if(qNum in line):
            writing = True
        if("\end{question}" in line):
            writing = False
        if(writing):
            text = text + line
    
    text = text + "\end{question}"
    text = text + "\end{document}"

    with open('Question.tex', 'w') as fout:
        fout.write(text)
        

    f.close()
    

def Delete(filename):
    os.remove(filename);

Compile(GenerateQuestion())
cmd = "C:/Users/egeis/Maths/PythonApplication1/Question.tex"
os.system(cmd)

input("Enter to finish")

Delete("Question.tex")