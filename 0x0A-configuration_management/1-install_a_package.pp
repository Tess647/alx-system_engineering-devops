# installs puppet-lint package
require 'cgi'

package {'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
