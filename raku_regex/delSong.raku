# @athor Yuan
# @data 2023-7-31 complete
# @target "对重复歌曲，比较大小，然后删除！"

sub search(@file)
{
    my $same_file = SetHash.new;
    my $tmp;
    while $tmp = @file.pop
    {

        if $tmp.basename.match(/<-[\.]>*/) ~~ / (<:Han + [、]>+ | \w*) \s[\-]\s ((<:Han>*) | \w.*)/
        # 匹配一个中文名字或者一个外文名字" - "匹配一个中文或者一个外文
        {
            #            say $tmp.basename.cache;

            if $1.chars < 2  { next;}
            for @file -> $i {
#                if $i.contains($0)
#                {
                    if $i.contains($1)
                    {
                        # say "if ......0...={$0},1...={$1},tmp...={$tmp}" ;
                        $same_file.set($i);
                        $same_file.set($tmp);
                    }
#                }
            }
        }
        else
        {
            # say "this is not match if condition valiable {$tmp}";
            # 经过前面的一折腾，这里可以不用要了
            # /\D\s?(.*)\s[\-]\s(.*)/ 匹配从非零非数值到最后一个空格为界限
            if $tmp.basename ~~ /\D\s?(.*)/
            {
                # say "else 0...={$0},tmp...={$tmp}";
                for @file -> $i {
                    if $i.contains($0)
                    {
                        $same_file.set($i);
                        $same_file.set($tmp);
                    }
                }
            }

        }

        # diff_delelte($same_file);bp add app:26


        next if $same_file.elems eq 0;

        my $item = $same_file.keys.max({
            $_.s if $_.e
        });

        say "save  {
            $item
        }";
        for $same_file.keys -> $k {

            next if $k eq $item;
            say  "delete {
                $k
            }";
            unlink $k;
        }

        $same_file = SetHash.new;
        # 这里一清空，就会导致上面循环筛选的元素重复
        say "............................................................................."

    }
}
sub MAIN($dir = '.') {
    my @todo = $dir.IO;
    my @file;
    while @todo {
        for @todo.pop.dir -> $path {
            if $path.d {
                @todo.push: $path;
            }
            else {
                @file.push: $path;
            }
        }
    }
    say @file.pop;
    say @file.pop;
    say "pop system file ##################################################################";
    # say @file.pop;
    search(@file);
}