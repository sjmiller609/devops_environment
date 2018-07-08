
include_recipe "openssl::upgrade"
include_recipe 'nginx::repo'
include_recipe 'nginx::package'
