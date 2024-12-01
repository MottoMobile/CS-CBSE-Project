'''
Developments to be done:-
Display record with search 
Give option with search criteria (search by name emp code or any other criteria)
'''
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector as sq
from mysql.connector import connect
from PIL import ImageTk, Image
import os


# Creating a Database and Table to store all the records of the company employees
def create():
    mydb = sq.connect(host="localhost",user="root",password="root")
    mycursor = mydb.cursor()
    sql = "Create database Game_Database"
    mycursor.execute(sql)
    mycursor.execute("Use Game_Database")
    mydb.commit()
    mycursor.execute("Create table Games(Game_Name VARCHAR(500), Genre VARCHAR(100), date_of_release DATE, Price INTEGER,Developer VARCHAR(500), Platforms VARCHAR(500))")
    mydb.commit()



# This part of code is to insert record
def insert():
    root.destroy()  # Closing main tk page
    insertk=tk.Tk()  # Opening a tk page for insert option
    insertk.geometry('1920x1080')

    # Image for background    
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\Background.png"))
    panel = tk.Label(insertk, image = img)
    panel.pack(side = "bottom", fill = "both")

    insertk.configure(bg='azure2')
    insertk.title('Insert Record')
    
    # Introducing labels for this option
    lab0=tk.Label(insertk,text='Fill out the below information',bg='azure2',font=('Arial',20,'bold'))
    lab1=tk.Label(insertk,text="Name of the Game:",bg='azure2',font=('Arial',16))
    lab2=tk.Label(insertk,text="Genre of the Game:",bg='azure2',font=('Arial',16))
    lab3=tk.Label(insertk,text="Launch Date:",bg='azure2',font=('Arial',16))
    lab4=tk.Label(insertk,text="Price:",bg='azure2',font=('Arial',16))
    lab5=tk.Label(insertk,text="Game Developer:",bg='azure2',font=('Arial',16))
    lab6=tk.Label(insertk,text="Platform(s):",bg='azure2',font=('Arial',16))

    # Placing the labels
    lab0.place(x=550,y=70)
    lab1.place(x=500,y=190)
    lab2.place(x=500,y=235)
    lab3.place(x=500,y=280)
    lab4.place(x=500,y=325)
    lab5.place(x=500,y=370)
    lab6.place(x=500,y=415)

    # initializing variable to read entry box data
    nm=StringVar()
    genre=StringVar()
    dor=StringVar()
    pr=StringVar()
    dev=StringVar()
    pf=StringVar()

    # Producing Entry boxes
    en1=tk.Entry(insertk,textvariable=nm,font=('Arial',16),bg='azure1')
    en2=tk.Entry(insertk,textvariable=genre,font=('Arial',16),bg='azure1')
    en3=tk.Entry(insertk,textvariable=dor,font=('Arial',16),bg='azure1')
    en4=tk.Entry(insertk,textvariable=pr,font=('Arial',16),bg='azure1')
    en5=tk.Entry(insertk,textvariable=dev,font=('Arial',16),bg='azure1')
    en6=tk.Entry(insertk,textvariable=pf,font=('Arial',16),bg='azure1')
    
    # Placing the entry boxes
    en1.place(x=780,y=190)
    en2.place(x=780,y=235)
    en3.place(x=780,y=280)
    en4.place(x=780,y=325)
    en5.place(x=780,y=370)
    en6.place(x=780,y=415)

    # Button functionality [ logic for the insert option ]
    def insertin():
        Name=nm.get()
        Genre=genre.get()
        DOR=dor.get()
        Price=pr.get()
        Developer=dev.get()
        Platform=pf.get()

        mydb = sq.connect(host="localhost",user="root",password="root",database="Game_Database")
        mycursor = mydb.cursor()
        sql = "INSERT INTO Games (Game_Name, Genre, Date_of_release, Price, Developer, Platforms) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (Name,Genre,DOR,Price,Developer,Platform)
        mycursor.execute(sql, val)
        mydb.commit()
        
        added=tk.Label(insertk,text='Record Inserted',font=('Arial',24),bg='azure2')
        added.place(x=630,y=575)
        
        nm.set('')
        genre.set('')
        dor.set('')
        pr.set('')
        dev.set('')
        pf.set('')    

    # Introducing button with command
    btin=tk.Button(insertk,text='Enter',font=('Arial',20),command=insertin,bg='azure2')
    btin.place(x=690,y=500)

    # Creating a function to ask confirmation from user for quiting
    def on_closing6():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            insertk.destroy() # Closing this window
            recreate_root() # Re-opening root window
        else:
            pass 
    insertk.protocol('WM_DELETE_WINDOW',on_closing6)
    insertk.mainloop()  

