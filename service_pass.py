import secrets
import subprocess

password_length = 16

# Generate a vault password and the Redis / MariaDB suser passwords.
vault_password = secrets.token_urlsafe(password_length)
service_password = secrets.token_urlsafe(password_length)

# Write the vault password to file to be used by Ansible
f = open("vault_password", "w")
f.write (vault_password)
f.close()

# Add the service password to a vault
ansible_vault = subprocess.run(["ansible-vault", "encrypt_string", "--vault-password-file", "vault_password", service_password, "--name", "vault_service_password", "--output", "host_vars/vault"])
