from random import randint as rint 
wordlist=[]
Final_Wordlist=[] 
with open("wordlewords.txt","r",newline="") as wordFile:
    for word in wordFile:
        word=word.strip()
        wordlist.append(word) 
       
            
GREEN, YELLOW, GRAY = ('g', 'y', 'b')
def getword():
  var=rint(0,len(wordlist)-1)
  return wordlist[var]



while True:
    word=getword()
    print(word)
    res=input("")
    
    for i in range(5):
                invalid = []
                if res[i] == GREEN:
                    # correct character + correct position
                    for w in wordlist:
                        if w[i] != word[i]:
                            invalid.append(w)
                elif res[i] == YELLOW:
                    # correct character + wrong position
                    for w in wordlist:
                        if word[i] not in w:
                            invalid.append(w)
                        elif w[i] == word[i]:
                          invalid.append(w)
                elif res[i] == GRAY:
                    # wrong character
                    for w in wordlist:
                        if word[i] in w:
                            special_case = False
                            for j in range(5):
                                if i != j and word[i] == word[j] and res[j] in [GREEN, YELLOW]:
                                    special_case = True
                            if not special_case:
                                invalid.append(w)

                for i_word in invalid:
                  wordlist.remove(i_word)

    print(wordlist)

    print(len(wordlist))
           
            
                      
            