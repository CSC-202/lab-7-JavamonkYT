# huffman-analysis.py
## author - Gregory L.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt


class Node:
    letter: str
    frequency: int
    left: any
    right: any

    def __init__(self, letter, frequency, left=None, right=None):
        self.letter = letter
        self.frequency = frequency
        self.left = left
        self.right = right

def retrieve_codes(v, path=""):
    global coding
    if v.letter != None:
        coding[v.letter] = path
    else:
        retrieve_codes(v.left, path+"0")
        retrieve_codes(v.right, path+"1")



# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding

# DATA - lyrics
POKEMON_LYRICS = 'I wanna be the very best. Like no one ever was. To catch them is my real test. To train them is my cause. I will travel across the land. Searching far and wide. Each Pokemon to understand. The power that\'s inside. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny. (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon. (gotta catch \'em all.) Gotta catch \'em all. Yeah. Every challenge along the way. With courage I will face. I will battle every day. To claim my rightful place. Come with me, the time is right. There\'s no better team. Arm in arm we\'ll win the fight. It\'s always been our dream. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon (gotta catch \'em all.) Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Yeah! (Pokemon, gotta catch \'em all). Its you and me. I know it\'s my destiny. (Pokemon) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you Pokemon. (gotta catch \'em all). Gotta catch \'em all. (Pokemon)'
JIGGLE_JIGGLE = 'You have to have something that sticks. You have to have something that\'s monumental. When you walk out on stage, that\'s been monumental. (Jiggle, jiggle) Can you remember any of the rap that you did? My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. I sip booze from chalices, holding my palaces. Crib is so crampy suckers suffer from paralysis. Rhymes, I write them in the castle. You try to diss me and pretty soon your ass. Will squat in a cell \'cause I can tell you it\'s illegal. Treason, that\'s the reason I\'m regal. You do the time for the crime of lèse-majesté. And **** the police \'cause they can\'t arrest me. (They can\'t arrest me, they can\'t arrest me). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?)'
ALPHABET = 'Now it\'s time for our wrap up. Let\'s give it everything we\'ve got. Ready, begin. Artificial amateurs aren\'t at all amazing. Analytically, I assault, animate things. Broken barriers bounded by the bomb beat. Buildings are broken, basically I\'m bombarding. Casually create catastrophes, casualties. Canceling cats got their canopies collapsing. Detonate a dime of dank daily doin\' dough. Demonstrations, Don Dada on the down low. Eatin\' other editors with each and every energetic. Epileptic episode, elevated etiquette. Furious fat fabulous fantastic. Flurries of funk felt feeding the fanatics. Imitators idolize, I intimidate. In a instant, I\'ll rise in a irate state. Juiced on my jams like jheri curls, jockin\' joints. Justly, it\'s just me, writin\' my journals. Kindly I\'m kindling all kinds of ink on. Karate kick type Brits in my kingdom. Let me live a long life, lyrically lessons is. Learned lame louses just lose to my livery. My mind makes marvelous moves, masses. Marvel and move, many mock what I\'ve mastered.  Niggas nap knowin\' I\'m nice naturally. Knack, never lack, make noise nationally.  Operation, opposition, off, not optional. Out of sight, out of mind, wide beaming opticals. Perfected poem, powerful punchlines. Pummeling petty powder puffs in my prime. Quite quaint quotes keep quiet it\'s Quannum Quarrelers ain\'t got a quarter of what we got, uh. Really raw raps, risin\' up rapidly. Riding the rushing radioactivity. Super scientifical sound search sought. Silencing super fire saps that are soft. Tales ten times talented, they\'re too tough. Take that, challengers, get a tune up. Universal, unique untouched. Unadulterated, the raw uncut. Verb vice Lord victorious valid. Violate vibes that are vain make \'em vanished. Why I\'m all well, would a wise wordsmith. Just weaving up words weeded up, on my work shift. Xerox, my X-ray-diation holes extra large. X-height letters and xylophone tones.'

