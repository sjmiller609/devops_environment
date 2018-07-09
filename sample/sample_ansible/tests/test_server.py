
import requests

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_service(host):
    ip_address = host.ansible.get_variables()["ansible_host"]
    response = requests.get("http://" + ip_address)
    assert "Automation for the People" in response.text
 
