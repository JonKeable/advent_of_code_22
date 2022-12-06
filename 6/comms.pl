use warnings;
use strict;

# my $filename = 'input.txt';
# my $k        = 4;

my ( $filename, $k ) = @ARGV;

## < for read
open FH, '<', $filename or die $!;

my @linelist = ();

while (<FH>) {
    push @linelist, $_;
}

my $txt = $linelist[0];
##print $txt;

for my $i ( 0 .. length($txt) - 1 ) {
    my $sub = substr( $txt, $i, $k );
    ## regex checks for matching char using back referencing of group
    if ( !( $sub =~ /(.).*?\1/ ) ) {
        my $loc = $i + $k;
        print "'$sub' found @ '$loc'\n";
        last;
    }
}

## print @linelist;
close FH;
