# installs puppet-lint package


package {'flask':
  ensure   => '3.0.3',
  name     => 'flask',
  provider => 'pip3'
}
