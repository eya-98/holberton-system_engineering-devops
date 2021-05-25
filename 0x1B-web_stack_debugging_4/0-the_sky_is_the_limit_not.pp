#  we are testing how well our web server setup featuring Nginx is doing under pressure 
exec { 'change':
    command => 'echo "ULIMIT=\"-n 2000\"" > /etc/default/nginx && /etc/init.d/nginx restart',
    path    => '/usr/local/bin/:/bin/',
}