#This code is to update record
def update():
    root.destroy()
    updatetk=tk.Tk()
    updatetk.geometry('1920x1080')

    # Image for Background
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\Background.png"))
    panel = tk.Label(updatetk, image = img)
    panel.pack(side = "bottom", fill = "both")


    updatetk.configure(bg='azure2')
    updatetk.title('Update Record')
    
    # Introducing labels for this option
    lab0=tk.Label(updatetk,text='Update Record',font=('Arial',20,'bold'),bg='azure2')
    lab1=tk.Label(updatetk,text='--> 1. Game name ',font=('Arial',16),bg='azure2')
    lab2=tk.Label(updatetk,text='--> 2. Genre',font=('Arial',16),bg='azure2')
    lab3=tk.Label(updatetk,text='--> 3. Launch Date',font=('Arial',16),bg='azure2')
    lab4=tk.Label(updatetk,text='--> 4. Price',font=('Arial',16),bg='azure2')
    lab5=tk.Label(updatetk,text='--> 5. Developer',font=('Arial',16),bg='azure2')
    lab9=tk.Label(updatetk,text='--> 6. Platform(s)',font=('Arial',16),bg='azure2')
    lab6=tk.Label(updatetk,text="Game name whose record you want to update:",font=('Arial',16),bg='azure2')
    lab7=tk.Label(updatetk,text="Record you want to update:",font=('Arial',16),bg='azure2')
    lab8=tk.Label(updatetk,text="Enter the change:",font=('Arial',16),bg='azure2')

    # Placing the labels
    lab0.place(x=600,y=70)
    lab6.place(x=480,y=190)
    lab1.place(x=540,y=235)
    lab2.place(x=540,y=280)
    lab3.place(x=540,y=325)
    lab4.place(x=540,y=370)
    lab5.place(x=540,y=415)
    lab9.place(x=540,y=460)
    lab7.place(x=480,y=515)
    lab8.place(x=480,y=560)
    
    # Initialising variable to read entry box
    upe=StringVar()
    fi=StringVar()
    fich=StringVar()

    # Producing Entry boxes
    en1=tk.Entry(updatetk,textvariable=upe,font=('Arial',14),bg='azure1') 
    en2=tk.Entry(updatetk,textvariable=fi,font=('Arial',14),bg='azure1') 
    en3=tk.Entry(updatetk,textvariable=fich,font=('Arial',14),bg='azure1') 

    # Placing entry boxes
    en1.place(x=1000,y=190)
    en2.place(x=1000,y=515)
    en3.place(x=1000,y=560)
    
    # Button functionality [ logic for the update option ]
    def updateit():
        up=upe.get()
        fields=int(fi.get())
        fieldch=fich.get()
        if fields==1:
            field='Game_Name'
        elif fields==2:
            field='Genre'
        elif fields==3:
            field='Date_of_release'
        elif fields==4:
            field='Price'
        elif fields==5:
            field='Developer'
        elif fields==6:
            field='Platforms'
        mydb= sq.connect(host="localhost",user="root",passwd="root",database="Game_Database")
        cursor=mydb.cursor()
        update="UPDATE Games set {} = '{}' WHERE Game_Name like '{}'".format(field,fieldch,up)
        cursor.execute(update)
        mydb.commit()
        lab0=tk.Label(updatetk,text="Record Updated",font=('Arial',24),bg='azure2')
        lab0.place(x=600,y=650)
        upe.set('')
        fi.set('')
        fich.set('')

    # Introducing Button with command
    bt1=tk.Button(updatetk,text='Update',font=('Arial',18),bg='azure2',command=updateit)
    bt1.place(x=660,y=600)

    # Creating a function to ask confirmation from user for quiting
    def on_closing5():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            updatetk.destroy() # Closing the window
            recreate_root() # Re-opening root window
        else:
            pass 
    updatetk.protocol('WM_DELETE_WINDOW',on_closing5)
    updatetk.mainloop()

