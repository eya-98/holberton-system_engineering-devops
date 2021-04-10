#using Puppet to make changes to our configuration file
file {'refuse to authenticate using a password' :
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no'
}

file { 'use the private key':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/holberton'
}

