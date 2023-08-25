# Ensure the puppetlabs-stdlib module
# Set the SSH client to use the private key ~/.ssh/school
include stdlib

file_line { 'Turn off authenticate using a password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Use private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}
