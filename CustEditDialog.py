#TODO:  Find out why the import names must be unique
import tkinter as CRTK
#from tkinter import messagebox
from CustDBFunctions import *
from CarsDBFunctions import *
from ResDBFunctions import *

cstDB = CustDBFunctions()
carDB = CarsDBFunctions()
resDB = ResDBFunctions()

class CustEditDialog(object):
    root = None

    def __init__(self, parent):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        #self.tki = CRTK.Tk()
        self.top = CRTK.Toplevel(CustEditDialog.root)
        #self.CarRentedEvent = CRTK.Event
        self.frm = CRTK.Frame(self.top, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.custID = parent.custID
        output = cstD.loadCustomerByID()
        for dat in output:
            id = '{}'.format(dat[0])
            name = '{} {}'.format(dat[0], dat[1], dat[2], dat[3])
            FName= '{}'.format(dat[1])
            LName= '{}'.format(dat[2])
            num = '{}'.format(dat[3])



        self.label = CRTK.Label(self.frm, text="Editing: {}".format(name))
        self.label.pack(padx=4, pady=4)

        self.lblFName = CRTK.Label(self.frm, text='First Name')
        self.lblFName.pack(padx=4, pady=4)
        self.entryFName = CRTK.Entry(self.frm)
        self.entryFName.pack(pady=4, padx=4)
        self.entryStart.insert(0, self.FName)
        #self.entryStart.bind('<Enter>', self.ResetStartDate)
        #self.entryStart.bind('<FocusOut>', self.ValidateStartDate)

        self.lblLName = CRTK.Label(self.frm, text = 'Last Name')
        self.lblLName.pack(padx=4, pady=4)
        self.entryLName = CRTK.Entry(self.frm)
        self.entryLName.pack(pady=4, padx=4)
        self.entryLName.insert(0, self.Lname)

        self.lblNum = CRTK.Label(self.frm, text = 'Phone Number')
        self.lblNum.pack(padx=4, pady=4)
        self.entryNum = CRTK.Entry(self.frm)
        self.entryNum.pack(pady=4, padx=4)
        self.entryNum.insert(0, self.num)

        self.b_cancel = CRTK.Button(self.frm, text='Cancel')
        self.b_cancel['command'] = self.top.destroy
        self.b_cancel.pack(padx=4, pady=4)    

        self.b_OK = CRTK.Button(self.frm, text='OK')
        #self.b_OK['command'] = self.updateCust
        #self.b_OK['command'] = self.top.destroy
        self.b_OK.pack(padx=4, pady=4) 

    def updateCust(self):
        print("Updating the Name into the databse....")
        

        



