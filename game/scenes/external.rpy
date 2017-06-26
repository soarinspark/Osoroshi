label elsewhere:

    show frank neutral:
        align (0.52, 1.0)
    c_frank "I went elsewhere!"
    c_frank "As in, this scene is found in another file."
    c_frank "It's called external.rpy and it's in the \"scenes\" folder!"
    hide frank
    
    show frank neutral:
        align (0.85, 1.0)
    show mike neutral:
        align (0.5, 1.0)
    with move
    c_mike "I exist now!"
    show joey neutral:
        align (0.5, 1.0)
    with moveinleft
    with vpunch
    c_joey "Im the best boy obviously"
    hide joey
    with moveoutright
    show shaun neutral:
        align (0.25, 1.0)
    show frank neutral:
        align (0.95, 1.0)
    show mike neutral:
        align (0.6, 1.0)
    with move
    c_shaun "Me too!"
    
    hide shaun
    hide mike
    hide frank
    with moveoutright
    show tim neutral:
        align (0.5, 1.0)
    with moveinleft
    c_tim "What did I miss?"
    c_tim "Guys?"
    c_tim "Hey wait up!"
    hide tim
    with moveoutright
    
    show meiko angry:
        align (0.35, 1.0)
        
    c_meiko "GUYS."
    c_meiko "STOP FUCKING AROUND AND FINISH MAKING A GAME ABOUT ME."
    
    jump begone