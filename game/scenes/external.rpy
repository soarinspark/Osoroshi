init:
    image testbackground = "my name jeff.jpg"

label elsewhere:
    
    scene testbackground

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
    
    c_mike "So who do you think is the best boy?"
    
    menu:
        "Frank":
            jump frank
            
        "Joey":
            jump joey
            
        "Mike":
            jump mike
            
        "Shaun":
            jump shaun
            
        "Tim":
            jump tim
            
        "Dominick":
            jump dom
            
        "Dan":
            jump dan
        
        "Damien":
            jump damien
        
        "Dr. McNamara":
            jump bigmac
        
    label frank:
        
        hide mike
        hide shaun
        with moveoutright
        show frank neutral:
            align (0.5, 1.0)
        c_frank "Hey thanks!"
        jump afterchoice
    
    label joey:
        hide mike
        hide shaun
        hide frank
        with moveoutright
        show joey neutral:
            align (0.5, 1.0)
        with moveinright
        
        c_joey "You heard it here folks, I'm the best boy!"
        
        jump afterchoice
            
    label mike:
        hide shaun
        hide frank
        with moveoutright
        show mike neutral:
            align (0.5, 1.0)
        with moveinright
        
        c_mike "I don't usually appreciate being lied to, but it was a nice gesture."
        
        jump afterchoice

    label shaun:
        hide frank
        hide mike
        with moveoutright
        show shaun neutral:
            align (0.5, 1.0)
        with moveinright
        c_shaun "No, you're the best boy ;)"
        jump afterchoice
            
    label tim:
        hide frank
        hide mike
        hide shaun
        with moveoutright
        show tim neutral:
            align (0.5, 1.0)
        with moveinright
        c_tim "Joey is bad at organizing code"
        jump afterchoice
    
    label dom:
        hide frank
        hide mike
        hide shaun
        with moveoutright
        show dom neutral:
            align (0.5, 1.0)
        with moveinleft
        c_dom "I mean, yeah. Obviously."
        jump afterchoice

    label dan:
        hide frank
        hide mike
        hide shaun
        with moveoutright
        show dan neutral:
            align (0.5, 1.0)
        with moveinleft
        c_dan "It's because I'm so sexy, right?"
        jump afterchoice
        
    label damien:
        hide frank
        hide mike
        hide shaun
        with moveoutright
        show damien neutral:
            align (0.5, 1.0)
        with moveinleft
        c_damien "You have great taste, fuckin faggot"
        jump afterchoice
        
    label bigmac:
        hide frank
        hide mike
        hide shaun
        with moveoutright
        show joey neutral:
            align (0.5, 1.0)
        with moveinleft
        c_joey "I'm sorry, what did you just say?"
        menu:
            "I said McNamara, bitch":
                jump badchoice
            
            "I didn't say anything.":
                jump repentance
                
    label badchoice:
        show joey angry:
            align (0.5, 1.0)
        c_joey "Please don't say that. Ever again. Please. You're a bad person."
        c_joey "I'm going to go now. Because you're a bad person."
        jump afterchoice
        
    label repentance:
        show joey neutral:
            align (0.5, 1.0)
        c_joey "Oh, okay. Good."
        jump afterchoice
    
    label afterchoice:
    hide shaun
    hide mike
    hide frank
    hide joey
    hide dom
    hide dan
    hide damien
    with moveoutright
    show tim neutral: #this looks awkward with tim already onscreen, someone suggest a fix pls
        align (0.5, 1.0)
    with moveinleft
    c_tim "Hey guys!"
    c_tim "Guys?"
    c_tim "What did I miss?"
    c_tim "Hey wait up!"
    hide tim
    with moveoutright
    
    show meiko angry:
        align (0.35, 1.0)
        
    c_meiko "GUYS."
    c_meiko "STOP FUCKING AROUND AND FINISH MAKING A GAME ABOUT ME."
    
    jump begone