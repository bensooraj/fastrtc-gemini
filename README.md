# FastRTC And Gemini Demo

## Features

1. FastRTC for real-time audio communication
2. Google Gemini for LLM brain

![FastRTC Gemini](demo.png)

## Project Structure

```bash
.
├── README.md
├── demo.png
├── iac
│   ├── fastrtc-v1-pkey.pem
│   ├── main.tf
│   ├── outputs.tf
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   ├── terraform.tfvars
│   ├── user_data
│   │   ├── fastrtc.service
│   │   └── user_data.sh.tftpl
│   └── variables.tf
├── pyproject.toml
├── src
│   └── fastrtc_gemini
│       ├── __init__.py
│       └── main.py
└── uv.lock
```

## Getting Started

### Prerequisites

* Python 3.11+
* Node v22.19.0 (LTS)
* uv for dependency management
* Terraform >= 1.4
* AWS account and credentials

### Setup

### 1. Clone the repository

```sh
git clone https://github.com/bensooraj/fastrtc-gemini.git
cd fastrtc-gemini
```

#### 2. **Create and activate a virtual environment:**

   ```bash
   uv venv
   ```

#### 3. **Install dependencies:**

   ```bash
   uv sync --frozen --no-cache
   ```

#### 4. **Configure AWS credentials:**

* Set up your AWS credentials (e.g., via `aws configure` or environment variables).

### Running Locally

#### 1. **Start the FastAPI development server:**

   ```bash
   uv run fastrtc-gemini
   ```

#### 2. **Access the app:**

* Open [http://127.0.0.1:7860](http://127.0.0.1:7860/) in your browser.

### Deploying to AWS

#### 0. **Configure AWS Credentials**

##### Option 1: Set AWS environment variables

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."
```

##### Option 2: Add a profile to your AWS credentials file

Copy and paste the following text in your AWS credentials file (`~/.aws/credentials`)

```bash
[profile-dev]
aws_access_key_id=...
aws_secret_access_key=...
aws_session_token=...
```

#### 1. **Initialize Terraform:**

   ```bash
   cd iac
   terraform init
   ```

#### 2. **Apply Terraform configuration:**

   ```bash
   terraform apply
   ```

* This will provision the AWS infrastructure and deploy the FastAPI app.

## Customization

* Update `iac/variables.tf` variables for your AWS region, instance type, and GitHub repo URL.

## Useful Scripts

```bash
# For listing all terraform resources
terraform show -json | jq -c '.values.root_module.resources[] | .address + " " + .values.id' -r\n
```
