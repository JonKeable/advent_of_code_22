#!/bin/awk -f
BEGIN {
    print "begin"
    depth = 0
    currDir = ""
    TOTAL_SPACE = 70000000
    SPACE_REQ = 30000000
}

{
    if ($1 == "$") {
        if ($2 == "cd") {
            ## i don't know why, but using == ".." didnt work! (or == anyting else, like "ee")
            if ($3 ~ /\.\./) {
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
    


    usedSpace = files["/"]
    print usedSpace
    remSpace = TOTAL_SPACE - usedSpace
    print ("current space: " TOTAL_SPACE " - " usedSpace " = " remSpace)
    spaceNeed = SPACE_REQ - remSpace
    print ("space needed: " SPACE_REQ " - " remSpace " = " spaceNeed)

    smallest = TOTAL_SPACE

    for (dir in files) {
        if (files[dir] >= spaceNeed && files[dir] < smallest) {
            smallest = files[dir]
            print files[dir]
        }
    }

    print ("smallest: " smallest)

}