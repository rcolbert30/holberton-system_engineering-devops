# Using Puppet, create a manifest, kills process killmenow
exec { 'pkill killmenow':
path => ['/usr/bin']
}
