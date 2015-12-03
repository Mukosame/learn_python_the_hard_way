class lexicon(object):

    def __init__ (self):
        self.stuff = {}
        self.words = {}
        self.sentence = []

    def findit(self, todo):
        direction = 'north south east'
        verb = 'go kill eat'
        stop = 'the in of'
        noun = 'bear princess'
        number = '3 91234'
        if (todo in direction):
            return 'direction'
        elif (todo in verb):
            return 'verb'
        elif(todo in stop):
            return 'stop'
        elif(todo in noun):
            return 'noun'
        elif(todo in number):
            return 'number'
        else:
            return 'error'
        
    def scan(self, stuff):
        #self.stuff = raw_input('> ')
        self.words = stuff.split()
        #analysis and return to a sentence
        while len(self.words) != 0:
            todo = self.words.pop()
            self.sentence.append((self.findit(todo), todo))
        return self.sentence

lexicon = lexicon();
print lexicon.scan('go north')