# This code is the delete a record 
def delete():
    root.destroy()
    deletetk=tk.Tk()        
    deletetk.geometry('1920x1080')

    # Image for background
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\Background.png"))
    panel = tk.Label(deletetk, image = img)
    panel.pack(side = "bottom", fill = "both")

    deletetk.configure(bg='azure2')
    deletetk.title('Delete Record')

    # Introducing labels for this option
    lab0=tk.Label(deletetk,text="Delete Record",font=('Arial',20,'bold'),bg='azure2')
    lab1=tk.Label(deletetk,text="Enter the Game name whose data you want to delete:",font=('Arial',16),bg='azure2')
    
    # Placing labels
    lab0.place(x=660,y=70)
    lab1.place(x=350,y=190)

    # Initialising variable to read entry box
    de=StringVar()

    # Producing and placing entry box
    en1=tk.Entry(deletetk,textvariable=de,font=('Arial',16),bg='azure1')
    en1.place(x=870,y=190)
    
    # Button functionality [ logic for the delete option ]
    def deleteit():
        dele=de.get()
        c=sq.connect(host="localhost",user="root",passwd="root",database="Game_Database")
        cursor=c.cursor()
        sql = "DELETE FROM Games WHERE Game_Name like '%{}%'".format(dele)
        cursor.execute(sql)
        c.commit()
        lab2=tk.Label(deletetk,text="Record Deleted",font=('Arial',24,'bold'),bg='azure2')
        lab2.place(x=630,y=300)
        de.set('')

    # Intorducing button with command
    btn1=tk.Button(text='Delete',font=('Arial',18),bg='azure2',command=deleteit)
    btn1.place(x=700,y=240)

    # Creating a function to ask confirmation from user for quiting
    def on_closing4():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            deletetk.destroy() # Closing this window
            recreate_root() # Re-opening root window
        else:
            pass 
    deletetk.protocol('WM_DELETE_WINDOW',on_closing4)
    deletetk.mainloop()

#This code is to search an anime from the list
def search():
    root.destroy()
    searchtk=tk.Tk()
    searchtk.geometry('1920x1080')

    #Image for background
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\Background.png"))
    panel = tk.Label(searchtk, image = img)
    panel.pack(side = "bottom", fill = "both")

    searchtk.title('Search Record')
    searchtk.configure(bg='azure2')
    
    lab1=tk.Label(searchtk,text="Game Name:",font=('Arial',16),bg='azure2')
    lab1.place(x=540,y=190)
    lab2=tk.Label(searchtk,text="Search Record",font=('Arial',20,'bold'),bg='azure2')
    lab2.place(x=640,y=70)

    se=StringVar()

    en1=tk.Entry(searchtk,textvariable=se,font=('Arial',16),bg='azure1')
    en1.place(x=690,y=190)

    def searchit():
        try:
            pat = se.get()
            mydb = sq.connect(host='localhost', user='root', password='root', database='Game_Database')
            cursor = mydb.cursor()
            q = "SELECT * FROM Games WHERE Game_Name LIKE '%{}%'".format(pat)
            cursor.execute(q)
            result = cursor.fetchall()

            if result:
                lab2 = tk.Label(searchtk, text='Record is available', font=('Arial', 18), bg='azure2')
                lab2.place(x=620, y=310)
            else:
                lab2 = tk.Label(searchtk, text='Record is not available', font=('Arial', 18), bg='azure2')
                lab2.place(x=620, y=310)
        except Exception as e:
            print(f"Error: {e}")

    # Introducing button with commands
    btn1=tk.Button(searchtk,text='Search',command=searchit,font=('Arial',14),bg='azure2')
    btn1.place(x=700,y=250)

    # Creating a function to ask confirmation from user for quiting
    def on_closing3():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            searchtk.destroy()
            recreate_root()
        else:
            pass 
    searchtk.protocol('WM_DELETE_WINDOW',on_closing3)
    searchtk.mainloop()

