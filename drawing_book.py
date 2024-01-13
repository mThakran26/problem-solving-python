# Hackerrank Question Link : https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

# Solution:
def pageCount(n, p):
    pages = []
    for i in range(0, n+1, 2):
        pages.append([i, i+1])
        
    for page in pages:
        if p in page:
            front = pages.index(page)
    
    back = len(pages) - front -1
    return (min(back, front))