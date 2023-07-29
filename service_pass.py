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

f = open("./group_vars/ctfd/vault.yml", "w")
f.write("service_pass: \"" + service_password + "\"")
f.close()

# Add the service password to a vault
ansible_vault = subprocess.run(["ansible-vault", "encrypt", "--vault-password-file", "vault_password", "./group_vars/ctfd/vault.yml"])
