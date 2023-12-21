#Configure SSH client to use the specified private key

include stdlib

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^#?(\s*IdentityFile\s+~/.ssh/school)',
  after   => '# This is the ssh client system-wide configuration file.  See',
}

# Configure SSH client to refuse password authentication
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  match   => '^#?(\s*PasswordAuthentication\s+yes)',
  after   => '# This is the ssh client system-wide configuration file.  See',
}