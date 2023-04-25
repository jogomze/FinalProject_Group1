import time #import time is used to regulate the intervals at which text appear for better eligibility
    
def intro(): #by defining the function, we will later use it for the split between the 2 major decisions of the game
    time.sleep(2) #by creating the following function, we tell the program how long it will take for the paragraph to be displayed
    print("Welcome to Self, Solace, and Solitude! You will take charge of Par'Jenga, a crashlanded colonist. \n")
    
    print("As Par'Jenga  falls through the ashen sky of a yet to be born world, a cloud of ash hugs Par'Jenga while a sky of smoldering orange spectates its third colonist be dropped into its earth. Like a bloody drop from the cornea of an orange dream, Par'Jenga crashes violently against the ground. And as the earth lets out a cry, Par'Jenga opens their eyes.\n") #we use \n at the end so the next paragraph will have a space for better elegibility
    
    time.sleep(2)
    
    print("As far as Par'Jenga's sight could take them, they could only see oceans of lava along horizons of pure dread, gray-ash clouds below a murderous sky and a solemn sun whose lava-tears dripped into the earth. The confusion that overwhelmed Par'Jenga made only thoughts that would trip themselves across anxieties, that through the cracks of their mind, would drip into fears.how to create spaces between paragraphs in python\n")
    
    time.sleep(2)
    
    print("Accustomed to solitude, Par'Jenga surprisingly adapted to her situation extremely quickly. In just a few hours, she had already become all too familiar with the molten rocks that she would walk across, and by a little rock spectating the fiery ocean, Par'Jenga decided to settle down and make her own home. Three days would pass where she would walk the burning plateau with the only thought being how she would even begin the colonization process.\n")

    time.sleep(2)
    print("Par'Jenga scouts the horizon of the molten planes, at the moment, they can only think of doing 1 of 2 things. 1) settle down and make camp, 2) recount a song of the old world.\n")
    time.sleep(2)
    print("which option will they choose? Will they settle down or will they sing?\n")
    time.sleep(2)

def settle_down():
   print("Accustomed to solitude, Par'Jenga surprisingly adapted to her situation extremely quickly. In just a few hours, they had already become all too familiar with the molten rocks that they would walk across, and by a little rock spectating the fiery ocean, Par'Jenga decided to settle down and make her own home. Three days would pass where they would walk the burning plateau with the only thought being how they would even begin the colonization process.\n")
   time.sleep(2)
   
   print("As Par'Jenga waited by their new home gazing at the horizon, Ansodu sprung from the fiery ocean. A being with the tail of a scorpion, mandible of an ant, and torso of a wasp jumped from that endless liquid fire garnished in clothes representative of his culture. Two long strands hugged the back of his neck and the front of his torso, a poncho of unrecognizable fabrics softly covered the rest of his body, and at the end two boots with pointed ends.\n")
   time.sleep(2)
   
   print("Par'Jenga is startled! what will they do? (attack or greet)\n")
   time.sleep(2)
   
   choice = input().lower() # we make define choice by the type of input that will be later on used, while at the same time using .lower() so the program can accept both inputs in lower and upper case
   if choice == "attack":
       print("Par'Jenga attacks Ansodu, however, without any weapons or natural defences, Ansodu quickly over-takes Par'Jenga. Due to the perceived attack, Ansodu strikes back. Now all that's left on the earth is Par'Jenga's body\n")
    
   elif choice == "greet": # == is used to check whether values are equal rathe than re-assigning a value
       print("Par'Jenga greets Ansodu.\n")
       time.sleep(2)
       print("Ansodu explains that since he has been here, he has not seen a single other soul in the planet. Due to this, he asks Par'Jenga if they would like to travel the world together(Yes or No)\n")
       time.sleep(2)
       choice = input().lower()
       if choice == "no":
        print("Par'Jenga travels the world forever, until eventually life blooms in the world. The molten plains become grassy terrains, the volcanic oceans turn into the most serene aquamarine waves, and at the end of their life, Par'Jenga lays down in their camp. As Par'Jenga admires the horizon, their weary eyes shut, until eventually they never open again.\n")
        time.sleep(2)
        
       elif choice == "yes":
        print("\nHours, months, and decades pass as the eras carry on. Through this long, and ardous exploration the oceans turn blue. The earth, no longer scorching, creates a scenery that both Ansodu and Par'Jenga had forgotten long ago. It is in this serenity that Ansodu asks Par'Jenga if they would like to be something \"more\"\n")
        time.sleep(2)
        print("How does Par'Jenga respond?(Yes or No)\n")
        time.sleep(2)
        choice = input().lower()
        if choice == "no":
            print("As the years pass by, the friendship that Par'Jenga and Ansodu would create would eventually become as strong as the core of planet himself. Years would pass until Ansodu would fall to an incredible sickness. In his last moments, v would remain by his side. Ansodu's body would twist and transform until it became a great forest. In this great forest, Par'Jenga would remain, tending to the needs of life itself, until their own life would pass away")
        else:
            print("Accepting the confession of love by Ansodu, Par'Jenga would walk across bizzare mirages and chaotic mountains. At the top of the greatest mountain, Ansodu and Par'Jenga would make their home, where they could see the world in its full beauty. The years would pass until their eventual death, however, before their inevitable end, Par'Jenga would only say \"this was a good life\"")

