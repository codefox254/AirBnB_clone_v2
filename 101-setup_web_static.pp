class web_static_setup {
  package { 'nginx':
    ensure => installed,
  }

  file { '/data':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
    require => Package['nginx'],
  }

  file { '/data/web_static':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
    require => File['/data'],
  }

  file { '/data/web_static/releases':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
    require => File['/data/web_static'],
  }

  file { '/data/web_static/shared':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
    require => File['/data/web_static'],
  }

  file { '/data/web_static/releases/test':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
    require => File['/data/web_static/releases'],
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
    require => File['/data/web_static/releases/test'],
  }

  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    require => File['/data/web_static/releases/test'],
    force  => true,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx_default.erb'),
    notify  => Service['nginx'],
    require => Package['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

include web_static_setup

