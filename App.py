import tkinter as tk
import pyperclip
import csv
from prompts import questions

promptNum = 0


def setPrompt(index):
    return questions[index]

def addRowCSV(file_path, prompt, answer):
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Prompt', 'Answer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'Prompt': prompt, 'Answer': answer})

def exportToCSV():
    addRowCSV("Dataset.csv", setPrompt(promptNum), retrievedResult)    


def nextPrompt():
    global promptNum
    promptNum = (promptNum + 1) % len(questions)  
    promptEntry.delete('1.0', tk.END)
    promptEntry.insert('1.0', setPrompt(promptNum))
    promptNumLabel.config(text="Prompt No: "+str(promptNum + 1))

def prevPrompt():
    global promptNum
    promptNum = (promptNum - 1) % len(questions)  
    promptEntry.delete('1.0', tk.END)
    promptEntry.insert('1.0', setPrompt(promptNum))
    promptNumLabel.config(text="Prompt No: "+str(promptNum - 1))

def changePrompt():
    global promptNum
    try:
        promptNum = int(setPromptNoEntry.get("1.0", "end-1c"))   
        if promptNum >  len(questions):
            print("Invalid no!")
        else:
            promptEntry.delete('1.0', tk.END)
            promptEntry.insert('1.0', setPrompt(promptNum % len(questions)))
            promptNumLabel.config(text="Prompt No: "+str(promptNum % len(questions)))
    except:
        print("Invalid no!")


def pasteResults():
    global retrievedResult
    retrievedResult = pyperclip.paste()
    resultEntry.delete('1.0', tk.END)
    resultEntry.insert('1.0', retrievedResult)


def createContext():
    contextEntry.delete('1.0', tk.END)
    contextEntry.insert('1.0', f"Context created for: {promptNum + 1}")
    prompt = f'''Give answer for the question  based on the context provided. 
    Based on the give context give answer or take relevant part from the context to form the answer.
    Keep the  answer simple and in brief.Question: {setPrompt(promptNum)} 
    also provide refrence used for generating answer according to Indian laws'''
    pyperclip.copy(prompt)

def resetState():
    contextEntry.delete('1.0', tk.END)
    resultEntry.delete('1.0', tk.END)



mainWindow = tk.Tk()
mainWindow.geometry("500x500")
mainWindow.title("Dataset Toolkit v0.2 By Aditya")

prompt = setPrompt(promptNum)

promptEntry = tk.Text(mainWindow, font=('calibre', 10, 'normal'), width=65, height=3)
promptEntry.insert('1.0', prompt)
promptEntry.pack()
promptEntry.place(x=10, y=10)
promptNumLabel = tk.Label(
        mainWindow,
        font=("Comic Sans", 10),
        text="Prompt No: 1")
promptNumLabel.place(x=10, y=80)

setPromptNoEntry = tk.Text(mainWindow, font=('calibre', 10, 'normal'), width=10, height=2)
setPromptNoEntry.place(x=260, y=80)

contextEntry = tk.Text(mainWindow, font=('calibre', 10, 'normal'), width=40, height=1)
contextEntry.place(x=120, y=180)

resultEntry = tk.Text(mainWindow, font=('calibre', 10, 'normal'), width=65, height=10)
resultEntry.place(x=10, y=220)

button = tk.Button(mainWindow, text="Set Prompt",command=changePrompt)
button.place(x=340, y=80)

button1 = tk.Button(mainWindow, text="Previous Prompt", command=prevPrompt)
button1.place(x=10, y=120)

button2 = tk.Button(mainWindow, text="Next Prompt", command=nextPrompt)
button2.place(x=120, y=120)

button3 = tk.Button(mainWindow, text="Create Context", command=createContext)
button3.place(x=10, y=180)

button4 = tk.Button(mainWindow, text="Paste Results", command=pasteResults)
button4.place(x=10, y=400)

button5 = tk.Button(mainWindow, text="Export to CSV", command=exportToCSV)
button5.place(x=100, y=400)

button6 = tk.Button(mainWindow, text="Reset State", command=resetState)
button6.place(x=400, y=400)

mainWindow.attributes("-topmost", True)

tk.mainloop()
