#Execute a command

exec{'kill_killmenow_process' :
  command => 'pkill killmenow',
  unless  => 'pgrep killmenow',
}
