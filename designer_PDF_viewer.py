# Hackerrank Question Link : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true

# Solution 
def designerPdfViewer(h, word):
    h_dict = {}
    temp = []
    for i in range(26):
        letter = chr(97+i)
        h_dict[letter] = h[i]
        
    for char in word:
        temp.append(h_dict[char])
    
    h_max = max(temp)
    
    return (h_max*len(word))
