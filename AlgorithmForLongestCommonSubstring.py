NO_OF_CHARS = 256
def BMwyszukiwanie(ciagZnakow, znakSzukany, złyZnakSprawdzenie):
    znak = len(znakSzukany)
    ciag = len(ciagZnakow)
    złyZnak = złyZnakSprawdzenie(znakSzukany, znak)
    s = 0
    tab=[]
    while(s <= ciag-znak):
        j = znak-1
        while j>=0 and znakSzukany[j] == ciagZnakow[s+j]:
            j -= 1
        if j<0:
            tab.append(format(s))
            s += (znak-złyZnak[ord(ciagZnakow[s+znak])] if s+znak<ciag else 1)
        else:
            s += max(1, j-złyZnak[ord(ciagZnakow[s+j])])
    if tab==[]:
        a=None
    else:
        a=True
    return tab, a 

def złyZnakSprawdzenie(string, size):
    badChar = [-1]*NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def create_array(tab,integer):
    new_one=[]
    for i in range(0,len(tab)):
        new_one.append(tab[i][integer])
    return new_one
def longest(string1, string2, BMSearch, funkcja, array):

    if string2>string1:
        c=string2
        string2=string1
        string1=c
    all_found_strings=[]
    for i in range(0,len(string2)):
        value=string2[i]
        for j in range(1+i,len(string2)+1):
            tab, flag =BMSearch(string1,value,funkcja)
            if flag==True:
                all_found_strings.append([tab,value,len(value)])
            if j!=len(string2):
                value=value+string2[j]
            print(value)
    siezes=array(all_found_strings,2)
    maximum=max(siezes)
    index = siezes.index(maximum)
    return all_found_strings[index]
d=longest("abccacbdbdadacb", "bdacaabcacbda",BMwyszukiwanie, złyZnakSprawdzenie,create_array)
print(d)
