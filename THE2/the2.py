vertices_inputlist = eval(input())

x0 = vertices_inputlist[0][0]
x1 = vertices_inputlist[1][0]
x2 = vertices_inputlist[2][0]
x3 = vertices_inputlist[3][0]
y0 = vertices_inputlist[0][1]
y1 = vertices_inputlist[1][1]
y2 = vertices_inputlist[2][1]
y3 = vertices_inputlist[3][1]
if vertices_inputlist[0][1] < 0 or vertices_inputlist[2][1] < 0:
    backuplist = [(x0,-y0),(x1,-y1),(x2,-y2),(x3,-y3)]
    intermedite_points_list = [(x0,-y0),(x1,-y1),(x2,-y2),(x3,-y3)]
else:
    backuplist = [(x0,y0),(x1,y1),(x2,y2),(x3,y3)]
    intermedite_points_list = [(x0,y0),(x1,y1),(x2,y2),(x3,y3)]
a = 0
c = 1
b = 2 
d = 3

if (backuplist[a+1][0]) > (backuplist[a][0]):
    c = a
    a += 1
elif(backuplist[a+1][0]) == (backuplist[a][0]):
    if (backuplist[a+1][1]) < (backuplist[a][1]):
        c = a
        a+=1

if (backuplist[b+1][0]) > (backuplist[b][0]):
    d = b
    b += 1
elif(backuplist[b+1])[0] == (backuplist[b][0]):
    if (backuplist[b+1][1]) < (backuplist[b][1]):
        d = b
        b += 1

if (backuplist[a][0]) > (backuplist[b][0]):
    _furthestpoint = backuplist[a]
    _furthestvarible = a 
elif (backuplist[a][0]) ==  (backuplist[b][0]):
    if (backuplist[a][1]) <  (backuplist[b][1]):
        _furthestpoint = backuplist[a]
        _furthestvarible = a 
    else:
        _furthestpoint = backuplist[b]
        _furthestvarible = b
else:
    _furthestpoint = backuplist[b]
    _furthestvarible = b


if (backuplist[c][0]) < (backuplist[d][0]):
    _closestpoint = backuplist[c]
    _closestvarible = c
elif (backuplist[c][0]) == (backuplist[d][0]):
    if (backuplist[c][1]) <  (backuplist[d][1]):
        _closestpoint = backuplist[c]
        _closestvarible = c
    else:
        _closestpoint = backuplist[d] 
        _closestvarible = d 
else:
    _closestpoint = backuplist[d] 
    _closestvarible = d 



if _furthestvarible > _closestvarible:
    del intermedite_points_list[_furthestvarible]
    del intermedite_points_list[_closestvarible]
else:
    del intermedite_points_list[_closestvarible]
    del intermedite_points_list[_furthestvarible]



acrosspointvaribleof_furthest = (_furthestvarible + 2) % 4
acrosspointvaribleof_closest = (_closestvarible + 2) % 4
x_across_offurthest = backuplist[acrosspointvaribleof_furthest][0]
y_across_offurthest = backuplist[acrosspointvaribleof_furthest][1]
x_across_ofclosest = backuplist[acrosspointvaribleof_closest][0]
y_across_ofclosest = backuplist[acrosspointvaribleof_closest][1]

yclosest = _closestpoint[1]
yfurthest = _furthestpoint[1] 
xfurthest = _furthestpoint[0]
xclosest = _closestpoint[0] 

xintpoint0 = intermedite_points_list[0][0]
yintpoint0 = intermedite_points_list[0][1]
xintpoint1 = intermedite_points_list[1][0]
yintpoint1 = intermedite_points_list[1][1]

y0_izdusum = ((yfurthest - yclosest) / (xfurthest - xclosest)) * (xintpoint0 - xclosest) + yclosest 
y1_izdusum = ((yfurthest - yclosest) / (xfurthest - xclosest)) * (xintpoint1 - xclosest) + yclosest



if yintpoint0 < yintpoint1:
    lowyintpointy = yintpoint0 
    lowyintpointx = xintpoint0
elif yintpoint0 == yintpoint1:
    if yfurthest > yclosest:
        if xintpoint0 > xintpoint1:
            lowyintpointy = yintpoint0
            lowyintpointx = xintpoint0
        else:
            lowyintpointy = yintpoint1
            lowyintpointx = xintpoint1
    else:
        if xintpoint0 > xintpoint1:
            lowyintpointy = yintpoint1
            lowyintpointx = xintpoint1
        else:
            lowyintpointy = yintpoint0
            lowyintpointx = xintpoint0
else:
    lowyintpointy = yintpoint1
    lowyintpointx = xintpoint1



S1 = abs(x_across_offurthest * (yfurthest - yclosest) + xclosest * (y_across_offurthest - yfurthest) + xfurthest * (yclosest - y_across_offurthest )) + abs(x_across_offurthest * (yfurthest - y_across_ofclosest) + x_across_ofclosest * (y_across_offurthest - yfurthest) + xfurthest * (y_across_ofclosest - y_across_offurthest ))
S2 = abs(x_across_ofclosest * (yclosest - yfurthest) + xfurthest * (y_across_ofclosest - yclosest) + xclosest * (yfurthest - y_across_ofclosest )) + abs(x_across_ofclosest * (yclosest - y_across_offurthest) + x_across_offurthest * (y_across_ofclosest - yclosest) + xclosest * (y_across_offurthest - y_across_ofclosest )) 
if S1 < S2:
    xconcavepoint = x_across_offurthest
    yconcavepoint = y_across_offurthest
    xnotconcavepoint = x_across_ofclosest
    ynotconcavepoint = y_across_ofclosest
    Areaquadrilateral = S1 / 2
else:
    xconcavepoint = x_across_ofclosest
    yconcavepoint = y_across_ofclosest
    xnotconcavepoint = x_across_offurthest
    ynotconcavepoint = y_across_offurthest
    Areaquadrilateral = S2 / 2



if (yintpoint0 > y0_izdusum and yintpoint1 < y1_izdusum):
    Area = ((xintpoint1 - xclosest) * (yintpoint1 + yclosest) / 2) + ((xfurthest - xintpoint1) * (yintpoint1 + yfurthest) / 2)
    print("%.2f" % Area)
elif (yintpoint0 < y0_izdusum and yintpoint1 > y1_izdusum):
    Area = ((xintpoint0 - xclosest) * (yintpoint0 + yclosest) / 2) + ((xfurthest - xintpoint0) * (yintpoint0 + yfurthest) / 2)
    print("%.2f" % Area)
elif yintpoint0 > y0_izdusum and yintpoint1 > y1_izdusum:
    if ((_furthestvarible + 1) % 4) == _closestvarible or ((_furthestvarible - 1) % 4) == _closestvarible:
        Area = (yclosest + yfurthest) * (xfurthest - xclosest) / 2
        print("%.2f" % Area) 
    else:
        Area = ((lowyintpointy + yclosest) * (lowyintpointx - xclosest) + (yfurthest + lowyintpointy) * (xfurthest - lowyintpointx)) / 2
        print("%.2f" % Area)
else:
    if (_closestvarible + 1 ) % 4 != _furthestvarible and (_closestvarible - 1) % 4 != _furthestvarible :
        Area = ((lowyintpointy + yclosest) * (lowyintpointx - xclosest) + (yfurthest + lowyintpointy) * (xfurthest - lowyintpointx)) / 2
        print("%.2f" % Area)  
    else:
        Area = ((xfurthest - xclosest) * (yfurthest + yclosest) / 2) - Areaquadrilateral
        print("%.2f" % Area)
    
