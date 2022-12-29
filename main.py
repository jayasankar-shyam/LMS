##################-----ADMIN WINDOW-----###################
def admin():
    root.destroy()
    adm=Tk()
    title="Administrator"
    adm.title(title)            
    adm.geometry("1500x720+10+30")
    adm.configure(bg="")
    adm.resizable(False,False)
    
    
    def issue_book():
        ilab=Label(frame,text="Enter the student id number",fg="black", bg="white", font=("Microsoft Yahei Light", 18, "bold"))
        ilab.place(x=50,y=350)
        iss=Frame(adm,width=900,height=300,bg="white")
        iss.place(x=325,y=430)
        def on_enter(e):
            user.delete(0, "end")
        def on_leave(e):
            name=user.get()
            if name == "":
                user.insert(0,"ID")
        user = Entry(iss, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
        user.place(x=300, y=10)
        user.insert(0,"ID")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        Frame(iss, width=295, height=2, bg="black").place(x=300, y=30)

        
        def issue_win():
            idno=user.get()
            sql="Select name from users where id=%s"
            cur.execute(sql, [(idno)])
            name=cur.fetchall()
            n=""
            for i in name:
                for j in i:
                    n+=j
            ###USER CHECK####
            if n=="":
                msg=messagebox.showerror(title="Wrong ID",message="User does not exist")
                return 0
            uwin=Tk()
            title="Issue Books"
            uwin.title(title)            
            uwin.geometry("1500x720+10+30")
            uwin.resizable(False,False)
            uwin.configure(bg="")
            # Frame of the GUI
            Label(uwin, bg="white").place(x=50, y=50)
            frame = Frame(uwin, width=1500, height=70, bg="white")
            frame.place(x=550, y=0)
            # Sign in Header
            heading = Label(frame, text="Issue Books", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))
            heading.place(x=100, y=10)
            contents=Frame(uwin,width=1500,height=500,bg="white")
            contents.place(x=10,y=100)
            name_label=Label(contents,text="Name of the Student : ", bg="white", font=("Microsoft Yahei Light", 15, "bold"))
            student_label=Label(contents,text=n, bg="white", font=("Microsoft Yahei Light", 15, "bold"))
            
            ################# BOOKS################################## 
            bookFrame=Frame(uwin,height=500,width=400, bg="#57a1f8")
            bookFrame.place(x=20,y=200)
            books_label=Label(bookFrame,text="Issued Books",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15, "bold"))
            id_label=Label(bookFrame,text="ID",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            title_label=Label(bookFrame,text="Title",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            books_label.place(x=120,y=10)
            id_label.place(x=30,y=50)
            title_label.place(x=180,y=50)
            
            
            name_label.place(x=10,y=50)
            student_label.place(x=250,y=50)

            
            books_list="select b.id,title from books b inner join book_issued bi ON bi.book_id=b.id where bi.user_id=%s;"
            cur.execute(books_list,[(idno)])
            books_list=cur.fetchall()
            list_books=[]
            id_books=[]
            for i in books_list:
                list_books.append(i[1])
                id_books.append(i[0])  
            ycor=100

            for i,j in zip(list_books,id_books):
                id1=Label(bookFrame,text=j,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1=Label(bookFrame,text=i,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1.place(x=180,y=ycor)
                id1.place(x=30,y=ycor)
                ycor+=50

            #################AVAILABLE BOOKS##################################    
            bookAvailable=Frame(uwin,height=500,width=400, bg="#57a1f8")
            bookAvailable.place(x=1080,y=200)
            books_label=Label(bookAvailable,text="Available Books",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15, "bold"))
            id_label=Label(bookAvailable,text="ID",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            title_label=Label(bookAvailable,text="Title",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            id_label.place(x=30,y=50)
            title_label.place(x=180,y=50)
            
            books_label.place(x=120,y=10)
            
            books_list="select id ,title from books WHERE id not in (select b.id from books b inner join book_issued bi ON bi.book_id=b.id where bi.user_id=%s);"
            cur.execute(books_list,[(idno)])
            books_list=cur.fetchall()
            list_books=[]
            id_books=[]
            for i in books_list:
                list_books.append(i[1])
                id_books.append(i[0])    
            ycor=100
            num=1
            for i,j in zip(list_books,id_books):
                id1=Label(bookAvailable,text=j,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1=Label(bookAvailable,text=i,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1.place(x=180,y=ycor)
                id1.place(x=30,y=ycor)
                ycor+=50
            
            #######################Center portion#########################
            center=Frame(uwin,height=500,width=400, bg="white")
            center.place(x=550,y=300)
            ques=Label(center,text="Enter the id of the book to be issued",bg="white",font=("Microsoft Yahei Light", 14, "bold"))
            ques.place(x=30,y=10)
            iss=Frame(center,width=400,height=300,bg="white")
            iss.place(x=40,y=70)
            def on_enter(e):
                idn.delete(0, "end")
            def on_leave(e):
                name=idn.get()
                if name == "":
                    user.insert(0,"ID")
            idn = Entry(iss, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
            idn.place(x=30, y=10)
            idn.insert(0,"ID")
            idn.bind("<FocusIn>", on_enter)
            idn.bind("<FocusOut>", on_leave)
            Frame(iss, width=295, height=2, bg="black").place(x=30, y=30)
            ###########################INSERT INTO BOOK ISSUED####################################
            def insert():
                bid=idn.get()
                sql="SELECT book_id from book_issued where user_id=%s"
                cur.execute(sql,[(idno)])
                res=cur.fetchall()
                if (int(bid),) in res:
                    msg=messagebox.showerror(title="Book Already Issued",message="Book Already Issued")
                elif int(bid) not in id_books:
                    msg=messagebox.showerror(title="Invalid ID",message="Book does not exist")
                else:   
                    sql="INSERT INTO book_issued(book_id,user_id) VALUES (%s,%s)"
                    cur.execute(sql,[(bid),(idno)])
                    conn.commit()
                    sql="SELECT book_id from book_issued where user_id=%s"
                    cur.execute(sql,[(idno)])
                    res=cur.fetchall()
                    if (int(bid),) in res:
                        msg=messagebox.showinfo(title="Book Issued",message="Book Issued Successfully")
                    else:
                         msg=messagebox.showerror(title="Book Not Issued",message="Error Occured while issuing")
                if msg=="ok":
                    uwin.destroy()
            Button(iss, width=15, pady=5, text="Submit", bg="#57a1f8", fg="white", border=0, command=insert,font=("Microsoft Yahei Light", 10, "bold")).place(x=100, y=90)
            
            uwin.mainloop()
 
        
    
    
        Button(iss, width=15, pady=5, text="Submit", bg="#57a1f8", fg="white", border=0, command=issue_win,font=("Microsoft Yahei Light", 10, "bold")).place(x=380, y=90)
           
########################################---RETURN BOOK---##########################################################
    def return_book():
        retlab=Label(frame,text="Enter the student id number",fg="black", bg="white", font=("Microsoft Yahei Light", 18, "bold"))
        retlab.place(x=50,y=350)
        ret=Frame(adm,width=900,height=300,bg="white")
        ret.place(x=325,y=430)
        def on_enter(e):
            user.delete(0, "end")
        def on_leave(e):
            name=user.get()
            if name == "":
                user.insert(0,"ID")
        user = Entry(ret, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
        user.place(x=300, y=10)
        user.insert(0,"ID")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        Frame(ret, width=295, height=2, bg="black").place(x=300, y=30)
        
        def return_win():
            idno=user.get()
            sql="Select name from users where id=%s"
            cur.execute(sql, [(idno)])
            name=cur.fetchall()
            conn.commit()
            n=""
            for i in name:
                for j in i:
                    n+=j 
            ###USER CHECK####
            if n=="":
                msg=messagebox.showerror(title="Wrong ID",message="User does not exist")
                return 0
            uwin=Tk()
            title="Return Books"
            uwin.title(title)            
            uwin.geometry("1500x720+10+30")
            uwin.configure(bg="")
            uwin.resizable(False,False)
            # Frame of the GUI
            Label(uwin, bg="white").place(x=50, y=50)
            frame = Frame(uwin, width=1500, height=70, bg="white")
            frame.place(x=550, y=0)
            # Sign in Header
            heading = Label(frame, text="Return Books", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))
            heading.place(x=100, y=10)
            contents=Frame(uwin,width=1500,height=500,bg="white")
            contents.place(x=10,y=100)
            name_label=Label(contents,text="Name of the Student : ", bg="white", font=("Microsoft Yahei Light", 15, "bold"))
            student_label=Label(contents,text=n, bg="white", font=("Microsoft Yahei Light", 15, "bold"))
            
            ################# BOOKS################################## 
            bookFrame=Frame(uwin,height=500,width=400, bg="#57a1f8")
            bookFrame.place(x=20,y=200)
            books_label=Label(bookFrame,text="Issued Books",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15, "bold"))
            id_label=Label(bookFrame,text="ID",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            title_label=Label(bookFrame,text="Title",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            books_label.place(x=120,y=10)
            id_label.place(x=30,y=50)
            title_label.place(x=180,y=50)
            
            
            name_label.place(x=10,y=50)
            student_label.place(x=250,y=50)

            
            books_list="select b.id,title from books b inner join book_issued bi ON bi.book_id=b.id where bi.user_id=%s;"
            cur.execute(books_list,[(idno)])
            books_list=cur.fetchall()
            list_books=[]
            id_books=[]
            for i in books_list:
                list_books.append(i[1])
                id_books.append(i[0])  
            ycor=100

            for i,j in zip(list_books,id_books):
                id1=Label(bookFrame,text=j,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1=Label(bookFrame,text=i,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1.place(x=180,y=ycor)
                id1.place(x=30,y=ycor)
                ycor+=50

            #################AVAILABLE BOOKS##################################    
            bookAvailable=Frame(uwin,height=500,width=400, bg="#57a1f8")
            bookAvailable.place(x=1080,y=200)
            books_label=Label(bookAvailable,text="Available Books",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15, "bold"))
            id_label=Label(bookAvailable,text="ID",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            title_label=Label(bookAvailable,text="Title",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 13, "bold"))
            id_label.place(x=30,y=50)
            title_label.place(x=180,y=50)
            
            books_label.place(x=120,y=10)
            
            books_list="select id ,title from books WHERE id not in (select b.id from books b inner join book_issued bi ON bi.book_id=b.id where bi.user_id=%s);"
            cur.execute(books_list,[(idno)])
            books_list=cur.fetchall()
            list_books=[]
            id_books=[]
            for i in books_list:
                list_books.append(i[1])
                id_books.append(i[0])    
            ycor=100
            num=1
            for i,j in zip(list_books,id_books):
                id1=Label(bookAvailable,text=j,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1=Label(bookAvailable,text=i,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
                book1.place(x=180,y=ycor)
                id1.place(x=30,y=ycor)
                ycor+=50
            
            #######################Center portion#########################
            center=Frame(uwin,height=500,width=500, bg="white")
            center.place(x=550,y=300)
            ques=Label(center,text="Enter the id of the book to be returned",bg="white",font=("Microsoft Yahei Light", 14, "bold"))
            ques.place(x=30,y=10)
            iss=Frame(center,width=400,height=300,bg="white")
            iss.place(x=40,y=70)
            def on_enter(e):
                idn.delete(0, "end")
            def on_leave(e):
                name=idn.get()
                if name == "":
                    user.insert(0,"ID")
            idn = Entry(iss, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
            idn.place(x=30, y=10)
            idn.insert(0,"ID")
            idn.bind("<FocusIn>", on_enter)
            idn.bind("<FocusOut>", on_leave)
            Frame(iss, width=295, height=2, bg="black").place(x=30, y=30)
            ###########################--RETURN BOOK ISSUED--####################################
            sql="SELECT book_id from book_issued where user_id=%s"
            cur.execute(sql,[(idno)])
            res=cur.fetchall()
            if len(res)==0:
                msg=messagebox.showerror(title="No Books",message="No books to return")
            def returnb():
                sql="DELETE FROM book_issued WHERE book_id=%s and user_id=%s; "
                bid=idn.get()
                cur.execute(sql,[(bid),(idno)])
                conn.commit()
                sql="SELECT book_id from book_issued where user_id=%s"
                cur.execute(sql,[(idno)])
                res=cur.fetchall()
                if int(bid) in id_books:
                    msg=messagebox.showerror(title="Not Found",message="Book Not Issued")
                elif (int(bid),) not in res:
                    msg=messagebox.showinfo(title="Book Returned",message="Book Returned Successfully")
                else:
                    msg=messagebox.showerror(title="Book Not Returned",message="Error Occured while returning")
                if msg=="ok":
                    uwin.destroy()
                    return 5
            Button(iss, width=15, pady=5, text="Submit", bg="#57a1f8", fg="white", border=0, command=returnb,font=("Microsoft Yahei Light", 10, "bold")).place(x=100, y=90)
            
            uwin.mainloop()
            if returnb()==5:
                uwin.destroy()
        Button(ret, width=15, pady=5, text="Submit", bg="#57a1f8", fg="white", border=0, command=return_win,font=("Microsoft Yahei Light", 10, "bold")).place(x=380, y=90)

    # Frame of the GUI
    Label(adm, bg="white").place(x=50, y=50)
    frame = Frame(adm, width=1500, height=500, bg="white")
    frame.place(x=550, y=0)
    # Sign in Header
    heading = Label(frame, text="ADMINISTRATOR", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))
    heading.place(x=100, y=10)
    lab=Label(frame,text="What do you want to do ? ",fg="black", bg="white", font=("Microsoft Yahei Light", 18, "bold"))
    lab.place(x=70,y=80)
    but=Frame(adm,width=900,height=100,bg="white")
    but.place(x=325,y=150)
    Button(but, width=20, pady=7, text="Issue Book", bg="#57a1f8", fg="white", border=0, command=issue_book,font=("Microsoft Yahei Light", 15, "bold")).place(x=0, y=50)
    Button(but, width=20, pady=7, text="Return Book", bg="#57a1f8", fg="white", border=0, command=return_book,font=("Microsoft Yahei Light", 15, "bold")).place(x=300, y=50)
    Button(but, width=20, pady=7, text="Exit", bg="#57a1f8", fg="white", border=0, command=adm.destroy,font=("Microsoft Yahei Light", 15, "bold")).place(x=600, y=50)
    adm.mainloop()

##################-----USER WINDOW-----###################
def user_win():
    usern=user.get()
    root.destroy()
    us=Tk()
    title="User Details"
    us.title(title)            
    us.geometry("1500x720+10+30")
    us.configure(bg="")
    us.resizable(False,False)
    # Frame of the GUI
    Label(us, bg="white").place(x=50, y=50)
    frame = Frame(us, width=1500, height=70, bg="white")
    frame.place(x=550, y=0)
    
    # Sign in Header
    heading = Label(frame, text="User Details", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))
    heading.place(x=100, y=10)
    ###############################################################
    sql="select id,name,department,semester from users where username=%s"   
    cur.execute(sql, [(usern)])
    dets=cur.fetchall()
    #########################---DETAILS---#########################
    details=Frame(us,width=500,height=600,bg="white")
    details.place(x=30,y=60)
    name_label=Label(details,text="Welcome "+dets[0][1], bg="white", font=("Microsoft Yahei Light", 15, "bold"))
    name_label.place(x=10,y=20)
        #Enter Fields
    text = Label(details, text="FULL-NAME", fg="black", bg="white", font=("Supreme",15))
    text.place(x=10, y=170)
    text0 = Label(details,text=" "+dets[0][1], fg="black", bg="white", font=("Microsoft Yahei Light",15))
    text0.place(x=10, y=210)
    text1 = Label(details, text="ID", fg="black", bg="white", font=("Supreme",15))
    text1.place(x=10, y=250)
    text2 = Label(details,text=" "+str(dets[0][0]), fg="black", bg="white", font=("Microsoft Yahei Light",15))
    text2.place(x=10, y=290)
    text3 = Label(details, text="SEMESTER", fg="black", bg="white", font=("Supreme",15))
    text3.place(x=10, y=330)
    text4 = Label(details,text=" "+str(dets[0][3]), fg="black", bg="white", font=("Microsoft Yahei Light",15))
    text4.place(x=10, y=370)
    text5 = Label(details, text="DEPARTMENT", fg="black", bg="white", font=("Supreme",15))
    text5.place(x=10, y=410)
    text6 = Label(details,text=" "+dets[0][2], fg="black", bg="white", font=("Microsoft Yahei Light",15))
    text6.place(x=10, y=450)
    text7 = Label(details, text="NO OF BOOKS ISSUED", fg="black", bg="white", font=("Supreme",15))
    text7.place(x=10, y=490)

    im=Frame(details,height=90,width=90,bg="white")
    im.place(x=10,y=70)
    img =PhotoImage(file='D:\\CODING\\LMS\\Jupyter\\pro.png')
    imlabel=Label(im,image=img,borderwidth=0)
    imlabel.pack()

    
    #########################---AVAILABLE FRAME---##########################
    bookAvailable=Frame(us,height=600,width=400, bg="#57a1f8")
    bookAvailable.place(x=1080,y=60)
    books_label=Label(bookAvailable,text="Available Books",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 23, "bold"))
    id_label=Label(bookAvailable,text="ID",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15, "bold"))
    title_label=Label(bookAvailable,text="Title",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15, "bold"))
    id_label.place(x=50,y=80)
    title_label.place(x=190,y=80)

    books_label.place(x=100,y=20)

    books_list="select id ,title from books WHERE id not in (select b.id from books b inner join book_issued bi ON bi.book_id=b.id where bi.user_id=%s);"
    cur.execute(books_list,[(dets[0][0])])
    books_list=cur.fetchall()
    list_books=[]
    id_books=[]
    for i in books_list:
        list_books.append(i[1])
        id_books.append(i[0])    
    ycor=125
    num=1
    for i,j in zip(list_books,id_books):
        id1=Label(bookAvailable,text=j,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
        book1=Label(bookAvailable,text=i,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
        book1.place(x=190,y=ycor)
        id1.place(x=50,y=ycor)
        ycor+=50

    #########################---BOOKS FRAME---######################
    books=Frame(us,width=400,height=600,bg="#57a1f8")
    books.place(x=600,y=60)
    isb=Label(books,text="Issued Books",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 23,"bold"))
    t=Label(books,text="Title",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15,"bold"))
    idl=Label(books,text="ID",fg="white",bg="#57a1f8", font=("Microsoft Yahei Light", 15,"bold"))
    isb.place(x=100,y=20)
    t.place(x=190,y=80)
    idl.place(x=50,y=80)
    books_list="select b.id,title from books b inner join book_issued bi ON bi.book_id=b.id where bi.user_id=%s;"
    cur.execute(books_list,[(dets[0][0])])
    books_list=cur.fetchall()
    list_books=[]
    id_books=[]
    for i in books_list:
        list_books.append(i[1])
        id_books.append(i[0])  
    ycor=125
    no=0
    for i,j in zip(list_books,id_books):
        id1=Label(books,text=j,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
        book1=Label(books,text=i,fg="black",bg="#57a1f8", font=("Microsoft Yahei Light", 15))
        book1.place(x=190,y=ycor)
        id1.place(x=50,y=ycor)
        ycor+=50
        no+=1
    text8 = Label(details,text=no, fg="black", bg="white", font=("Microsoft Yahei Light",15))
    text8.place(x=15, y=530)
    us.mainloop()


##################-----SIGN UP WINDOW-----###################
def sign_up():
    #root.destroy()
    sp=Tk()
    title="Sign Up"
    sp.title(title)
    sp.geometry("450x800+500+15")
    sp.configure(bg="")
    sp.resizable(False,False)

    Label(sp, bg="white").place(x=50, y=50)

    frame = Frame(sp, width=350, height=700, bg="white")
    frame.place(x=55, y=70)


    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))
    heading.place(x=100, y=5)
##############ID####################
    def on_enter(e):
        idno.delete(0, "end")
    def on_leave(e):
        name=idno.get()
        if name == "":
            idno.insert(0,"ID")
    idno = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
    idno.place(x=30, y=80)
    idno.insert(0,"ID")
    idno.bind("<FocusIn>", on_enter)
    idno.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)
##############NAME####################
    def on_enter(e):
        fname.delete(0, "end")
    def on_leave(e):
        name=fname.get()
        if name == "":
            fname.insert(0,"Full Name")
    fname = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
    fname.place(x=30, y=150)
    fname.insert(0,"Full Name")
    fname.bind("<FocusIn>", on_enter)
    fname.bind("<FocusOut>", on_leave)    
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)
##############Department####################
    def on_enter(e):
        dep.delete(0, "end")
    def on_leave(e):
        name=dep.get()
        if name == "":
            dep.insert(0,"Department")
    dep = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft Yahei Light",11))
    dep.place(x=30, y=220)
    dep.insert(0,"Department")
    dep.bind("<FocusIn>", on_enter)
    dep.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)
##############Semester####################    
    def on_enter(e):
        sem.delete(0, "end")
    def on_leave(e):
        name=sem.get()
        if name == "":
            sem.insert(0,"Semester")
    sem = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft Yahei Light",11))
    sem.place(x=30, y=290)
    sem.insert(0,"Semester")
    sem.bind("<FocusIn>", on_enter)
    sem.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=317)  
    login_label=Label(frame, text="Login Credentials", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 18, "bold"))
    login_label.place(x=65, y=350)
##############USERNAME#############    
    def on_enter(e):
        user.delete(0, "end")
    def on_leave(e):
        name=user.get()
        if name == "":
            user.insert(0,"Username")
    user = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft Yahei Light",11))
    user.place(x=30, y=423)
    user.insert(0,"Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=450)
##############PASSWORD####################
    def on_enter(e):
        code.delete(0, "end")
    def on_leave(e):
        name=code.get()
        if name == "":
            code.insert(0,"Password")
    code = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft Yahei Light",11))
    code.place(x=30, y=493)
    code.insert(0,"Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=520)
##############PASSWORD reenter####################
    def on_enter(e):
        code2.delete(0, "end")
    def on_leave(e):
        name=code2.get()
        if name == "":
            code2.insert(0,"Re-enter password")
    code2 = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft Yahei Light",11))
    code2.place(x=30, y=563)
    code2.insert(0,"Re-enter password")
    code2.bind("<FocusIn>", on_enter)
    code2.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=590)
    def check():
        idn=idno.get()
        n=fname.get()
        d=dep.get()
        s=sem.get()
        u=user.get()
        c=code.get()
        c2=code2.get()
        def register():
            sql="INSERT INTO users(Id,Name,Department,Semester,username,password) VALUES (%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,(idn,n,d,s,u,c))
            entry="Select id from users "
            cur.execute(entry)
            ids = cur.fetchall()
            conn.commit()
            if (int(idn),) in ids:
                msg_box=messagebox.showinfo(title="Sign Up Successfull",message="You have successfully signed up.")
                if msg_box=='ok':
                    sp.destroy()
                    root.mainloop()
        sql="select username from users"
        cur.execute(sql)
        usernames = cur.fetchall()
        sql="select id from users"
        cur.execute(sql)
        ids = cur.fetchall()  
        if c!="Password" and idn!="ID" and d!="Department"and s!="Semester" and u!="Username" and fname!="Full Name":
            if c!=c2:
                messagebox.showerror(title="Password error",message="Please check password.")
            elif ("u",) in usernames or (int(idn),) in ids:
                messagebox.showerror(title="Already Exists",message="User already exixts")
            else:
                register()
                
        else:
            messagebox.showerror(title="Sign Up Failed !!",message="Please check your fields.")
    Button(frame, width=39, pady=7, text="Submit", bg="#57a1f8", fg="white", border=0,command=check).place(x=35, y=617)
    sp.mainloop()


##################-----MAIN-----###################
from tkinter import* 
from tkinter import messagebox
import mysql.connector

conn=mysql.connector.connect(host='localhost',password='pass',user='root',database='library')
cur=conn.cursor()
root=Tk()
title="Login"
root.title(title)
root.geometry("450x500+500+200")
root.configure(bg="")
root.resizable(False,False)

# Frame of the GUI
# img = PhotoImage(file="login.png")
Label(root, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=55, y=70)

# Sign in Header
heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))
heading.place(x=100, y=5)

# User entry box

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0,"Username")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei Light",11))
user.place(x=30, y=80)
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Password entry box
def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name=code.get()
    if name == "":
        code.insert(0,"Password")


code = Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft Yahei Light",11))
code.place(x=30, y=150)
code.insert(0,"Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)


Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Sign in Button 
def sign_in():
    username=user.get()
    password=code.get()
    sql = "select * from users where username = %s and password = %s"
    cur.execute(sql, [(username), (password)])
    results = cur.fetchall()
    if username=='admin'and password=='admin':
        msg_box=messagebox.showinfo(title="Login Successfull !!",message="Welcome admin")
        if msg_box=='ok':
            admin()
    elif results:
        msg_box=messagebox.showinfo(title="Login Successfull !!",message="You have successfully logged in.")
        if msg_box=='ok':
            user_win()
    else:
        messagebox.showerror(title="Login Failed !!",message="Please check your credentials.")
Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=sign_in).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft Yahei Light",9))
label.place(x=75, y=270)

# Sign up Button
sign = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8",command=sign_up)
sign.place(x=215, y=270)

root.mainloop()