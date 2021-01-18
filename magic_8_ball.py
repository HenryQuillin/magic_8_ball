"""

This is Henry's magic eight ball code.

I tried, but I could not find a way to 
allow spaces in the input field.

You have to press "concentrate" to 
get the Magic eight ball to give an
answer, but only after you have inputed your question. 


"""
import simplegui
import random
a = ""
b = ""
question = ""


def number_to_fortune(number):
    if number == 0:
        return ("Definitly not")
    elif number == 1:
        return ("I sense no") 
    elif number == 2: 
        return ("Don't count on it")
    elif number == 3: 
        return ("ask again")
    elif number == 4: 
        return ("Can't predict now")
    elif number == 5:
        return ("As I see it, yes")
    elif number == 6:
        return ("Most Likely")
    elif number == 7: 
        return ("Yes definitely")
    else: 
        return ("Something is wrong:(") 


    
    
def ball():
    global question
    global number
    print ("Your question is " + (str(question)))
    print ("You shake the Magic 8-Ball, concentrate hard!")
    print ("The magic eight ball says", str(number_to_fortune(number)))
    
def input_q(q):
    global question 
    global a
    question = str(q) 
    a = "You shake the Magic 8-Ball"
 
    
def concentrate():
    global b 
    global a
    b = "The magic eight ball says: " + str(number_to_fortune(random.randrange(0,8)))
    a = ""
    
   
    
def reset():
    global a 
    global b 
    global question
    a = ""
    b = ""
    question = ""

 

def draw(canvas):
    global a 
    canvas.draw_polygon([(50, 120), (300, 440), (550, 120)], 12, 'Teal', "Aqua")
    canvas.draw_text("Your question is " + str(question), (150, 150), 15, "Blue", "monospace")
    canvas.draw_text(str(a), (190, 185), 15, "Navy", "monospace")
    canvas.draw_text(str(b), (130, 185), 15, "Purple", "monospace")
    canvas.draw_circle((300, 30), 70, 5, 'White', 'White')
    canvas.draw_text("8", (283, 50), 74, "Black")
  


    


frame = simplegui.create_frame("Magic Eight Ball", 600, 500)

frame.add_input("What is your question", input_q, 100)

frame.add_button("concentrate!", concentrate, 100) 

frame.add_button("reset", reset, 100)

frame.set_draw_handler(draw)




frame.start()