#Coolio's "Gangsta's Paradise"
coolio = "As I walk through the valley of the shadow of death I take a look at my life and realize there\'s nothin\' left \'Cause I\'ve been blastin\' and laughin\' so long, that Even my mama thinks that my mind is gone But I ain\'t never crossed a man that didn\'t deserve it Me be treated like a punk, you know that\'s unheard of You better watch how you\'re talkin\', and where you\'re walkin\' Or you and your homies might be lined in chalk I really hate to trip but I gotta loc As they croak, I see myself in the pistol smoke, fool I\'m the kinda G the little homies wanna be like On my knees in the night, sayin\' prayers in the streetlight Been spendin\' most their lives, livin\' in the gangsta\'s paradise Been spendin\' most their lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise Look at the situation they got me facin\' I can\'t live a normal life, I was raised by the street So I gotta be down with the hood team Too much television watchin\' got me chasin\' dreams I\'m an educated fool with money on my mind Got my ten in my hand and a gleam in my eye I\'m a loc\'d out gangsta, set trippin\' banger And my homies is down so don\'t arouse my anger, fool Death ain\'t nothin\' but a heartbeat away I\'m livin\' life, do or die, what can I say? I\'m 23 now, but will I live to see 24? The way things is going, I don\'t know Tell me why are we so blind to see That the ones we hurt are you and me? Been spendin\' most their lives, livin\' in the gangsta\'s paradise Been spendin\' most their lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise Power and the money, money and the power Minute after minute, hour after hour Everybody\'s runnin\', but half of them ain\'t lookin\' It\'s goin\' on in the kitchen, but I don\'t know what\'s cookin\' They say I gotta learn, but nobody\'s here to teach me If they can\'t understand it, how can they reach me I guess they can\'t, I guess they won\'t I guess they front, that\'s why I know my life is out of luck, fool Been spendin\' most their lives, livin\' in the gangsta\'s paradise Been spendin\' most their lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise Tell me why are we so blind to see That the ones we hurt are you and me? Tell me why are we so blind to see That the ones we hurt are you and me?"
#Weird Al's "Handy"
weirdal = "First things first, I\'m a craftsman (craftsman) Remodelling is my only passion (it\'s my passion) And I\'m the greatest in the business Want referrals, yo My clientèle will bear you witness (right, right) I can help when your door jamb sticks (heh?) There is nothing in the world I can\'t fix (yeah) I do tiles, I do stone, I do bricks Call me, I\'ll come rushing over with my bag of tricks (bag of tricks) Where you go when your disposal is rusted (rusted) Termite problem making you disgusted (yuck) When your front window is busted (hey hey hey) Just one man that\'s always trusted I\'m so handy, you already know I\'ll fix your plumbing when your toilets over flows I\'m so handy, I\'ll bring you up to code When your dishwasher\'s about to explode Now you see that your furnace is needing some service I\'m fully bonded, no need to be nervous Perhaps you would like a new counter Formica Maybe I\'ll hook up your dish washer combo dryer But all your pipes are antique Your water pressure\'s too weak You got an attic full of dry rot Because your roof sprung a leak Your fridge is starting to reek Your hardwood floors really squeak But don\'t you worry I\'ll just show you my amazing technique Now let me glue that, glue that and screw that, screw that Any random chore you got, well I can do that, do that Or maybe I\'ll just rewire your house for fun I got 99 problems but a switch ain\'t one I\'m so handy, everyone said so I\'ll grout your bathroom, resurface your patio I\'m so handy, I\'m the guy to know When your leaf blower doesn\'t blow-oh-oh-oh Patch the drywall, clean your gutters and mow the lawn Make that phone call, I\'ll install anything you want Yeah, check my big staple gun, my socket wrenches are second to none I won\'t quit \'til I\'m done, don\'t even care if I hammer my thumb (OW!) Still rocking my screwdriver Got the whole world thinking I\'m MacGuyver Your heating bills are shocking I can solve that with some duct tape and some caulking Your house is a disaster, huh? Need a guy whose a master with the plaster, huh? Let me be your stripper Taking off lacquer, no one does it quicker I\'m so handy, you already know I\'ll beat all price quotes, my hourly rates are low I\'m so handy, you should call this pro I\'m in the phone book and se habla Español"
#Tim Blais's "Leukocyte"
timblais = "Cause I I I got the SARS tonight So watch me ring up my blood cells of white First up Coming through the blood Neutrophil come slow your roll Eat up micro bods Gummed up when your guts explode Hang tight waiting monocyte Hulk out til you\'re chowing em down Signals from my killer cells And those weak and infected go \"blao\" This is getting heavy Better get the lymph nodes all ready Got a fever running And these signal cytokines flooding Defense overrun we need to send a sample on Dendritic, you gotta go off so let\'s go! Cause I I I got the SARS tonight So watch me bring peptides to the meeting site Fly into the lymph node with the details of the bug So I can fight it off by leukocyte Bring a friend, join the crowd Together filling up the node New white lymphocytes Of the thymus and the bone Scatter-gun, million-to-one Which ones are compatible? \"Ladies and gentlemen I got the antigen So you can keep your eyes on the ball This is getting heavy Can we get T\'s trained already Helping, teaching, gunning Plasma cells with antibods flooding These made optimal We need to save a sample of Archive em, y\'all others go off And let\'s go Cause I I I got the SARS tonight So watch me bring trained cells to the battle site Target a specific set of features of the bug So I can fight it off by leukocyte Slide through the side to find the right site of the fight Fight it leukocyte Fly like a guided viricide bind to the site Fight it leukocyte Target cells exhibiting a feature of the bug So I can fight it off by leukocyte Die for the tribe deny the shock play Try and imbibe a fly-by-night prey Pry, nullify the viral home bay Fight it off leukocyte Spy to provide a vital dossier Vie to supply the binding Y shape Scry, then apply a cytokine aide Fight it off leukocyte Cause I I I got the SARS tonight So watch me bring all guns to the firefight Target tainted tissue with a team to SWAT the bug So I can fight it off by leukocyte Cause I I I got the SARS tonight So watch me bring the fire to the parasite Integrated synergy to seek and squash the bug So I can fight it off by leukocyte Guide what survived to multiply righting the blight Right it leukocyte Time to resign, the high supply cost to requite Bite it leukocyte But I will keep this memory with features of the bug So I can fight it off by leukocyte"




