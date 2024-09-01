# CTFd Server Builder

This is a simple Terraform / Vagrant configuration to launch an AWS or local Ubuntu server. The server is then provisioned with CTFd using the Ansible playbook.

It runs CTFd using Gunicorn and NGINX and installs a Lets Encrypt SSL certificate with certbot.

A security group on AWS allows only HTTP/S access and SSH from the public IP of the host running Terraform. The CTFd site will be unconfigured and require immediate setup. Alternatively you can import your own backup of a CTFd instance by placing ctfd_backup.zip in the root folder of the project.

As it is just used for short lived small team training, it is currently configured to use spot instances. Change the max spot price / instance type in terraform.tfvars.

### NOTES
- Comment out the certbot generation for testing so you don't trip the API limits for the same domain in a five day period.
- Don't forget to set your R53 zone identifier for DNS.
- You'll need python3, Ansible and AWS CLI working on the terraform host.

### TODO 

- [X] At the moment the Ansible playbook isn't idempotent as it generates a new service password for the Redis cache ACL and MariaDB root user on the fly. Need to migrate this password to Ansible vault.
  - Fixed. Implemented with the Python script `service_pass.py` for Ansible Vault and added idempotency with .my.cnf.
- [ ] Create a flag to use on-demand instance instead of spot should reliability be important.
- [ ] Modularise some of the TF config, such as key creation.
- [ ] Remove a few extra hardcoded parameters and replace with variables.
- [ ] Launch as a GitHub action?
- [ ] Add paramter to import a site backup on configuration:
```bash
cd /var/www/ctfd
source venv/bin/activate
python import.py ~/<BACKUP>.zip
sudo systemctl restart ctfd
```
