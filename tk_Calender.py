from tkinter import *
from tkcalendar import Calendar
# Create Tkinter window
well = Tk()
#Create Title name
well.title("Calendar")

#the Background colour
well.configure(background="grey")
# Set the geometry of tkinter window
well.geometry("600x500")
# Add Calendar widget
cal = Calendar(well, selectmode='day',
                        date_pattern='dd-mm-yyyy', 
                        background = "green",
                        foreground = "white",
                        selectbackground = "red", 
                        normalbackground = "lightgreen",
                        weekendbackground = "darkgreen",
                        weekendforeground = "white")
cal.pack(pady = 50)
#Function works when click on select button
def gt_date():
    date.config(background="magenta", text = "Selected Date : " + cal.get_date())
# Add Button
Button(well, background= "yellow", text = "Select the Date and Click on the get Date",
    command = gt_date).pack(pady = 10)
#Add Label for Showing Date on window screen
date = Label(well, text = "")
date.pack(pady = 25)
# Execute Tkinter
well.mainloop()

