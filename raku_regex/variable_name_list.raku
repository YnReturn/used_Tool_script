my $fh = open "/mnt/d/Web_code/JTbox/src/var.ts", :r;
my $contents = $fh.slurp;
$fh.close;
$contents ~~ m:global/:r <(\S+ \s*)> '=' \s* \S*/;
print $/.words.join(",");