import tkinter as tk
import mysql.connector as sql
import datetime

'''This class is the Repair Console Window'''
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Repair Console')
        self.get_db()
        self.create_widgets()

    def get_db(self):
        #These are the parameters for the database you wish to connect to.
        self.host = 'hostname'
        self.user = 'username'
        self.password = 'password'
        self.database = 'database name'

    #Calls the functions for the window widgets
    def create_widgets(self):
        self.add_repair_widgets(0,0)
        self.add_repair_table(1,2)
        self.add_overdue_table(13,2)
        self.add_modify(13,0)

    #Creates the Modify RA table
    def add_modify(self,y,x):
        self.mod = tk.StringVar(self)
        self.mod.set('Modify Comment')

        self.modmenu = tk.OptionMenu(self,self.mod,'Modify Comment','Modify First Name','Modify Last Name','Modify Model','Modify Manufacturer','Modify Status','Modify Type','Delete Entry')
        self.modenter = tk.Entry(self)
        self.modenternew = tk.Entry(self)
        self.modbutton = tk.Button(self,text = 'Modify',command = self.modify,bg = 'orange')
        self.modenter.insert(0,'Enter RA Number')
        self.modenternew.insert(0,'Enter New Data')

        self.modmenu.grid(row = y + 1,column = x,columnspan = 2)
        self.modenter.grid(row = y + 2,column = x,columnspan = 2)
        self.modenternew.grid(row = y + 3,column = x,columnspan = 2)
        self.modbutton.grid(row = y + 4,column = x, columnspan = 2)

    #Creates the Overdue RA's table
    def add_overdue_table(self,y,x):
        self.ra2text = tk.Text(self,height = 12, width = 8,wrap = tk.NONE)
        self.fn2text = tk.Text(self,height = 12, width = 16,wrap = tk.NONE)
        self.ln2text = tk.Text(self,height = 12, width = 16,wrap = tk.NONE)
        self.et2text = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.md2text = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.mn2text = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.st2text = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.cm2text = tk.Text(self,height = 12, width = 32,wrap = tk.NONE)
        self.dt2text = tk.Text(self,height = 12, width = 10,wrap = tk.NONE)
        
        self.refresh2 = tk.Button(self,text = 'Refresh', bg = 'limegreen',command = self.get_overdue)

        scrol2 = tk.Scrollbar(self)
        self.ra2text.config(yscrollcommand=scrol2.set)
        self.fn2text.config(yscrollcommand=scrol2.set)
        self.ln2text.config(yscrollcommand=scrol2.set)
        self.et2text.config(yscrollcommand=scrol2.set)
        self.md2text.config(yscrollcommand=scrol2.set)
        self.mn2text.config(yscrollcommand=scrol2.set)
        self.st2text.config(yscrollcommand=scrol2.set)
        self.cm2text.config(yscrollcommand=scrol2.set)
        self.dt2text.config(yscrollcommand=scrol2.set)
        scrol2.config(command=self.yview2)

        self.get_overdue()

        tk.Label(self,text = 'Overdue Repairs', font = ('Courier 12')).grid(row = y,column = x + 7,columnspan = 2)

        self.refresh2.grid(column = x+1,row = y, pady = 4)
        self.ra2text.grid(row = y + 1,column = x + 1,rowspan = 9,sticky = tk.N+tk.S)
        self.fn2text.grid(row = y + 1,column = x + 2,rowspan = 9,sticky = tk.N+tk.S)
        self.ln2text.grid(row = y + 1,column = x + 3,rowspan = 9,sticky = tk.N+tk.S)
        self.et2text.grid(row = y + 1,column = x + 4,rowspan = 9,sticky = tk.N+tk.S)
        self.md2text.grid(row = y + 1,column = x + 5,rowspan = 9,sticky = tk.N+tk.S)
        self.mn2text.grid(row = y + 1,column = x + 6,rowspan = 9,sticky = tk.N+tk.S)
        self.st2text.grid(row = y + 1,column = x + 7,rowspan = 9,sticky = tk.N+tk.S)
        self.dt2text.grid(row = y + 1,column = x + 8,rowspan = 9,sticky = tk.N+tk.S)
        self.cm2text.grid(row = y + 1,column = x + 9,rowspan = 9,sticky = tk.E+tk.W+tk.N+tk.S)
        scrol2.grid(row = y,column = x,rowspan = 9,sticky=tk.N+tk.S+tk.W)
        self.grid_rowconfigure(x + 1,weight = 1)
        self.grid_rowconfigure(x + 2,weight = 1)
        self.grid_rowconfigure(x + 3,weight = 1)
        self.grid_rowconfigure(x + 4,weight = 1)
        self.grid_rowconfigure(x + 5,weight = 1)
        self.grid_rowconfigure(x + 6,weight = 1)
        self.grid_rowconfigure(x + 7,weight = 1)
        self.grid_rowconfigure(x + 8,weight = 1)
        self.grid_rowconfigure(x + 9,weight = 1)

    #Creates the Repairs table
    def add_repair_table(self,y,x):
        self.search = tk.StringVar(self)
        self.search.set('Search by RA')

        self.searchmenu = tk.OptionMenu(self,self.search,'Search by RA','Search by Last Name','Search By Model','Search by Manufacturer', 'Search by Status')
        self.searchenter = tk.Entry(self)
        self.searchbutton = tk.Button(self,text = 'Search',command = self.searching)
        self.refresh = tk.Button(self,text = 'Refresh', bg = 'limegreen',command = self.get_repairs)

        self.ratext = tk.Text(self,height = 12, width = 8,wrap = tk.NONE)
        self.fntext = tk.Text(self,height = 12, width = 16,wrap = tk.NONE)
        self.lntext = tk.Text(self,height = 12, width = 16,wrap = tk.NONE)
        self.ettext = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.mdtext = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.mntext = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.sttext = tk.Text(self,height = 12, width = 12,wrap = tk.NONE)
        self.cmtext = tk.Text(self,height = 12, width = 32,wrap = tk.NONE)
        self.dttext = tk.Text(self,height = 12, width = 10,wrap = tk.NONE)
        
        scrol = tk.Scrollbar(self)
        hscrol = tk.Scrollbar(self,orient = 'horizontal')
        self.ratext.config(yscrollcommand=scrol.set)
        self.fntext.config(yscrollcommand=scrol.set)
        self.lntext.config(yscrollcommand=scrol.set)
        self.ettext.config(yscrollcommand=scrol.set)
        self.mdtext.config(yscrollcommand=scrol.set)
        self.mntext.config(yscrollcommand=scrol.set)
        self.sttext.config(yscrollcommand=scrol.set)
        self.cmtext.config(yscrollcommand=scrol.set,xscrollcommand=hscrol.set)
        self.dttext.config(yscrollcommand=scrol.set)
        scrol.config(command=self.yview)
        hscrol.config(command=self.cmtext.xview)

        self.get_repairs()

        self.searchmenu.grid(row = y,column = x + 2)
        self.searchenter.grid(row = y,column = x + 3)
        self.searchbutton.grid(row = y,column = x + 4)
        self.refresh.grid(column = x + 1,row = y, pady = 4)

        tk.Label(self,text = 'RA Number:'     ).grid(row = y + 1,column = x + 1)
        tk.Label(self,text = 'First Name:'    ).grid(row = y + 1,column = x + 2)
        tk.Label(self,text = 'Last Name:'     ).grid(row = y + 1,column = x + 3)
        tk.Label(self,text = 'Equipment Type:').grid(row = y + 1,column = x + 4)
        tk.Label(self,text = 'Model:'         ).grid(row = y + 1,column = x + 5)
        tk.Label(self,text = 'Manufacturer:'  ).grid(row = y + 1,column = x + 6)
        tk.Label(self,text = 'Status:'        ).grid(row = y + 1,column = x + 7)
        tk.Label(self,text = 'Date:'          ).grid(row = y + 1,column = x + 8)
        tk.Label(self,text = 'Comments:'      ).grid(row = y + 1,column = x + 9)
        tk.Label(self,text = 'Repairs'        , font = ('Courier 12')).grid(column = x + 7,row = y,columnspan = 2)

        self.ratext.grid(row = y + 2,column = x + 1,rowspan = 9,sticky = tk.N+tk.S)
        self.fntext.grid(row = y + 2,column = x + 2,rowspan = 9,sticky = tk.N+tk.S)
        self.lntext.grid(row = y + 2,column = x + 3,rowspan = 9,sticky = tk.N+tk.S)
        self.ettext.grid(row = y + 2,column = x + 4,rowspan = 9,sticky = tk.N+tk.S)
        self.mdtext.grid(row = y + 2,column = x + 5,rowspan = 9,sticky = tk.N+tk.S)
        self.mntext.grid(row = y + 2,column = x + 6,rowspan = 9,sticky = tk.N+tk.S)
        self.sttext.grid(row = y + 2,column = x + 7,rowspan = 9,sticky = tk.N+tk.S)
        self.dttext.grid(row = y + 2,column = x + 8,rowspan = 9,sticky = tk.N+tk.S)
        self.cmtext.grid(row = y + 2,column = x + 9,rowspan = 9,sticky = tk.E+tk.W+tk.N+tk.S)
        scrol.grid(row = y + 2,column = x,rowspan = 9,sticky=tk.N+tk.S+tk.W)
        hscrol.grid(row = y + 11,column = x + 9,sticky = tk.N+tk.W+tk.E)
        self.grid_columnconfigure(x + 9,weight = 1)
        self.grid_rowconfigure(x + 1,weight = 1)
        self.grid_rowconfigure(x + 2,weight = 1)
        self.grid_rowconfigure(x + 3,weight = 1)
        self.grid_rowconfigure(x + 4,weight = 1)
        self.grid_rowconfigure(x + 5,weight = 1)
        self.grid_rowconfigure(x + 6,weight = 1)
        self.grid_rowconfigure(x + 7,weight = 1)
        self.grid_rowconfigure(x + 8,weight = 1)
        self.grid_rowconfigure(x + 9,weight = 1)

    #Creates the add RA table
    def add_repair_widgets(self,y,x):
        self.etvar = tk.StringVar(self)
        self.stvar = tk.StringVar(self)
        self.etvar.set('Turntable')
        self.stvar.set('Recieved')
        self.eRA = tk.Entry(self)
        self.eFN = tk.Entry(self)
        self.eLN = tk.Entry(self)
        self.eET = tk.OptionMenu(self,self.etvar,'Cassette Player','Cartridge','Turntable','Compact System','CD Player','Amplifier','Reel to Reel', 'Reciever','Amplified Speaker','Tuner','Preamp','Voltage Conversion','Other')
        self.eMd = tk.Entry(self)
        self.eMn = tk.Entry(self)
        self.eSt = tk.OptionMenu(self,self.stvar,'Recieved','Inspected','In Progress','Finished','Shipped')
        self.eCm = tk.Entry(self)
        self.eDt = tk.Entry(self)
        self.eDt.insert(0,'YYYY-MM-DD')
        
        self.enter = tk.Button(self,text = 'Enter Repair to Database',bg = 'steelblue',command = self.send_entries)

        tk.Label(self,text = 'RA Number:'     ).grid(column = y,row = x + 2)
        tk.Label(self,text = 'First Name:'    ).grid(column = y,row = x + 3)
        tk.Label(self,text = 'Last Name:'     ).grid(column = y,row = x + 4)
        tk.Label(self,text = 'Equipment Type:').grid(column = y,row = x + 5)
        tk.Label(self,text = 'Model:'         ).grid(column = y,row = x + 6)
        tk.Label(self,text = 'Manufacturer:'  ).grid(column = y,row = x + 7)
        tk.Label(self,text = 'Status:'        ).grid(column = y,row = x + 8)
        tk.Label(self,text = 'Comments:'      ).grid(column = y,row = x + 9)
        tk.Label(self,text = 'Date:'          ).grid(column = y,row = x + 10)


        self.eRA.grid(column = y + 1, row = x + 2)
        self.eFN.grid(column = y + 1, row = x + 3)
        self.eLN.grid(column = y + 1, row = x + 4)
        self.eET.grid(column = y + 1, row = x + 5)
        self.eMd.grid(column = y + 1, row = x + 6)
        self.eMn.grid(column = y + 1, row = x + 7)
        self.eSt.grid(column = y + 1, row = x + 8)
        self.eCm.grid(column = y + 1, row = x + 9)
        self.eDt.grid(column = y + 1, row = x + 10)

        self.enter.grid(column = y, row = x + 11,pady = 4,columnspan = 2)

    #This binds together several references to textboxes so that a single scrollbar can control them.
    def yview(self,*args):
        self.ratext.yview(*args)
        self.fntext.yview(*args)
        self.lntext.yview(*args)
        self.ettext.yview(*args)
        self.mdtext.yview(*args)
        self.mntext.yview(*args)
        self.sttext.yview(*args)
        self.cmtext.yview(*args)
        self.dttext.yview(*args)

    #Ditto
    def yview2(self,*args):
        self.ra2text.yview(*args)
        self.fn2text.yview(*args)
        self.ln2text.yview(*args)
        self.et2text.yview(*args)
        self.md2text.yview(*args)
        self.mn2text.yview(*args)
        self.st2text.yview(*args)
        self.cm2text.yview(*args)
        self.dt2text.yview(*args)
    
    #Formats the entered text into a SQL query
    def send_entries(self):
        entry = ['1','This','Is','A','Test','of','Repair','Logger','01/01/0001']
        entry[0] = self.eRA.get()
        entry[1] = self.eFN.get()
        entry[2] = self.eLN.get()
        entry[3] = self.etvar.get()
        entry[4] = self.eMd.get()
        entry[5] = self.eMn.get()
        entry[6] = self.stvar.get()
        entry[7] = self.eCm.get()
        entry[8] = self.eDt.get()
        query = 'INSERT INTO repairs (repairnumber,firstname,lastname,typeof,model,manufacturer,statusof,comments,dateof) VALUES ('
        query = query +entry[0]+',\''+entry[1]+'\''+',\''+entry[2]+'\''+',\''+entry[3]+'\''+',\''+entry[4]+'\''+',\''+entry[5]+'\''+',\''+entry[6]+'\''+',\''+entry[7]+'\''+',\''+entry[8]+'\''+');'
       
        db =  sql.connect(
            host = self.host,
            user = self.user,
            passwd = self.password,
            database = self.database)
        curs = db.cursor(buffered = True)
        curs.execute(query)
        db.commit()
        db.close()
        
        self.get_repairs()

    #Retrieves the repairs from the database
    def get_repairs(self):
        self.ratext.delete(1.0,tk.END)
        self.fntext.delete(1.0,tk.END)
        self.lntext.delete(1.0,tk.END)
        self.ettext.delete(1.0,tk.END)
        self.mdtext.delete(1.0,tk.END)
        self.mntext.delete(1.0,tk.END)
        self.sttext.delete(1.0,tk.END)
        self.cmtext.delete(1.0,tk.END)
        self.dttext.delete(1.0,tk.END)
        db =  sql.connect(
            host = self.host,
            user = self.user,
            passwd = self.password,
            database = self.database)
        curs = db.cursor(buffered = True)
        curs.execute('SELECT repairnumber,firstname,lastname,typeof,model,manufacturer,statusof,comments,dateof FROM repairs')
        row = curs.fetchone()
        while row is not None:
            self.ratext.insert(tk.END,row[0])
            self.fntext.insert(tk.END,row[1])
            self.lntext.insert(tk.END,row[2])
            self.ettext.insert(tk.END,row[3])
            self.mdtext.insert(tk.END,row[4])
            self.mntext.insert(tk.END,row[5])
            self.sttext.insert(tk.END,row[6])
            self.cmtext.insert(tk.END,row[7])
            self.dttext.insert(tk.END,row[8])
            self.ratext.insert(tk.END,'\n')
            self.fntext.insert(tk.END,'\n')
            self.lntext.insert(tk.END,'\n')
            self.ettext.insert(tk.END,'\n')
            self.mdtext.insert(tk.END,'\n')
            self.mntext.insert(tk.END,'\n')
            self.sttext.insert(tk.END,'\n')
            self.cmtext.insert(tk.END,'\n')
            self.dttext.insert(tk.END,'\n')
            row = curs.fetchone()
        db.close()
            
    def get_overdue(self):
        self.ra2text.delete(1.0,tk.END)
        self.fn2text.delete(1.0,tk.END)
        self.ln2text.delete(1.0,tk.END)
        self.et2text.delete(1.0,tk.END)
        self.md2text.delete(1.0,tk.END)
        self.mn2text.delete(1.0,tk.END)
        self.st2text.delete(1.0,tk.END)
        self.cm2text.delete(1.0,tk.END)
        self.dt2text.delete(1.0,tk.END)
        db =  sql.connect(
            host = self.host,
            user = self.user,
            passwd = self.password,
            database = self.database)
        curs = db.cursor(buffered = True)
        curs.execute('SELECT repairnumber,firstname,lastname,typeof,model,manufacturer,statusof,comments,dateof FROM repairs WHERE DATE_SUB(CURDATE(),INTERVAL 50 DAY) >= dateof')
        row = curs.fetchone()
        while row is not None:
            self.ra2text.insert(tk.END,row[0])
            self.fn2text.insert(tk.END,row[1])
            self.ln2text.insert(tk.END,row[2])
            self.et2text.insert(tk.END,row[3])
            self.md2text.insert(tk.END,row[4])
            self.mn2text.insert(tk.END,row[5])
            self.st2text.insert(tk.END,row[6])
            self.cm2text.insert(tk.END,row[7])
            self.dt2text.insert(tk.END,row[8])
            self.ra2text.insert(tk.END,'\n')
            self.fn2text.insert(tk.END,'\n')
            self.ln2text.insert(tk.END,'\n')
            self.et2text.insert(tk.END,'\n')
            self.md2text.insert(tk.END,'\n')
            self.mn2text.insert(tk.END,'\n')
            self.st2text.insert(tk.END,'\n')
            self.cm2text.insert(tk.END,'\n')
            self.dt2text.insert(tk.END,'\n')
            row = curs.fetchone()
        db.close()
              
    def searching(self):
        self.ratext.delete(1.0,tk.END)
        self.fntext.delete(1.0,tk.END)
        self.lntext.delete(1.0,tk.END)
        self.ettext.delete(1.0,tk.END)
        self.mdtext.delete(1.0,tk.END)
        self.mntext.delete(1.0,tk.END)
        self.sttext.delete(1.0,tk.END)
        self.cmtext.delete(1.0,tk.END)
        self.dttext.delete(1.0,tk.END)
        query = 'SELECT repairnumber,firstname,lastname,typeof,model,manufacturer,statusof,comments,dateof FROM repairs WHERE '
        sdict = {'Search by RA':'repairnumber = '+ self.searchenter.get(),
                 'Search by Last Name':'lastname = '+'\''+ self.searchenter.get()+'\'',
                 'Search By Model':'model = '+ '\''+self.searchenter.get()+'\'',
                 'Search by Manufacturer':'manufacturer = '+'\''+ self.searchenter.get()+'\'',
                 'Search by Status':'statusof = '+'\''+ self.searchenter.get()+'\''}

        db =  sql.connect(
            host = self.host,
            user = self.user,
            passwd = self.password,
            database = self.database)
        curs = db.cursor(buffered = True)
        curs.execute(query + sdict[self.search.get()])
        row = curs.fetchone()
        while row is not None:
            self.ratext.insert(tk.END,row[0])
            self.fntext.insert(tk.END,row[1])
            self.lntext.insert(tk.END,row[2])
            self.ettext.insert(tk.END,row[3])
            self.mdtext.insert(tk.END,row[4])
            self.mntext.insert(tk.END,row[5])
            self.sttext.insert(tk.END,row[6])
            self.cmtext.insert(tk.END,row[7])
            self.dttext.insert(tk.END,row[8])
            self.ratext.insert(tk.END,'\n')
            self.fntext.insert(tk.END,'\n')
            self.lntext.insert(tk.END,'\n')
            self.ettext.insert(tk.END,'\n')
            self.mdtext.insert(tk.END,'\n')
            self.mntext.insert(tk.END,'\n')
            self.sttext.insert(tk.END,'\n')
            self.cmtext.insert(tk.END,'\n')
            self.dttext.insert(tk.END,'\n')
            row = curs.fetchone()
        db.close()
            
    def modify(self):
        ra = self.modenter.get()
        mdict = {'Modify Comment':'comments',
                 'Modify Last Name':'lastname',
                 'Modify First Name':'firstname',
                 'Modify Model':'model',
                 'Modify Manufacturer':'manufacturer',
                 'Modify Status':'statusof',
                 'Modify Type':'typeof'}
        if self.mod.get() == 'Delete Entry':
            query = 'DELETE FROM repairs WHERE repairnumber = '+self.modenter.get()
        else:
            query = 'UPDATE repairs SET '+mdict[self.mod.get()]+' = '+'\''+ self.modenternew.get()+'\''+' WHERE repairnumber = ' + ra +';'

        db =  sql.connect(
            host = self.host,
            user = self.user,
            passwd = self.password,
            database = self.database)
        curs = db.cursor()
        curs.execute(query)
        db.commit()
        self.get_repairs()
        db.close()

def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()         
