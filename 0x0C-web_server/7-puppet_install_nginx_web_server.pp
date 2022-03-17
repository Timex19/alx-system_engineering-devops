# Install Nginx web server using Puppet

exec {'nginx_install':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Holberton School" | sudo tee /var/www/html/index.html',
  provider => shell,
}
exec {'nginx_full':
  command  => 'sudo sed -i "30i \\\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=oavMtUWDBTM;\n}" /etc/nginx/sites-available/default ; sudo service nginx restart',
  provider => shell,
}