def display():
    # This code is to display all the records
    root.destroy()
    displaytk = tk.Tk()
    displaytk.configure(bg='azure2')
    displaytk.geometry('1920x1080')

    # Image for background
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\Background.png"))
    panel = tk.Label(displaytk, image = img)
    panel.pack(side = "bottom", fill = "both")

    displaytk.title('Display Record')

    mydb= sq.connect(host="localhost", user="root", password="root", database="Game_Database")
    cursor = mydb.cursor()
    sql = "SELECT * FROM Games ORDER BY Game_Name"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    lab1=tk.Label(displaytk,text='Displaying Records',font=('Arial',20,'bold'),bg='azure2')
    lab1.place(x=650,y=70)
    # Display header labels
    header_labels = ['Game Name', 'Genre', 'Date of Release', 'Price', 'Developer', 'Platform(s)']
    for i, header in enumerate(header_labels):
        tk.Label(displaytk, text=f'{i + 1}. {header}', font=('Arial', 16), bg='azure2').place(x=610, y=190 + i * 45)

    # Display employee records
    for i, record in enumerate(myresult):
        record_text = ', '.join(map(str, record))
        tk.Label(displaytk, text=record_text, font=('Arial', 16), bg='azure2').place(x=550, y=500 + i * 45)

    # Creating a function to ask confirmation from user for quiting
    def on_closing2():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            displaytk.destroy() # Closing this window
            recreate_root() # Re-opening root window
        else:
            pass 
    displaytk.protocol('WM_DELETE_WINDOW',on_closing2)
    displaytk.mainloop()


# Re-opening the root window which asks for function the user want to apply
# This is an extra feature to reopen the window once it is closed

# Defining an empty variable.
l=0

def recreate_root():
    global root
    global root1
    global l
    #Taking the root window we created earlier

    # This is all the labels and other functions available in this window
    
    if l==0:
        root1.destroy()
        l+=1
    else:
        pass
    root=tk.Tk() 
    root.geometry('1920x1080')
    root.configure(bg='azure2')
    root.title('Option Page')

    img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\Background.png"))
    panel = tk.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both")
    
    lab3=tk.Label(root, text="WELCOME TO GAME DATABASE",font=('Arial',20,'bold'),bg='azure2')
    lab6=tk.Label(root, text="Made By: Ishaan Chhaya",font=('Arial',20,'bold'),bg='azure2')
    lab3.place(x=540,y=70)  # Positioning the labels
    lab6.place(x=590,y=130)  

    lin1=tk.Label(root,text="1.Insert new data ",font=('Arial',16),bg='azure2')
    lin2=tk.Label(root,text="2.Update the table",font=('Arial',16),bg='azure2')
    lin3=tk.Label(root,text="3.Delete the record from the table",font=('Arial',16),bg='azure2')
    lin4=tk.Label(root,text="4.Search a record from the table",font=('Arial',16),bg='azure2')
    lin5=tk.Label(root,text="5.Display the table",font=('Arial',16),bg='azure2')
    lin6=tk.Label(root,text="6.Quit",font=('Arial',16),bg='azure2')

    lin1.place(x=540,y=190)
    lin2.place(x=540,y=235)
    lin3.place(x=540,y=280)
    lin4.place(x=540,y=325)
    lin5.place(x=540,y=370)
    lin6.place(x=540,y=415)

    ch=StringVar() # Creating a variable to store value input from entry box
    
    lab1=tk.Label(root,text="Which function do you want to apply:",font=('Arial',16),bg='azure2')
    lab1.place(x=540,y=470)

    en1=tk.Entry(root, textvariable=ch, font=('Arial',16),bg='azure1')
    en1.place(x=560,y=525)

    # Creating a function to ask confirmation from user for quiting
    def on_closing1():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                root.destroy()
            else:
                pass 
    # Creating if else to run each function as asked by user
    def choicefunc():
        choice=ch.get()
        if choice=='1':  # To insert new data
            insert()        
        #To update
        elif choice=='2':
            update()
        #To delete a record
        elif choice=='3':
            delete()
        #To search a record
        elif choice=='4':
            search()
        #To Display the data
        elif choice=='5':
            display()   
        else:
            on_closing1()

    # Creating button with command to run the functions
    btn1=tk.Button(root,text='Enter',font=('Arial',16),bg='azure2',command=choicefunc)
    btn1.place(x=815,y=520)
    root.mainloop()
    #Recreating the option window


