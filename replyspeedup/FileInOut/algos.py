# in_lines contains a reversed list of all the lines in the input file
def algo_1(in_lines):
    out_lines = []
    ### HERE STARTS THE ALGORITHM ###

    casecount = int(in_lines.pop())


    for i in range(casecount):

        gadgetcount = int(in_lines.pop())
        pregadgets = in_lines.pop().split()
        gadgets = []
        for j in range(len(pregadgets)):
            if not int(pregadgets[j]) in gadgets:
                gadgets.append(int(pregadgets[j]))


        smallest_num = min(gadgets)

        common_divs = []

        for j in range(smallest_num, 0, -1):
            success = True
            for k in gadgets:
                if k % j:
                    success = False
                    break
            if success:
                common_divs.append(j)

        out_lines.append('Case #' + str(i + 1) + ':' + str(len(common_divs)) + '\n')

    ### HERE ENDS THE ALGORITHM ###
    return out_lines


def algo_2(in_lines):
    out_lines = []

    ### HERE STARTS THE ALGORITHM ###
    # use out_lines.reverse(); out_lines.pop() instead of readline
    # dont forget to append '\n' on each line
    casecount = int(in_lines.pop())

    for k in range(casecount):
        settings = in_lines.pop().split()
        N = int(settings[0])
        D = int(settings[1])
        C = in_lines.pop().split()
        for i in range(len(C)):
            C[i] = int(C[i])

        current = [k for k in range(N)]

        for i in range(D):
            liste = [0 for x in range(N)]
            for j in range(N):
                liste[C[j]] = current[j]


            current = liste

        out_line = ''
        for i in current:


            out_line = out_line + ' ' + str(i)

        out_lines.append('Case #' + str(k + 1) + ':' + str(out_line)+'\n')

    print('finished')
    ### HERE ENDS THE ALGORITHM ###
    return out_lines

def algo_3(in_lines):
    out_lines = []

    ### HERE STARTS THE ALGORITHM ###
    # use out_lines.reverse(); out_lines.pop() instead of readline
    # dont forget to append '\n' on each line
    casecount = int(in_lines.pop())

    for k in range(casecount):
        settings = in_lines.pop().split()
        N = int(settings[0])
        K = int(settings[1])


        A = in_lines.pop().split()
        B = in_lines.pop().split()

        for i in range(len(A)):
            A[i] = int(A[i])

        for i in range(len(B)):
            B[i] = int(B[i])

        A.sort()
        B.sort()

        Amin = A[:K]
        Bmin = B[:K]

        Bmin.reverse()
        scoremin = 0
        for i in range(K):
            scoremin += Amin[i]*Bmin[i]

        A.reverse()
        B.reverse()

        Amax = A[:K]
        Bmax = B[:K]


        scoremax = 0
        for i in range(K):
            scoremax += Amax[i] * Bmax[i]



        out_lines.append('Case #'+str(k+1)+': '+str(scoremin)+' '+str(scoremax)+'\n')



    ### HERE ENDS THE ALGORITHM ###
    return out_lines