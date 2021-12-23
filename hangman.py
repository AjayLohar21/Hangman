import random
import pygame
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
pygame.mixer.init()



score = 0
run = True
# main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg = "#f5f5dc")
    count = 0
    win_count = 0
    # choosing word
    index = random.randint(0,15)
    file = open('words.txt','r')
    l = file.readlines()
    selected_word = l[index].strip('\n')
    
    # creation of word dashes variables
    x = 490
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#f5f5dc",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
        
    #letters icon
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    # hangman images
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
    #letters placement
    button = [['b1','a',250,595],['b2','b',320,595],['b3','c',390,595],['b4','d',460,595],['b5','e',530,595],['b6','f',600,595],['b7','g',670,595],['b8','h',740,595],['b9','i',810,595],['b10','j',880,595],['b11','k',950,595],['b12','l',1020,595],['b13','m',1090,595],['b14','n',250,645],['b15','o',320,645],['b16','p',390,645],['b17','q',460,645],['b18','r',530,645],['b19','s',600,645],['b20','t',670,645],['b21','u',740,645],['b22','v',810,645],['b23','w',880,645],['b24','x',950,645],['b25','y',1020,645],['b26','z',1090,645]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#f5f5dc",activebackground="#f5f5dc",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))

    #hangman placement
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#f5f5dc",image={})'.format(p1[0],p1[1]))



    # placement of first hangman image
    c1.place(x = 500,y =- 50)
    
    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(root,bd = 0,command = close,bg="#f5f5dc",activebackground = "#f5f5dc",font = 10,image = e1)
    ex.place(x=1370,y=10)


    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        pygame.mixer.music.load('wrong.mp3')
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play()
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    pygame.mixer.music.load('correct.mp3')
                    pygame.mixer.music.play()
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 1
                pygame.mixer.music.load('victory.mp3')
                pygame.mixer.music.set_volume(100)
                pygame.mixer.music.play()
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,500,-50))
            if count == 6:
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()

    root.mainloop()

