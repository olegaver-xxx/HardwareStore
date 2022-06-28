sudo aa-status

# Shutdown apparmor and prevent it from restarting
sudo systemctl disable apparmor.service --now

# Unload AppArmor profiles
sudo service apparmor teardown

# Re-check AppArmor status
sudo aa-status

# Try to re-stop containers
docker-compose down
