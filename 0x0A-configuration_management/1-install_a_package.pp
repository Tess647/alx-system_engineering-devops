# Install puppet-lint version 2.5.0

package { 'Werkzeung':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}