output "instance_conn_details" {
  value = "ssh -i ${var.private_key_filename} ctfd@${aws_instance.ctfd_server.public_ip}"
}

output "ansible_conn_details " {
  value = terraform_data.ctfd_ansible.local-exec.command
}
