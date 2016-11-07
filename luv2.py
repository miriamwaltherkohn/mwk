    print "Hello LUV!"

potential_content = raw_input("Name one of your urgencies?")
potential_collegues = raw_input("Who shares this urgency with you?")
poetential_methode = raw_input("How do you want to approach this shared urgency?")

    print "Imagine yourself far away on top of a hill inside and around a castle with %s, envisioning the future of %s, while %s." % (potential_collegues,potential_content,poetential_methode)
#It may sound creepy, but trust me it's not. ;-)

def luv_approach(f,u)
    # f = number of recurring folks
    # u = number of shared urgencies
    if f >= 20 and u == 1:
        return "Tackle the shared urgency and explore it from diffrent angles for the five following days!"
    elif f < 20 or u >= 2:
        return "Getting to know the intriguing strangers and being inspired by urgencies and point of views that lay outside one's own filter-bubble..."
    else:
        return "The werewolves are watching you!"

luv_approach() #add your arguments here!
