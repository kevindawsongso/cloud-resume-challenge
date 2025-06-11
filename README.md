# 🌐 Kevin Dawson – Cloud Resume Challenge

Welcome! This is my completed version of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/), a hands-on cloud engineering project designed to showcase real-world skills across web development, serverless infrastructure, CI/CD automation, and cloud security.

This repository contains the full source code and automation behind my live resume website, deployed entirely on AWS with modern DevSecOps practices.

---

## ✅ What This Project Includes

- **Static Website** built with HTML, Tailwind CSS, and hosted on an Amazon S3 bucket.
- **HTTPS & CDN** via Amazon CloudFront for secure, global delivery.
- **Custom Domain** configured with Route 53 DNS and SSL.
- **Live Visitor Counter** using:
  - Amazon API Gateway
  - AWS Lambda (Python)
  - Amazon DynamoDB (on-demand mode)
- **Serverless Architecture** defined with AWS SAM (`template.yaml`).
- **CI/CD Pipelines** using GitHub Actions:
  - Frontend: S3 sync + CloudFront cache invalidation
  - Backend: SAM build and deploy on push
- **Secrets Management** via GitHub Secrets (no hardcoded credentials).

---

## 📂 Repository Structure

```
kevin-dawson-cloud-resume-challenge/
├── backend/                 # Lambda + SAM templates
│   ├── visitor_counter_lambda.py
│   └── template.yaml
├── frontend/                # HTML resume + styling
│   ├── index.html
│   ├── portfolio.html
│   └── ...
├── .github/workflows/       # GitHub Actions for CI/CD
│   ├── deploy-frontend.yml
│   └── deploy-backend.yml
└── samconfig.toml           # Local SAM config (safe for public repo)
```

---

## 🚀 How to Deploy

To deploy this project in your own AWS environment:

1. **Set up your AWS credentials locally** using named profiles or environment variables.
2. **Install dependencies:**
   - AWS CLI
   - AWS SAM CLI
   - Python 3.11+
   - GitHub CLI (optional)
3. **Backend Deployment:**

   ```bash
   cd backend
   sam build
   sam deploy --guided
   ```

4. **Frontend Deployment:**
   - Upload `frontend/` contents to your S3 bucket.
   - Invalidate CloudFront if necessary.

5. **CI/CD:**  
   Configure GitHub Secrets for:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION`
   - `S3_BUCKET_NAME`
   - `CLOUDFRONT_DISTRIBUTION_ID`

   The GitHub Actions will deploy automatically on push.

---

## 🎯 Skills Demonstrated

- CloudFormation + Infrastructure as Code
- Python + Serverless Lambda
- DynamoDB data modeling
- SAM CLI for build/deploy
- GitHub Actions workflows
- IAM permissions and least privilege
- CORS configuration and troubleshooting
- Debugging CI logs and deployment logs

---

## 🧠 Lessons Learned

This project pushed me to get hands-on with the full lifecycle of a serverless app: from design, build, and deploy, to debugging CI/CD issues and managing production resources. I gained deeper comfort with automation, cloud security, and identifying runtime mismatches across environments.

---

## 🔒 Security & Secrets

No sensitive keys or credentials are included in this repository. All authentication is handled securely through GitHub Actions secrets and IAM roles scoped to least privilege.

---

## 📫 Connect

Check out the live site [here](https://d3ax42r72scge7.cloudfront.net)  
Or connect with me on [LinkedIn](https://linkedin.com/in/kevin-dawson-gso)

---

Thank you for checking out my project! Feedback and collaboration are always welcome.
