# Install Flask from pip3

class flask {
  exec { 'install_flask':
    command  => 'pip3 install flask==2.1.0',
    creates  => '/usr/local/lib/python3/dist-packages/flask',
    path     => ['/usr/bin', '/usr/local/bin'],
    provider => shell,
    require  => Package['python3-pip'],
  }
}

# Ensure Python 3 pip package is installed
package { 'python3-pip':
ensure   => installed
}

