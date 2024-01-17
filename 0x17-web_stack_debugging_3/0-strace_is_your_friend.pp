#corrected code -> bug fix

exec { 'Find bugs and fix':
    command => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
    provider => linux
}