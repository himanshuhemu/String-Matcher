from timeit import default_timer as timer

#Functions are for search a pattern "pat" in a string "txt"

def NaiveSearch(pat, txt): 
    lst=[]
    start = timer() #Initial time
    M = len(pat) 
    N = len(txt) 
    i = 0
  
    while i <= N-M: 
        # For current index i, check for pattern match 
        for j in range(M): 
            if txt[i+j] != pat[j]: 
                break
            j += 1
  
        if j==M:    # if pat[0...M-1] = txt[i,i+1,...i+M-1] 
            lst.append(i)
            i = i + M 
        
        elif j==0: 
            i = i + 1
        else: 
            i = i+ j    # slide the pattern by j 
    end = timer()   #Final Time
    #print(end)
    tm=end-start
    t="%.8f"%tm
    #t=round(tm,6)
    return t,lst        

def RabinSearch(pat, txt): 
    start1 = timer()
    lst=[]
    q = 101 # A prime number 
    d = 256
    M,N = len(pat), len(txt) 
    i,j,h = 0,0,1
    p = 0    # hash value for pattern 
    t = 0    # hash value for txt
  
    # The value of h would be "pow(d, M-1)%q" 
    for i in range(M-1): 
        h = (h*d)%q 
  
    # Calculate the hash value of pattern and first window 
    # of text 
    for i in range(M): 
        p = (d*p + ord(pat[i]))%q 
        t = (d*t + ord(txt[i]))%q 
  
    # Slide the pattern over text one by one 
    for i in range(N-M+1): 
        # Check the hash values of current window of text and 
        # pattern if the hash values match then only check 
        # for characters on by one 
        if p==t: 
            # Check for characters one by one 
            for j in range(M): 
                if txt[i+j] != pat[j]: 
                    break
  
            j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] 
            if j==M: 
                lst.append(i) 
  
        # Calculate hash value for next window of text: Remove 
        # leading digit, add trailing digit 
        if i < N-M: 
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q 
  
            # We might get negative values of t, converting it to 
            # positive  
            if t < 0: 
                t += q 
    end1=timer()
    tim=end1-start1
    ntm="%.8f"%tim
    #ntm=round(tim,6)
    return ntm,lst
            

# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    start=timer()
    lst=[]
    M,N = len(pat),len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            print("Found pattern at index "+str(i-j))
            lst.append(str(i-j))
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    end=timer()
    tme=end-start
    rtme="%.8f"%tme
    return rtme,lst
     
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1
  
# Driver program to test the above functions
#txt = "ABCEABCDABCEABCD"
#pat = "ABCD"
#tm,lst=NaiveSearch(pat, txt)
#print(tm)
#print(lst) 
#q = 101 # A prime number 
#search(pat,txt) 
#KMPSearch(pat, txt) 
