#Created by: Younes Elfitori
#Created on: Oct 2017
#Created for ICS3U
#This program shows the leap 

import ui

def leap_year_touch_up_inside(sender):
    leapyear = int(view['year_textfield'].text)
    
    if (leapyear % 4) == 0:
      if (leapyear % 100) == 0:
        if (leapyear % 400) == 0:
          view['answer_label'].text = 'It is a leap year.'
        else:
          view['answer_label'].text = 'It is not a leap year.'
      else:
        view['answer_label'].text = 'It is a leap year.'
    else:
      view['answer_label'].text = 'It is not a leap year.'

view = ui.load_view()
view.present('sheet')
