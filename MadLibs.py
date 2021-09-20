def madLibs():
    #mad Libs accepts no arguments
    #It gets nouns, verbs, adjectives, and adverbs
    #It displays a story with the inserted words
    
    #Get the insert words and phrases
    print('Mad Libs: Doomed on Zoom')
    timeUnit = input('Enter a unit of time:')
    adj1 = input('Enter an adjective:')
    noun1 = input('Enter a noun:')
    noun2 = input('Enter a second noun:')
    num1 = input('Enter a number:')
    noun3 = input('Enter a third noun:')
    cothingItem = input('Enter an item of clothing:')
    animal = input('Enter an animal in plural form (tigers, bats, etc):')
    person1 = input("Enter a person's name:")
    verb1 = input('Enter a verb in the past tense:')
    noun4 = input('Enter a fourth noun:')
    
    imFigure = input('Enter an imaginary creature:')
    popCulture = input('Enter a pop culture icon:')
    adj2 = input('Enter a second adjective:')
    memberFamily = ('Enter a family member title (Dad, brother, etc):')
    verb2 = input('Enter a verb ending in -ing:')
    songTitle = input('Enter a song title:')
    person2 = input("Enter a second person's name:")
    website = input('Enter a website name:')
    
    techCEO = input('Enter the name of a tech CEO:')
    verb3 = input('Enter a third verb:')
    liquid = input('Enter the name of a liquid:')
    eDevice = input('Enter the name of an electronic device:')
    phrase = input('Enter a phrase or exclamation:')
    food = input('Enter a type of food:')
    verb4 = input('Enter a verb ending in -ing:')
    
    #Display the story with the inserted words or phrases
    print('Mad Libs: Doomed on Zoom')
    
    print("We've all been using Zoom for over a", timeUnit, 'now, but not everyone is', adj1, 'when it comes'\
          'to best practices for', noun1, 'meetings. Recently, I attended a panel discussion on', noun2,\
          '. First, the event had a delayed strat because it took', num1, 'minutes for the panelists to figure'\
          'out how to use the', noun3, 'button. The lead speaker was wearing nothing but a', cothingItem,\
          ', and several attendees were distracted by their pet', animal, '. The meeting really went off the rails'\
          'when', person1, verb1, 'while not realizing they were unmuted. It was all', noun4, 'from there on out.'\
          'The host,', person1, ',tried to restore order, but no one took them seriously because of their', \
          imFigure, 'filter. My', popCulture, 'virtual background seemed', adj2, 'in comparison. The meeting'\
          "continued, until it was interrupted by one of the speaker's", memberFamily, verb2, 'in the background.'\
          'Someone started playing', songTitle, 'by', person2, ', and', website, 'could be seen in the tabs of'\
          'whoever was screensharing. Things became so crazy that', techCEO, 'joined the meeting just to',\
          verb3, 'everyone in the audience. Before they could speak, the Zoom lost connection because the host'\
          'spilled', liquid, 'on their', eDevice, '. We never even got to say "', phrase, '." People just need '\
          'to learn their manners. Now, back to doom-scrolling, baking', food, 'and', verb4, 'for me.')
    