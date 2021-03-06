'''the order in which to check for categories will be the following:
  - directly particle or interjection if len(word)<4 (pronouns are included)
  - correlative
  - noun
  - adjective
  - verb
  - adverb
  '''
  
def isCorrelative(word):
    basis = ['ki', 'ti', 'ĉi', 'i', 'neni']
    suffix = ['a', 'al', 'am', 'e', 'el', 'es', 'o', 'om', 'u']
    for prefix in basis:
        for ending in suffix:
          if prefix+ending in word[-6:-1]:
                    return True
                return False
        return False
    return False
    
def isNoun(word):
    if word[-1].lower() not in ['o', 'j', 'n']:
        return False
    elif word[-1].lower() == 'n':
        return word[-3:-2]=='oj' or word[-2]=='o'
    elif word[-1].lower()=='o':
        return True
    return False
    
def isAdjective(word):
    if word[-1].lower() not in ['a', ''j', 'n']:
        return False
    elif word[-1].lower()=='n':
        return word[-3:-2]=='aj' or word[-2]=='a'
    elif word[-1].lower()=='a':
        return True
    return True
        
def isVerb(word):
    if word[-1].lower() not in ['s', 'u', 'i']:
        if word[-3:-1].lower() in ['nta', 'ata', 'ita', 'ota']:
            return True
        return False
    elif word[-1].lower() == 's' and word[-2].lower() in ['a', 'i', 'o', 'u']:
        return True
    elif word[-1].lower()=='i' or word[-1].lower()=='u' and len(word) > 3:
        return True
    return False
    
def isParticipe(word):
    return isAdjective(word) and isVerb(word)

def isAdverb(word):
    return len(word)>3 and word[-1].lower()=='e'

def typeWord(word):
    if isCorrelative(word): return 'correlative'
    elif isNoun(word): return 'noun'
    elif isParticipe(word): return 'participe'                            
    elif isVerb(word): return 'verb'
    elif isAdverb(word): return 'adverb'
    elif isAdjective(word): return 'adjective'                            
    else: return 'particle'
                                
'''def Dictionary(filename):
    isURL1 = "http://"
    isURL2 = "https://"
    if filename.startswith(isURL1) or filename.startswith(isURL2) :
        from urllib.request import urlopen
        webPage = urlopen(filename)
        text = str(webPage.read(), "utf-8")
        webPage.close()
    else:
        f = open(filename, "r")
        text = f.read()
        f.close()
    return text'''
    
def Dictionary(text):
  words = text.split(' ').split('\n')                                
  pass   
                                
                                
  
        
