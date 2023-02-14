in_lines = []
with open('input.txt', 'r') as file_in:
    in_lines = file_in.readlines()

in_lines.reverse()

def algo(in_lines):
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



        out_lines.append('Case #'+str(k+1)+': '+str(scoremin)+' '+str(scoremax))



    ### HERE ENDS THE ALGORITHM ###
    return out_lines

out_lines = algo(in_lines)
with open('output.txt', 'w') as file_out:
    file_out.writelines(out_lines)