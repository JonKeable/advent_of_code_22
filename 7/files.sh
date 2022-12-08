#!/bin/awk -f
BEGIN {
    print "begin"
    depth = 0
    currDir = ""
    MAX_SIZE = 100000
}

{
    if ($1 == "$") {
        if ($2 == "cd") {
            print "change directory"
            ## i don't know why, but using == ".." didnt work! (or == anyting else, like "ee")
            if ($3 ~ /\.\./) {
                print "go up"
                delete dirDepths[depth]
                depth--
                currDir = dirDepths[depth]
            }
            else {
                # need this as some subdirs in different parent dirs have the same name, this was the source of issues
                if (currDir == "") {
                    currDir = $3
                }
                else {
                    currDir = (currDir "/" $3)
                }
                dirDepths[depth] = currDir
                depth++
                files[currDir]+=0
            }
        }
    }

    else if ($1 == "dir") {
    }

    #files
    else {
        for (d in dirDepths) {
            files[dirDepths[d]] += $1
        }
    }
}


END {


    print "end stuff"


    print "----------------"
    sum = 0
    for (dir in files) {

        if (files[dir] <= MAX_SIZE) {
            print "small nuff"
            sum += files[dir]
        }
        else {
            print "too big"
        }

    }

    print ("sum : " sum)
    print "end"
}