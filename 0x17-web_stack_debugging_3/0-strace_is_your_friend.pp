#Wordpress debugging

exec { 'error conf php':
  provider => 'shell',
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}