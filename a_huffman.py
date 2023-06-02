# huffman.py
## author - Gregory L.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message = "Hello there"
#Coolio
message2 = "As I walk through the valley of the shadow of death I take a look at my life and realize there\'s nothin\' left \'Cause I\'ve been blastin\' and laughin\' so long, that Even my mama thinks that my mind is gone But I ain\'t never crossed a man that didn\'t deserve it Me be treated like a punk, you know that\'s unheard of You better watch how you\'re talkin\', and where you\'re walkin\' Or you and your homies might be lined in chalk I really hate to trip but I gotta loc As they croak, I see myself in the pistol smoke, fool I\'m the kinda G the little homies wanna be like On my knees in the night, sayin\' prayers in the streetlight Been spendin\' most their lives, livin\' in the gangsta\'s paradise Been spendin\' most their lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise Look at the situation they got me facin\' I can\'t live a normal life, I was raised by the street So I gotta be down with the hood team Too much television watchin\' got me chasin\' dreams I\'m an educated fool with money on my mind Got my ten in my hand and a gleam in my eye I\'m a loc\'d out gangsta, set trippin\' banger And my homies is down so don\'t arouse my anger, fool Death ain\'t nothin\' but a heartbeat away I\'m livin\' life, do or die, what can I say? I\'m 23 now, but will I live to see 24? The way things is going, I don\'t know Tell me why are we so blind to see That the ones we hurt are you and me? Been spendin\' most their lives, livin\' in the gangsta\'s paradise Been spendin\' most their lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise Power and the money, money and the power Minute after minute, hour after hour Everybody\'s runnin\', but half of them ain\'t lookin\' It\'s goin\' on in the kitchen, but I don\'t know what\'s cookin\' They say I gotta learn, but nobody\'s here to teach me If they can\'t understand it, how can they reach me I guess they can\'t, I guess they won\'t I guess they front, that\'s why I know my life is out of luck, fool Been spendin\' most their lives, livin\' in the gangsta\'s paradise Been spendin\' most their lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise We keep spendin\' most our lives, livin\' in the gangsta\'s paradise Tell me why are we so blind to see That the ones we hurt are you and me? Tell me why are we so blind to see That the ones we hurt are you and me?"
#Weird Al
message3 = "As I walk through the valley where I harvest my grain I take a look at my wife and realize she\'s very plain But that\'s just perfect for an Amish like me You know, I shun fancy things like electricity At 4:30 in the morning, I\'m milkin\' cows Jebediah feeds the chickens and Jacob plows, fool And I\'ve been milkin\' and plowin\' so long that Even Ezekiel thinks that my mind is gone I\'m a man of the land, I\'m into discipline Got a Bible in my hand and a beard on my chin But if I finish all of my chores, and you finish thine Then tonight, we\'re gonna party like it\'s 1699 We been spending most our lives Livin\' in an Amish paradise I churned butter once or twice Livin\' in an Amish paradise It\'s hard work and sacrifice Livin\' in an Amish paradise We sell quilts at discount price Livin\' in an Amish paradise A local boy kicked me in the butt last week I just smiled at him and I turned the other cheek I really don\'t care, in fact I wish him well \'Cause I\'ll be laughing my head off when he\'s burning in Hell But I ain\'t never punched a tourist even if he deserved it An Amish with a \'tude? You know that\'s unheard of I never wear buttons but I got a cool hat And my homies agree I really look good in black, fool If you come to visit, you\'ll be bored to tears We haven\'t even paid the phone bill in 300 years But we ain\'t really quaint, so please don\'t point and stare We\'re just technologically impaired There\'s no phone, no lights, no motorcar Not a single luxury Like Robinson Crusoe It\'s as primitive as can be We been spending most our lives Livin\' in an Amish paradise We\'re just plain and simple guys Livin\' in an Amish paradise There\'s no time for sin and vice Livin\' in an Amish paradise We don\'t fight, we all play nice Livin\' in an Amish paradise Hitchin\' up the buggy, churnin\' lots of butter Raised a barn on Monday, soon I\'ll raise another Think you\'re really righteous? Think you\'re pure in heart? Well, I know I\'m a million times as humble as thou art I\'m the pious guy the little Amlettes wanna be like On my knees day and night, scorin\' points for the afterlife So don\'t be vain and don\'t be whiny Or else, my brother, I might have to get medieval on your heinie We been spending most our lives Livin\' in an Amish paradise We\'re all crazy Mennonites Livin\' in an Amish paradise There\'s no cops or traffic lights Livin\' in an Amish paradise But you\'d probably think it bites Livin\' in an Amish paradise"
#Parody I made for one of my math classes
message4 = "As I write with my pencil on the theory of group, I miss an operation, and I start to droop, But that\'s no problem for Algebraist like me Just define a new one with Distributivity! At 12 o\'clock in the high noon, I sit in class, Take the quizzes, take exams, and try to pass Fool! And I\'ve been provin\' and writin\' so long That even my advisor thinks that my mind is gone! I\'m a lord of the rngs, and a group-maker that Draws a formal sum that\'s finite for a coproduct hat But if you got a unity, and characteristic prime, Then every element\'s a unit, and your field is lookin\' fine. We been spending most our lives Livin\' in Algebraist\'s Paradise! We got Euler lookin\' wise Livin\' in Algebraist\'s Paradise! We prove theorems once or twice Livin\' in Algebraist\'s Paradise! Sylow groups will conjugize Livin\' in Algebraist\'s Paradise! An exam problem asked me ‘bout Zn last week, Prove the relatively prime are the units you seek. Euler\'s Theorem\'s got your phi n to power, Find equiv to 1, watch your time save tower! If your gcd is 1 for ax = b, Got a unique solute\' You know Fermat says that. Integral domain becomes equivalence class, Now extend it to a field, add and mult like their fracs Fool! If you add some x\'s, get an irreducing poly, Extend the field to closure and get zeroes for your folly But degree\'s, finite these, gets vector space you seek The Galois Field p-to-n\'s unique Every max ideal is prime ideal, Every PID is a UFD, Can ascend containment finitely If you meet your ACC. We been spending most our lives Livin' in Algebraist\'s Paradise! Topology gives us Lies, Livin' in Algebraist\'s Paradise! All the time in quiz just flies, Livin' in Algebraist\'s Paradise! We know Monsters don\'t play nice, Livin' in Algebraist\'s Paradise! Quotientin\' the kernels, factorin\' your polys, Close a field on one day, then reduce your bases! Think you know your Grobners? Think you\'re good at math? Well I know I learned methods for irreducing that path Doesn\'t take an Eisenstein to realize That the reals aren\'t bright, transcendentals gonna give you fright! But don\'t be ‘fraid, and presuppose, Just quotient x^2+1 to get the complex which is closed! We been spending most our lives Livin\' in Algebraist\'s Paradise! Kernel and range homomorphize, Livin\' in Algebraist\'s Paradise! With four quarters, my brain fries Livin\' in Algebraist\'s Paradise! You will find a nice surprise, Livin\' in Algebraist\'s Paradise! Oooooooooooough"

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
letterfreq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
allnodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


## defining our data structures
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

    def __str__(self):
        return "Letter " + str(self.letter) + ", Frequency " + str(self.frequency) + ", Left (" + str(self.left) + "), Right (" + str(self.right) + ")"

## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding
    if v.letter != None:
        coding[v.letter] = path
    else:
        retrieve_codes(v.left, path+"0")
        retrieve_codes(v.right, path+"1")

# STEP 1
## counting the frequencies
message = message.upper()
for letter in message:
    if letter not in letterfreq.keys():
        letterfreq[letter] = 1
    else:
        letterfreq[letter] += 1




# STEP 2
## initialize the nodes
allnodes = list()
for (letter, letterfreq) in letterfreq.items():
    allnodes.append(Node(letter, letterfreq))



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
print(coding)

result = ""
for letter in message:
    result += coding[letter]

print(result)

# STEP 5
## analyize compression performance
n_original_bits: int = len(message) * 8
n_encoded_bits: int = len(result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')