# Checking the existence of the database and to create if does not exist and create if does not exist
def check_database_existence():
    user_=Username.get()
    pwd=Password.get()
    try:
        mydb = sq.connect(host="localhost",user=user_,password=pwd,database="Game_Database")
        recreate_root()
    except sq.Error as e:
        if e.errno == 1049:  # MySQL error code for "Unknown database"
            create()
        else:
            print(f"Error: {e}")
# Login page

# Function for showing the entered credentials and progressing to next protocol
def submitact():
     
    user = Username.get()
    passw = Password.get()
  
    print(f"The name entered by you is {user} {passw}")
  
    logintodb(user, passw)

# Function to check and run the log in process
def logintodb(user,passw):
    if user in 'root' and passw in 'root':
        check_database_existence()


# GUI for Log in Page    
root1 = tk.Tk()
root1.geometry("1920x1080")
root1.configure(bg='light slate gray')
root1.title("DBMS Login Page")

# Image for Log In page
img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\LOG IN.png"))
panel = tk.Label(root1, image = img)
panel.pack(side = "bottom", fill = "both")
 
# Defining the first row
lblfrstrow = tk.Label(root1, text ="Username: ", font=('Arial', 22))
lblfrstrow.place(x =640, y = 470, width =155)
lblfrstrow.configure(bg='light slate gray')

# Entry for Username
Username = tk.Entry(root1,textvariable= chr, bg='azure1',font=('Arial',20))
Username.place(x = 800, y = 473, width = 100)

# Defining the second row
lblsecrow = tk.Label(root1, text ="Password: ", font=('Arial', 22))
lblsecrow.place(x = 640, y = 520, width=155)
lblsecrow.configure(bg='light slate gray')

# Entry for Password
Password = tk.Entry(root1, textvariable=chr, bg='azure1',font=('Arial',20))
Password.place(x = 800, y = 523, width = 100)

# Log in button  
submitbtn = tk.Button(root1, text ="LOG IN", 
                      bg ='LightSteelBlue1', command = submitact, font=('Arial', 16))
submitbtn.place(x = 730, y = 600, width = 80)
 
root1.mainloop()







# Root window
root=tk.Tk()
root.geometry('1920x1080')
root.configure(bg='azure2')
root.title('Option Page')


img = ImageTk.PhotoImage(Image.open("C:\\Users\\ishaa\\Desktop\\Background.png"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both")
 
lab3=tk.Label(root,text="WELCOME TO GAME DATABASE",font=('Arial',18,'bold'),bg='azure2')
lab6=tk.Label(root, text="Made By: Ishaan Chhaya",font=('Arial',18,'bold'),bg='azure2')
lab3.place(x=540,y=70)  
lab6.place(x=590,y=130)
lin1=tk.Label(root,text="1.Insert new data ",font=('Arial',14),bg='azure2')
lin2=tk.Label(root,text="2.Update the table",font=('Arial',14),bg='azure2')
lin3=tk.Label(root,text="3.Delete the record from the table",font=('Arial',14),bg='azure2')
lin4=tk.Label(root,text="4.Search a record from the table",font=('Arial',14),bg='azure2')
lin5=tk.Label(root,text="5.Display the table",font=('Arial',14),bg='azure2')
lin6=tk.Label(root,text="6.Quit",font=('Arial',14),bg='azure2')

lin1.place(x=540,y=190)
lin2.place(x=540,y=235)
lin3.place(x=540,y=280)
lin4.place(x=540,y=325)
lin5.place(x=540,y=370)
lin6.place(x=540,y=415)

ch=StringVar()
   
lab1=tk.Label(root,text="Which function do you want to apply:",font=('Arial',16),bg='azure2')
lab1.place(x=540,y=470)

en1=tk.Entry(root, textvariable=ch, font=('Arial',16),bg='azure1')
en1.place(x=560,y=525)

# Creating a function to ask confirmation from user for quiting
def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            root.destroy() #closing root window
        else:
            pass 
def choicefunc():
    choice=ch.get()

    # To insert new data
    if choice=='1':  
        insert()
    #To update
    elif choice=='2':
        update()   
    #To delete a record
    elif choice=='3':
        delete()  
    #To search a record
    elif choice=='4':
        search()
    #To Display the data
    elif choice=='5':
        display() 
    else:
        on_closing()


btn1=tk.Button(root,text='Enter',font=('Arial',14),bg='azure2',command=choicefunc)
btn1.place(x=815,y=520)
root.mainloop()
