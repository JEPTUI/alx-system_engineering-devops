class ssh_client_config {
  file { '/etc/ssh/100-puppet_ssh_config':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('100-puppet_ssh_config/ssh_config.erb'),
  }
}
