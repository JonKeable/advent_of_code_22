#!/bin/awk -f
BEGIN {
    print "begin";
}

{
    if ($1 == "$")    
    {
        print "control input";
    }

    else if ($1 == "dir")   
    {
        print "directory";
    }

    else
    {
        print "file";
    }
}


END {
    print "end";
}