#!/bin/awk -f
BEGIN {
    print "begin"
    depth = 0
    currDir = ""
    MAX_SIZE = 100000
}

{
    if ($1 == "$") {
        #print "control input";
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
                #print $3
                # need this as some subdirs in different parent dirs have the same name, this was the source of issues
                currDir = (currDir "/" $3)
                #print currDir
                dirDepths[depth] = currDir
                depth++
                files[currDir]+=0
            }
        }
    }

    else if ($1 == "dir") {
        #print "directory";

    }

    #files
    else {
        #print "file"
        #print $1
        #print "-----#-----"
        for (d in dirDepths) {
            #print "....."
            #print d
            #print dirDepths[d]
            #print files[dirDepths[d]]
            files[dirDepths[d]] += $1
            #print files[dirDepths[d]]
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
        #print dir
        #print files[dir]
        #print ""
    }

    print ("sum : " sum)
    print "end"

    print files["dtmbp"]
}