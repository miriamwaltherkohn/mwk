print "Hello LUV!"

potential_content = raw_input("Name one of your urgencies?")
potential_collegues = raw_input("Who shares this urgency with you?")
potential_methode = raw_input("How do you want to approach this shared urgency?")

if len(potential_content) > 0 and potential_content.isalpha():
    if len(potential_collegues) > 0 and potential_collegues.isalpha():
        if len(potential_methode) > 0 and potential_methode.isalpha():
            print "Imagine yourself far away on top of a hill inside and around a castle with %s, envisioning the future of %s, while %s." % (potential_collegues,potential_content,potential_methode)
#It may sound creepy, but trust me it's not. ;-)
else:
    print "Try again"    

number_of_recurring_folks = raw_input("How many people you already know participate in luv17?")
number_of_recurring_folks = int(number_of_recurring_folks)
number_of_shared_urgencies = raw_input("How many common topics do you excpect at luv17?")
number_of_shared_urgencies = int(number_of_shared_urgencies)

def luv_approach(f,u):
    # f = number of recurring folks
    # u = number of shared urgencies
    if f >= 20 and u == 1:
        return "Tackle the shared urgency and explore it from diffrent angles for the five following days!"
    elif f < 20 or u >= 2:
        return "Getting to know the intriguing strangers and being inspired by urgencies and point of views that lay outside one's own filter-bubble..."
    else:
        return "The werewolves are watching you!"

print luv_approach(number_of_recurring_folks, number_of_shared_urgencies) #add your arguments here!
