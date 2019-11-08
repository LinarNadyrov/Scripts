
#!/usr/bin/perl

my $n_servers=3;
my $base_servername="aa"; #название сервера

my $config_name="/etc/haproxy/haproxy.cfg";
my $config_template="/etc/haproxy/haproxy.cfg.template";
my $log_file="/var/log/haproxy_weights";

# Для свободной памяти - по убфванию, для LA или нагрузки на CPU - по возрастанию
# 0 - сортировка по убыванию
# 1e+12 - сортировка по возрастанию
#my $orderFlag=1e+12;
my $orderFlag=1e+7;

sub getValue($)
{
 my $n=shift;
 my $cmd="zabbix_get -k 'net.tcp.service[http,,8080]' -s $base_servername$n.domain.ru 2>/dev/null";
 my $value=`$cmd`;
 return $orderFlag if length($value)==0 || $value==0;
 $cmd="zabbix_get -k 'system.cpu.load[percpu,avg5]' -s $base_servername$n.domain.ru 2>/dev/null";
 #$cmd="zabbix_get -k 'ct.memory.size[free]' -s $base_servername$n.domain.ru 2>/dev/null";
 $value=`$cmd`;
 $value=$orderFlag if length($value)==0;
 return $value;
}

my @values;

sub getOrder()
{
 my @arr;
 for (my $i=0,$j=0; $i<$n_servers; ++$i) {
  $arr[$i] = getValue($i+1);
 }
 @values=@arr;
 # Сортировка по убыванию
 my @b;
 if  ($orderFlag==0) {
  @b = sort { $b <=> $a } @arr;
 } else {
  @b = sort { $a <=> $b } @arr;
 }
 my @ret;
 for(my $i=0; $i<=$#arr; ++$i) {
  for (my $n=0; $n<=$#arr; ++$n) {
   if ($b[$i] == $arr[$n] && $arr[$n]>=0) {
    $ret[$j++] = $n+1;
    $arr[$n] = -1;
    break;
   }
  }
 }
 return @ret;
}

my $order;

sub saveLog()
{
 open(my $fh, '>>', $log_file) or die "Can't open log file [$!]\n";
 print $fh localtime()." order: ";
 for ($i=0; $i<$n_servers; ++$i) {
  print $fh "$base_servername".$order[$i]." ";
 }
 print $fh "; values: ";
 for ($i=0; $i<$n_servers; ++$i) {
  $values[$i] =~ s/\s//g;
  print $fh "$base_servername".($i+1)."=".($values[$i])." ";
 }
 print $fh "\n";
}

# Начало скрипта

@order = getOrder();

open(FILE, $config_template) or die "Can't read file [$!]\n";  
local $/;
$config = <FILE>; 
close (FILE);  

my $login="";
for (my $i=0; $i<$n_servers; $i++) {
 my $n = $order[$i];
 $login.="\t"."server $base_servername$n $base_servername$n.domain.ru:8080\n";
}

my $server="";
for (my $i=0; $i<$n_servers; $i++) {
 my $n = $order[$i];
 $server.="\t"."server $base_servername$n $base_servername$n.domain.ru:8080 cookie $base_servername$n\n";
}

$config =~ s/__login__/$login/g;
$config =~ s/__server__/$server/g;

my $tmp = "$config_name.tmp";
open(my $fh, '>', $tmp) or die "Не могу открыть '$tmp' $!";
print $fh $config;
close $fh;

if (system("diff -q $config_name $tmp >/dev/null 2>&1")) {
 rename($tmp, $config_name) or die "Не могу переименовать $tmp в $config_name: $!";
 system("systemctl reload haproxy || systemctl restart haproxy");
 saveLog();
} else {
 unlink($tmp);
}
