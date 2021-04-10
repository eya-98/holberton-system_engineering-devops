#using Puppet to make changes to our configuration file
line { 'Turn off password':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true
}

line { 'Declare identity':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
  replace => true
}
