output "instance_conn_details" {
  value = "ssh -i ${var.private_key_filename} ctfd@${aws_instance.ctfd_server.public_ip}"
}