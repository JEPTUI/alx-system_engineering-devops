package { 'apache2':
  ensure => 'installed',
}
file { '/etc/apache2/conf.d/my_custom.conf':
  ensure  => 'file',
  content => "MyCustomConfigContent\n",
  require => Package['apache2'],
}
service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/apache2/conf.d/my_custom.conf'],
}
