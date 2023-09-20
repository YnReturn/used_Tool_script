sub MAIN($tmp) {
    $_ = $tmp;
    s:g/ <[\x[4e00] .. \x[9fa5]]>* //;    
    .say;             
}
# $_ = q{12r测四1221十四....};