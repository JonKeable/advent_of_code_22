use warnings;
use strict;

my $filename = 'input.txt';

## < for read
open FH, '<', $filename or die $!;

my @linelist = ();
my $k        = 4;

while (<FH>) {
    push @linelist, $_;
}

my $txt = $linelist[0];
##print $txt;

for my $i ( 0 .. length($txt) - 1 ) {
    my $sub = substr( $txt, $i, $k );
    ## print "Index: $i, Text: $four \n";
    if ( !( $sub =~ /(.).*?\1/ ) ) {
        print "'$sub' repeated @ '$i'\n";
        last;
    }
}

## print @linelist;
close FH;