# DATA - mantras
GREEN_LATTERN = 'In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil\'s might, Beware my power... Green Lantern\'s light!'
JEDI_CODE = 'Emotion, yet peace. Ignorance, yet knowledge. Passion, yet serenity. Chaos, yet harmony. Death, yet the Force.'
SITH_CODE = 'Peace is a lie. There is only Passion. Through Passion, I gain Strength. Through Strength, I gain Power. Through Power, I gain Victory. Through Victory my chains are Broken. The Force shall free me.'

wreckitralph = "I\'m bad, and that\'s good. I will never be good, and that\'s not bad. There\'s no one I\'d rather be than me."
vogonpoetry = "Oh freddled gruntbuggly, Thy micturations are to me, As plurdled gabbleblotchits, in midsummer morning On a lurgid bee, That mordiously hath blurted out, Its earted jurtles, grumbling Into a rancid festering confectious organ squealer. Now the jurpling slayjid agrocrustles, Are slurping hagrilly up the axlegrurts, And living glupules frart and stipulate, Like jowling meated liverslime, Groop, I implore thee, my foonting turlingdromes, And hooptiously drangle me, With crinkly bindlewurdles, mashurbitries. Or else I shall rend thee in the gobberwarts with my blurglecruncheon, See if I don\'t!"
rickandmorty = "To be fair, you have to have a very high IQ to understand Rick and Morty. The humour is extremely subtle, and without a solid grasp of theoretical physics most of the okes will go over a typical viewer\'s head. There\'s also Rick\'s nihilistic outlook, which is deftly woven into his characterisation- his personal philosophy draws heavily from Narodnaya Volya literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of these jokes, to realise that they\'re not just funny- they say something deep about LIFE. As a consequence people who dislike Rick & Morty truly ARE idiots- of course they wouldn\'t appreciate, for instance, the humour in Rick\'s existential catchphrase \"Wubba Lubba Dub Dub,\" which itself is a cryptic reference to Turgenev\'s Russian epic Fathers and Sons. I\'m smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Dan Harmon\'s genius wit unfolds itself on their television screens. What fools.. how I pity them. And yes, by the way, i DO have a Rick & Morty tattoo. And no, you cannot see it. It\'s for the ladies\' eyes only- and even then they have to demonstrate that they\'re within 5 IQ points of my own (preferably lower) beforehand. Nothin personnel kid."



