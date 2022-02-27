import tkinter as tk 
from tkinter.ttk import *
import sqlite3
from tkinter import *

'''
import speech_recognition as sr # for speech recognition to play songs
import pyttsx3 as tts  # python module for speech
engine = tts.init()
volume = engine.getProperty('volume')
engine.setProperty('volume',0.75)
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
'''

root = tk.Tk()

root.title("DataBase Manager by Mohit Gupta")
root.geometry("800x640")  

#-------------------------create text box--------------------------------------------
songs = Entry(root, width=50)
songs.grid(row=8,column=1,pady=5)
age0_2 = Entry(root, width=50)
age0_2.grid(row=9, column=1,pady=5)
age4_6 = Entry(root, width=50)
age4_6.grid(row=10, column=1,pady=5)
age8_12 = Entry(root, width=50)
age8_12.grid(row=11, column=1,pady=5)
age15_20 = Entry(root, width=50)
age15_20.grid(row=12, column=1,pady=5)
age25_32 = Entry(root, width=50)
age25_32.grid(row=13, column=1,pady=5)
age38_43 = Entry(root, width=50)
age38_43.grid(row=14, column=1,pady=5)
age48_53 = Entry(root, width=50)
age48_53.grid(row=15, column=1,pady=5)
age60_100 = Entry(root, width=50)
age60_100.grid(row=16, column=1,pady=5)
singer_name = Entry(root, width=50)
singer_name.grid(row=17, column=1,pady=5)
h = Entry(root, width=50)
h.grid(row=18, column=1,pady=5)
s = Entry(root, width=50)
s.grid(row=19, column=1,pady=5)
a = Entry(root, width=50)
a.grid(row=20, column=1,pady=5)
cr = Entry(root, width=50)
cr.grid(row=21, column=1,pady=5)
su = Entry(root, width=50)
su.grid(row=22, column=1,pady=5)
delete = Entry(root, width=20)
delete.grid(row=11, column=3, pady=5)

#--------------------------------create text box label--------------------------------------------
songs_label = Label(root, text="Songs",padx=5)
songs_label.grid(row=8, column=0)
age0_2_label = Label(root, text="Age0_2",padx=5)
age0_2_label.grid(row=9, column=0)
age4_6_label = Label(root, text="Age4_6",padx=5)
age4_6_label.grid(row=10, column=0) 
age8_12_label = Label(root, text="Age8_12",padx=5)
age8_12_label.grid(row=11, column=0) 
age15_20_label = Label(root, text="Age15_20",padx=5)
age15_20_label.grid(row=12, column=0) 
age25_32_label = Label(root, text="Age25_32",padx=5)
age25_32_label.grid(row=13, column=0) 
age38_43_label = Label(root, text="Age38_43",padx=5)
age38_43_label.grid(row=14, column=0) 
age48_53_label = Label(root, text="Age48_53",padx=5)
age48_53_label.grid(row=15, column=0) 
age60_100_label = Label(root, text="Age60_100",padx=5)
age60_100_label.grid(row=16, column=0)
singer_name_label = Label(root, text="singer",padx=5)
singer_name_label.grid(row=17, column=0)  
h_label = Label(root, text="Happy",padx=5)
h_label.grid(row=18, column=0) 
s_label = Label(root, text="Sad",padx=5)
s_label.grid(row=19, column=0) 
a_label = Label(root, text="Angry",padx=5)
a_label.grid(row=20, column=0) 
cr_label = Label(root, text="cry",padx=5)
cr_label.grid(row=21, column=0) 
su_label = Label(root, text="Surprise",padx=5)
su_label.grid(row=22, column=0) 
delete_label = Label(root, text="Select ID")
delete_label.grid(row=11, column=2, pady=10)

#----------------------------info---------------------------------------
def update():
	conn = sqlite3.connect('music4.db')
	c = conn.cursor()

	item_id = delete.get() #b3 is delete button

	c.execute("""UPDATE music SET
		songs = :songs,
		age0_2 = :age0_2,
		age4_6 = :age4_6,
		age8_12 = :age8_12,
		age15_20 = :age15_20,
		age25_32 = :age25_32,
		age38_43 = :age38_43,
		age48_53 = :age48_53,
		age60_100 = :age60_100,
		singer_name = :singer_name,
		happy = :h,
		sad = :s,
		angry = :a,
		cry = :cr,
		surprise = :su,
		WHERE oid = :oid""",
		{
			'songs': songs_editor.get(),
			'age0_2': age0_2_editor.get(),
			'age4_6': age4_6_editor.get(),
			'age8_12': age8_12_editor.get(),
			'age15_20': age15_20_editor.get(),
			'age25_32': age25_32_editor.get(),
			'age38_43': age38_43_editor.get(),
			'age48_53': age48_53_editor.get(),
			'age60_100': age60_100_editor.get(),
			'singer_name': singer_name_editor.get(),
			'h': h_editor.get(),
			's': s_editor.get(),
			'a': a_editor.get(),
			'cr': cr_editor.get(),
			'su': su_editor.get(),
			'oid': item_id
		})

	conn.commit()
	conn.close()

