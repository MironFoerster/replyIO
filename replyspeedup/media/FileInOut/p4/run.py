for t in range(int(in_lines.pop())):    ax=[]    ay=[]    aa=[]    aminx=[]    amaxx=[]    aminy=[]    amaxy=[]    lx=[]    ly=[]    lc=[]    lxo=[]    lyo=[]    lco=[]    lao=[]    la=[]    N, C, Q = map(int, in_lines.pop().split(" "))    for q in range(Q):        x, y, c = in_lines.pop().split(" ")        x = int(x)        y = int(y)        if c == "A":            ax.append(x)            ay.append(y)        else:            lxo.append(x)            lyo.append(y)            lco.append(c)    for l in range(Q-len(ax)):        lao.append(0)    for k in range(len(ax)):        xmin=xmax=ax[k]        ymin=ymax=ay[k]        lx=lxo        ly=lyo        la=lao        lc=lco        for i in range (C-1):            deltax=xmax-xmin+1            deltay=ymax-ymin+1            for j in range (len(lx)):                if lx[j]<xmin:                    u=xmax-lx[j]+1                elif lx[j]>xmax:                    u=lx[j]-xmin+1                else:                    u=deltax                if ly[j]<ymin:                    v=ymax-ly[j]+1                elif ly[j]>ymax:                    v=ly[j]-ymin+1                else:                    v=deltay                #print(u*v)                la[j]=u*v            #print("la=",la)            amin=min(la)            print(amin)            print(la)            print(lx)            g=la.index(amin)            print(g)            ix=lx[g]            if ix<xmin:                xmin=ix            elif ix>xmax:                xmax=ix            #print("g",g)            iy=ly[g]            if iy<ymin:                ymin=iy            elif iy>ymax:                ymax=iy            colour=lc[g]            lxn, lyn, lan, lcn = [], [], [], []            cis=0            for h in lc:                if not h==colour:                    lxn.append(lx[cis])                    lyn.append(ly[cis])                    lan.append(0)                    lcn.append(h)                cis+=1            lx, ly, la, lc = lxn, lyn, lan, lcn        aa.append(amin)        aminx.append(xmin)        amaxx.append(xmax)        aminy.append(ymin)        amaxy.append(ymax)        #print(xmin,ymin,xmax,ymax,amin)    s=aa.index(min(aa))    #print(aminx[s],aminy[s],amaxx[s],amaxy[s],aa[s])    out_lines.append("Case #"+str(t+1)+": "+" ".join(str(i) for i in [aminx[s],aminy[s],amaxx[s],amaxy[s],aa[s]])+"\n")