# the input, what we want to encode
def huffman(message:str) -> float:
    global coding

    # for counting the letter frequencies
    letterfreq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    allnodes: list = list()
    # the output, should be all 0's and 1s
    result = str()

    message = message.upper()

    for letter in message:
        if letter not in letterfreq.keys():
            letterfreq[letter] = 1
        else:
            letterfreq[letter] += 1

    print(letterfreq)


    # STEP 2
    ## initialize the nodes
    allnodes = list()
    for (letter, frequency) in letterfreq.items():
        allnodes.append(Node(letter, frequency))



    # STEP 3
    ## combine each nodes until there's only one item in the nodes list
    while len(allnodes) > 1:
        ## sort based on weight
        allnodes.sort(key=lambda x: x.frequency, reverse=True)

        ## get the first min
        min_a: Node = allnodes.pop()

        ## get the second min
        min_b: Node = allnodes.pop()

        ## combine the two
        combined = Node(letter=None, frequency=(min_a.frequency + min_b.frequency), left=min_b, right=min_a)

        ## put the combined nodes back in the list of nodes
        allnodes.append(combined)





    # STEP 4
    ## reconstruct the codes
    huff_root = allnodes[0]
    retrieve_codes(huff_root)

    result = ""
    for letter in message:
        result += coding[letter]

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)



    return result, coding, compression_ratio




# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Leathrum Analyzing Huffman')
plt.gcf().supylabel("Compression %")
plt.gcf().supxlabel("Length of Message")
MAX_N: int = int(128 * 3 / 2)
x = [i for i in range(1, MAX_N)]

# PLOT 1
## POKEMON
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = coolio[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(x, ratios, linestyle="dashdot", linewidth=2)

## JIGGLE JIGGLE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = weirdal[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(x, ratios, linestyle="dashdot", linewidth=2)

## ALPHABET
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = timblais[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(x, ratios, linestyle="dashdot", linewidth=2)
plt.legend(["Gangsta's Paradise (n=" + str(len(coolio)) + ")", "Handy (n=" + str(len(weirdal)) + ")", "Leukocyte (n=" + str(len(timblais)) + ")"])

# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = wreckitralph[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(x, ratios, linestyle="dashdot", linewidth=2)

## GREEN LATERN'S OATH
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = vogonpoetry[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(x, ratios, linestyle="dashdot", linewidth=2)

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = rickandmorty[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(x, ratios, linestyle="dashdot", linewidth=2)
plt.legend(["Wreck-It Ralph (n=" + str(len(wreckitralph)) + ")", "Vogon Poetry (n=" + str(len(vogonpoetry)) + ")", "Rick and Morty (n=" + str(len(rickandmorty)) + ")"])

plt.savefig("C:/Users/grego/Desktop/CalPoly_Senior/CS202/lab-7-JavamonkYT-master/figs/lab7_leathrum.png")
'''



coding = dict()
_, _, ratio = huffman(coolio)
print("Coolio:", coding)
print("Ratio:", ratio)
coding = dict()
_, _, ratio = huffman(weirdal)
print("Weird Al:", coding)
print("Ratio:", ratio)
coding = dict()
_, _, ratio = huffman(timblais)
print("Tim Blais:", coding)
print("Ratio:", ratio)
coding = dict()
_, _, ratio = huffman(wreckitralph)
print("Wreck It Ralph:", coding)
print("Ratio:", ratio)
coding = dict()
_, _, ratio = huffman(vogonpoetry)
print("Vogon Poetry:", coding)
print("Ratio:", ratio)
coding = dict()
_, _, ratio = huffman(rickandmorty)
print("Rick And Morty:", coding)
print("Ratio:", ratio)
'''