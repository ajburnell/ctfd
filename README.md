# CTFd Server Builder

This is a simple Terraform / Vagrant configuration to launch an AWS or local Ubuntu server. The server is then provisioned with CTFd using the Ansible playbook.

It runs CTFd using Gunicorn and NGINX and installs a Lets Encrypt SSL certificate with certbot.

As it is just used for short lived small team training, it is currently configured to use spot instances.

Amend configurations as required in `variables.tf` and `ctfd_external_vars.yml`.

### NOTES
- Comment out the certbot generation for testing so you don't trip the API limits for the same domain in a five day period.
- Don't forget to set your R53 zone identifier for DNS.

### TODO 

-[] At the moment the Ansible playbook isn't idempotent as it generates a new service password for the Redis cache ACL and MariaDB root user on the fly. Need to migrate this password to Ansible vault.
-[] Create a flag to use on-demand instance instead of spot should reliability be important.
-[] Modularise some of the TF config, such as key creation.
-[] Remove a few extra hardcoded parameters and replace with variables.
-[] Launch as a GitHub action?
-[] Add paramter to import a site backup on configuration:
```bash
cd /var/www/ctfd
source venv/bin/activate
python import.py ~/<BACKUP>.zip
sudo systemctl restart ctfd
```
