provider "local" {}

resource "local_file" "infra_note" {
  filename = "${path.module}/../k8s/cluster_setup.txt"
  content  = "Kubernetes Cluster Infrastructure verified via Terraform."
}

output "status" {
  value = "Infrastructure Provisioning Simulation Completed Successfully!"
}