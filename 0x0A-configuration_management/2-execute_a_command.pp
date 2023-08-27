#Execute a command

exec{'kill_killmenow_process' :
  path    => '/bin/',
  command => 'pkill killmenow',
  unless  => 'pgrep killmenow'
}