def edit():
	editor = Tk()
	editor.title("Information")
	editor.geometry("600x640")

	conn = sqlite3.connect('music4.db')
	c = conn.cursor()

	item_id = delete.get()

	c.execute("SELECT * FROM music WHERE oid = "+ item_id )
	items = c.fetchall()

	songs_editor = Entry(editor, width=50)
	songs_editor.grid(row=8,column=1,pady=5)
	age0_2_editor = Entry(editor, width=50)
	age0_2_editor.grid(row=9, column=1,pady=5)
	age4_6_editor = Entry(editor, width=50)
	age4_6_editor.grid(row=10, column=1,pady=5)
	age8_12_editor = Entry(editor, width=50)
	age8_12_editor.grid(row=11, column=1,pady=5)
	age15_20_editor = Entry(editor, width=50)
	age15_20_editor.grid(row=12, column=1,pady=5)
	age25_32_editor = Entry(editor, width=50)
	age25_32_editor.grid(row=13, column=1,pady=5)
	age38_43_editor = Entry(editor, width=50)
	age38_43_editor.grid(row=14, column=1,pady=5)
	age48_53_editor = Entry(editor, width=50)
	age48_53_editor.grid(row=15, column=1,pady=5)
	age60_100_editor = Entry(editor, width=50)
	age60_100_editor.grid(row=16, column=1,pady=5)
	singer_name_editor = Entry(editor, width=50)
	singer_name_editor.grid(row=17, column=1,pady=5)
	h_editor = Entry(editor, width=50)
	h_editor.grid(row=17, column=1,pady=5)
	s_editor = Entry(editor, width=50)
	s_editor.grid(row=18, column=1,pady=5)
	a_editor = Entry(editor, width=50)
	a_editor.grid(row=19, column=1,pady=5)
	cr_editor = Entry(editor, width=50)
	cr_editor.grid(row=20, column=1,pady=5)
	su_editor= Entry(editor, width=50)
	su_editor.grid(row=21, column=1,pady=5)
#--------------------------------create text box label--------------------------------------------
	songs_label = Label(editor, text="Songs",padx=5)
	songs_label.grid(row=8, column=0)
	age0_2_label = Label(editor, text="Age0_2",padx=5)
	age0_2_label.grid(row=9, column=0)
	age4_6_label = Label(editor, text="Age0_2",padx=5)
	age4_6_label.grid(row=10, column=0) 
	age8_12_label = Label(editor, text="Age0_2",padx=5)
	age8_12_label.grid(row=11, column=0) 
	age15_20_label = Label(editor, text="Age0_2",padx=5)
	age15_20_label.grid(row=12, column=0) 
	age25_32_label = Label(editor, text="Age0_2",padx=5)
	age25_32_label.grid(row=13, column=0) 
	age38_43_label = Label(editor, text="Age0_2",padx=5)
	age38_43_label.grid(row=14, column=0) 
	age48_53_label = Label(editor, text="Age0_2",padx=5)
	age48_53_label.grid(row=15, column=0) 
	age60_100_label = Label(editor, text="Age0_2",padx=5)
	age60_100_label.grid(row=16, column=0)
	singer_name_label = Label(editor, text="Age0_2",padx=5)
	singer_name_label.grid(row=17, column=0)  
	h_label = Label(editor, text="Happy",padx=5)
	h_label.grid(row=17, column=0) 
	s_label = Label(editor, text="Sad",padx=5)
	s_label.grid(row=18, column=0) 
	a_label = Label(editor, text="Angry",padx=5)
	a_label.grid(row=19, column=0) 
	cr_label = Label(editor, text="cry",padx=5)
	cr_label.grid(row=20, column=0) 
	su_label = Label(editor, text="Surprise",padx=5)
	su_label.grid(row=21, column=0)

	for item in items:
		songs_editor.insert(0, item[0])
		age0_2_editor.insert(0, item[1])
		age4_6_editor.insert(0, item[2])
		age8_12_editor.insert(0, item[3])
		age15_20_editor.insert(0, item[4])
		age25_32_editor.insert(0, item[5])
		age38_43_editor.insert(0, item[6])
		age48_53_editor.insert(0, item[7])
		age60_100_editor.insert(0, item[8])
		singer_name_editor.insert(0, item[9])
		h_editor.insert(0, item[10])
		s_editor.insert(0, item[11])
		a_editor.insert(0, item[12])
		cr_editor.insert(0, item[13])
		su_editor.insert(0, item[14])
	
	b4_edit = Button(editor, text = "Info",padx=50,fg="white",pady=5,bg="blue")
	b4_edit.grid(row=34, column=1)




