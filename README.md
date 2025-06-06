
# 🃏 Monte Pi Joker

Estimate π (pi) the clowny way using a Monte Carlo simulation!  
This mini pipeline uses Python, NumPy, and Pandas to simulate dart throws, estimate π, and upload the results to an AWS S3 bucket. Fully Dockerized for fun and portability.

---

## 🎯 Project Overview

We simulate throwing random darts at a square target with a quarter circle inside. By calculating how many darts land inside the circle, we estimate the value of π.

The results are:
- Saved locally as a CSV
- Uploaded to an S3 bucket of your choice

---

## 🧠 How It Works

1. Generate 10,000 random `(x, y)` coordinates
2. Count how many fall inside the quarter circle
3. Estimate π using:  
   \[
   \pi \approx 4 \cdot \frac{\text{# points inside circle}}{\text{total points}}
   \]
4. Save all data to `results.csv`
5. Upload `results.csv` to your configured AWS S3 bucket

---

## 📦 Tech Stack

- 🐍 Python 3.11
- 🔢 NumPy & Pandas
- ☁️ AWS S3 via `boto3`
- 🐳 Docker (for containerized execution)
- 🧪 dotenv for secret key handling

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-username/monte-pi-joker.git
cd monte-pi-joker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_DEFAULT_REGION=your-region
S3_BUCKET_NAME=your-s3-bucket-name
```

### 4. Run the script

```bash
python main.py
```

### 5. Run with Docker (Optional)

```bash
chmod +x run.sh
./run.sh
```
## ▶️ Quickstart for Reviewers (GitHub Codespaces)

This project runs end-to-end inside GitHub Codespaces — no local setup required.

It demonstrates:
- Monte Carlo simulation of π (pi)
- Data analysis with Pandas
- Upload to AWS S3
- Docker compatibility

### 🔧 Instructions

```bash
# ✅ STEP 1: Launch Codespace
# - Click the green “Code” button on this repository
# - Open a Codespace from the “Codespaces” tab

# ✅ STEP 2: Confirm you're in the project directory
ls
# You should see: main.py, requirements.txt, run.sh, etc.

# ✅ STEP 3: Install Python dependencies
pip install -r requirements.txt

# ✅ STEP 4: Add AWS credentials to `.env`
touch .env
# Paste the following into the file:
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_DEFAULT_REGION=your-region
S3_BUCKET_NAME=your-s3-bucket-name

# ✅ STEP 5: Run the pipeline
python main.py

# ✅ STEP 6 (Optional): Run it via Docker
chmod +x run.sh
./run.sh
```

---

## 🖼️ Example Output

- CSV file: 10,000 dart throws, circle test, and π estimate  
- ✅ Uploaded to: `s3://your-bucket/monte_pi/results.csv`

---
