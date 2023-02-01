# Start cluster
sudo kubeadm init --pod-network-cidr 10.0.1.0/24 --apiserver-advertise-address 10.0.1.52

# Install CNI
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml