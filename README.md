
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

---

## 🖼️ Example Output

- CSV file: 10,000 dart throws, circle test, and π estimate
- ✅ Uploaded to: `s3://your-bucket/monte_pi/results.csv`

---


