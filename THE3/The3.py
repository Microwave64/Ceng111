def rotation(pattern, I ,degree = 0):
    new_rotation = []
    row = int(len(pattern))
    coloum = int(len(pattern[0]))
    i = 0
    j = row - 1
    a = ""
    while i < coloum:
        while j >= 0:    
            a += (pattern[j][i])
            j -= 1
        j = row - 1
        i += 1 
        new_rotation.append(a)
        a = "" 
    degree += 90
    return helper_pattern_search(new_rotation, I, degree)
    

def helper_pattern_search(P, I, degree = 0):
    row_pattern = int(len(P))
    coloum_pattern = int(len(P[0]))
    row_image = int(len(I))
    coloum_image = int(len(I[0]))
    
    if row_pattern > row_image or coloum_pattern > coloum_image:
        if degree == 270:
            return False
        return rotation(P,I,degree)

    k = 0   #indexcoloumpattern
    l = 0   #indexrow_pattern
    i = 0   #indexcoloum_image
    j = 0   #indexrowimage

    while j < (row_image):
        while i < (coloum_image):
            if P[l][k] == I[j][i]:  
                if l == 0:
                    lastcoloum_of_firstrow = i
                    firstrow = j 
                k += 1
                i += 1 
                if k == coloum_pattern:
                    if l == (row_pattern - 1):
                        return ((j-l),(i-k),degree)
                    else:
                        l += 1
                        i -= coloum_pattern
                        k = 0
                        break
                elif i == coloum_image:
                    k = 0
                    l = 0
                    i = 0
                    break
            else:     
                i += 1
                if i == coloum_image:
                    k = 0
                    i = 0
                    l = 0
                    break
                elif l != 0:
                    k = 0
                    i = lastcoloum_of_firstrow - coloum_pattern + 2
                    j = firstrow       
                    l = 0       
                elif k != 0:
                    i -= 1
                    k = 0
        j += 1
    else:
        if degree == 270:
            return False
        return rotation(P,I,degree)

def pattern_search(P, I): 
    return helper_pattern_search(P, I)