def sing():
    print("Par'Jenga sings songs from the old world\n")
    time.sleep(2)
   
    print("In the trance of the tunes, an interloper shows herself \"Hi, my name is Gabransa\".\n")
    time.sleep(2)
   
    print("What does Par'Jenga do? (ignore or greet)\n")
    time.sleep(2)
   
    choice = input().lower()
    if choice == "ignore":
     print("Par'Jenga ignores Gabransa.\n")
     time.sleep(2)
     print("Par'Jenga would travel the ever-evolving world without ever meeting anyone again. In their end times Par'Jenga would wonder how different life would be had they not ignore Gabransa\n")
    
    elif choice == "greet":
        print("Par'Jenga greets Gabransa.\n")
        time.sleep(2)
        print("Gabransa explains that she has been lost for a long time and seeing how Par'Jenga sings songs from the old world she would like to tag along.(Yes or No)\n")
        time.sleep(2)
        choice = input().lower()
        if choice == "no":
            print("Par'Jenga would travel the world alone, sometimes seeing Gabransa along the shore. Even if fickle, their friendship would eventually bloom as the years progressed, until one day they wouldn't be able to see each other again.\n")
        
        elif choice == "yes":
         print("Singing songs of the old world, Par'Jenga and Gabransa would travel the world in search of beauty were beauty doesn't exist. In this endless search Gabransa would notice that the most beautiful thing to exist in this world was Par'Jenga. So, by mustering all her strenght, she asked Par'Jenga if they would like to become something \"more\".\n")
         time.sleep(2)
         print("How does Par'Jenga respond?(Yes or No)\n")
         time.sleep(2)
         choice = input().lower()
         
         if choice == "no":
             print("Although Par'Jenga wouldn't reciprocate the feelings that Gabransa expressed, they would remain friends for immemorable times. Epochs and eras would pass until a great forest would emerge into the great volcanic planet. In this great forest that they would call \"Ansodu\" they would lie until the day that Gabransa had to leave. In the final days of Gabransa, Par'Jenga would take her to the fiery ocean. Gabransa would look at the endless horizon and say \"dont miss me too much Par'Jenga. When you cross to the other side I will be waiting for you with open arms\". As she says that her body would fall into the ocean, cooling it with the serenity of her life, until aquamarine oceans of peacefullness would emerge. Par'Jenga would admire this ocean until the end of his days\n")
         else:
             print("Accepting the confession of love by Gabransa, Par'Jenga would sing, chant and dance with Gabransa. The solitude that they were used to would disolve along the laughs, and Par'Jenga would understand that this is what happiness must truly feel like. Cycles would pass in their roccoco-like life, until eventually both would grow too old to stand. So, along the edge of a cliff, before their end Par'Jenga would tell Gabransa: \"this was a good life\".\n")

def main(): #The def main(): statement in the code defines a function called main(). Any code that is written inside this function will be executed when the program is run.
    intro()
    choice = input().lower()
    if choice == "settle down":
        settle_down()
        
    elif choice == "sing":
        sing()
        
    else:
        print("Invalid choice. Please choose again.")
        
if __name__ == "__main__":#checks if the current module is being executed as the main program
    main()
