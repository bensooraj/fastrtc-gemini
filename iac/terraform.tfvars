# --- Required/commonly changed ---
region          = "us-east-1"
name            = "fastrtc-gemini"
instance_type   = "t3.xlarge"
github_repo_url = "https://github.com/bensooraj/fastrtc-gemini.git"

# --- Optional: enable SSH access (comment out or set to "" to disable) ---
# Use your real public key and your public IP in CIDR form.
ssh_key_name = "fastrtc-v1-pkey"
# ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMockKeyGoesHere1234567890ABCDEFG your_email@example.com"
# ssh_cidr       = "203.0.113.10/32"