#--------------------------------ADD TO DATABASE FUNCTION----------------------------
#add a new record to the table
def add_one():
	conn = sqlite3.connect('music4.db')
	c = conn.cursor()

	c.execute("INSERT INTO music VALUES (:songs, :age0_2, :age4_6, :age8_12, :age15_20, :age25_32, :age38_43, :age48_53, :age60_100, :singer_name, :h, :s, :a, :cr, :su)",
			{
				'songs': songs.get(),
				'age0_2': age0_2.get(),
				'age4_6': age4_6.get(),
				'age8_12': age8_12.get(),
				'age15_20': age15_20.get(),
				'age25_32': age25_32.get(),
				'age38_43': age38_43.get(),
				'age48_53': age48_53.get(),
				'age60_100': age60_100.get(),
				'singer_name': singer_name.get(),
				'h': h.get(),
				's': s.get(),
				'a': a.get(),
				'cr': cr.get(),
				'su': su.get()
			})

	songs.delete(0, END)
	age0_2.delete(0, END)
	age4_6.delete(0, END) 
	age8_12.delete(0, END) 
	age15_20.delete(0, END)
	age25_32.delete(0, END)
	age38_43.delete(0, END)
	age48_53.delete(0, END)
	age60_100.delete(0, END)
	singer_name.delete(0, END)
	h.delete(0, END)
	s.delete(0, END)
	a.delete(0, END)
	cr.delete(0, END)
	su.delete(0, END)

	conn.commit()
	conn.close()

'''
def show_allsongs():
	conn = sqlite3.connect('music4.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM music WHERE age25_32 LIKE '1' AND happy LIKE '1'")
	items = c.fetchall()
    #print(str(items))
SELECT rowid, * FROM music
	for item in items:
        # print(item)
		print(str(item[0]) + "\t\t" + str(item[1]) + "\t\t" + str(item[2]) + "\t\t" + str(item[3]) + "\t\t" + str(item[4])+ "\t\t" + str(item[5] + str(item[6]) + "\t\t" + str(item[7]) + "\t\t" + str(item[8]) + "\t\t" + str(item[9]) + "\t\t" + str(item[10])+ "\t\t" + str(item[11])+ str(item[12])+ "\t\t" + str(item[13]))
	# conn.commit()
	# conn.close()
'''

def show_allSongs():
    conn = sqlite3.connect('music4.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM music")
    items = c.fetchall()
    # print(items)

    print_items = ''
    
    for item in items:
        print_items = str(item[0]) + " " + str(item[1]) + "\t\t\t|" + str(item[2]) + "   " + str(item[3]) + "    " + str(item[4])+ "    " + str(item[5]) + "    " + str(item[6]) + "    " + str(item[7]) + "    " + str(item[8]) + "    " + str(item[9]) + "  |  " + str(item[11]) + "    " + str(item[12]) + "    " + str(item[13]) + "    " + str(item[14]) + "    " + str(item[15]) + " | " + str(item[10])
        #print_items += "\n"
        print(print_items)
    print("---------------------------------------------------------------------------------------------------\n")
    # b8_label = Label(root, text=print_items)
    # b8_label.grid(row=22, column=0,columnspan=2)

    conn.commit()
    conn.close()

#--------------------------------------------------------------------------------------
######CREATE A TABLE FUNCTION
def create_table():
	conn = sqlite3.connect('music4.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE music(
						songs text,
						age0_2 text,
						age4_6 text,
						age8_12 text,
						age15_20 text,
						age25_32 text,
						age38_43 text,
						age48_53 text,
						age60_100 text,
						singer_name text,
						happy text,
						sad text,
						cry text,
						angry text,
						surprise text
						)""")
	conn.commit()
	conn.close()



#--------------------------------deleting record---------------------------------------------
def delete_one():
	conn = sqlite3.connect('music4.db')
	c = conn.cursor()

	c.execute("DELETE from music WHERE rowid = " + delete.get())

	delete.delete(0, END)

	conn.commit()
	conn.close()



label1 = Label(root, text = "   ",pady=10)

b1 = Button(root, text = "Create table", command = create_table,padx=35,fg="white",pady=5,bg="green")
b2 = Button(root, text = "AddToDatabase", command = add_one,padx=25,fg="white",pady=5,bg="orange")
b3 = Button(root, text = "Delete", command = delete_one,padx=52.3,fg="white",pady=5,bg="Red")
b4 = Button(root, text = "Info", command = edit,padx=50,fg="white",pady=5,bg="blue")
b5 = Button(root, text = "DataBase Management System by Mohit Gupta",padx=125,pady=10,fg="White",bg="black")
b6 = Button(root, text = "Tools",state=DISABLED,padx=55,pady=10)
b7 = Button(root, text = "# USE FOR ADD TOOL ",state=DISABLED,padx=30,pady=10)
b8 = Button(root, text = "Displayall", command = show_allSongs,padx=25,fg="white",pady=5,bg="orange")

label1.grid(row=2, column=3)
b1.grid(row=6, column=3)
b2.grid(row=23, column=1)
b3.grid(row=12, column=3)
b4.grid(row=14, column=3)
b5.grid(row=1, column=1)
b6.grid(row=1, column=3)
b7.grid(row=2, column=1)
b8.grid(row=25, column=1)


# calling mainloop method which is used 
# when your application is ready to run 
# and it tells the code to keep displaying  
root.mainloop() 