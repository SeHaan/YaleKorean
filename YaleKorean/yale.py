#%%
from .dict_yale import dict_0_YALE
from .dict_total import dict_0_TOTAL

def PUAtoUni(line: str) -> str:
    """
    ## PUAtoUni(line: str) -> str
    - Hanyang PUA to Unicode Hangul Jamo Plain
    """
    new_line = ''
    for i in range(len(line)):
        tt = ord(line[i])

        ## Hanyang PUA -> 첫가끝 ##
        if (tt >= 0xe0bc and tt <= 0xefff) or (tt >= 0xf100 and tt <= 0xf66e):
            new_line = new_line + dict_0_TOTAL[tt]

        ## 조합형 -> 첫가끝 ##
        elif (tt >= 0xac00 and tt <=0xd79f):
            onset = chr(((tt - 0xac00) // (28*21)) + 0x1100)
            peak = chr((((tt - 0xac00) % (28*21)) // 28) + 0x1161)
            coda = chr(((tt - 0xac00) % 28) + 0x11a7)
              
            new_line += onset
            new_line += peak
            if (tt - 0xac00) % 28 != 0: new_line += coda
        else:
            new_line += line[i]

    return new_line

def YaleCont(line: str) -> str:
    """
    ## YaleCont(line: str) -> str
    Yale transcription of Contemporary Korean
    """
    line = PUAtoUni(line)
    new_line = ''

    for i in range(len(line)):
        try:
            # /ㅜ/ after bilabial sound is transcribed as /u/;
            # Otherwise, /wu/.
            if line[i] == chr(0x116E):
                if i != 0 and line[i-1] in [chr(0x1106), chr(0x1107), chr(0x1108), chr(0x1111)]:
                    new_line = new_line + 'u'
                else:
                    new_line = new_line + dict_0_YALE[line[i]]
            else:
                new_line = new_line + dict_0_YALE[line[i]]
        except KeyError:
            new_line = new_line + line[i]
    
    return new_line

def YaleMid(line: str) -> str:
    """
    ## YaleMid(line: str) -> str
    Yale transcription of Middle Korean
    """
    line = PUAtoUni(line)
    new_line = ''

    for i in range(len(line)):
        try:
            if line[i] == chr(0x1172):
                new_line = new_line + 'ywu'
            else:
                new_line = new_line + dict_0_YALE[line[i]]
        except KeyError:
            new_line = new_line + line[i]

    
    new_line = new_line.replace('o', 'wo').replace('O', 'o')

    return new_line
