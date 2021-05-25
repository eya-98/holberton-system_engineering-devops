# Change the OS configuration so that it is possible to login with the holberton use
exec{ 'change configuration':
    command => 'echo "" > /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/',
}
