"""
Monte Carlo Simulation to Estimate π (Pi)

This script uses random sampling to estimate the value of π by simulating
points within a unit square and checking how many fall inside a quarter circle.
The results are saved to a CSV file and uploaded to an AWS S3 bucket.

"""

import numpy as np
import pandas as pd
import boto3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file (for AWS credentials and S3 bucket)
load_dotenv()

def estimate_pi(num_points=10000):
    """
    Estimate the value of π using Monte Carlo simulation.

    Parameters:
        num_points (int): Number of random points to generate.

    Returns:
        pi_estimate (float): The estimated value of π.
        x (np.ndarray): Array of x coordinates.
        y (np.ndarray): Array of y coordinates.
        inside_circle (np.ndarray): Boolean mask indicating if a point falls inside the unit circle.
    """
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    inside_circle = x**2 + y**2 <= 1
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    return pi_estimate, x, y, inside_circle

def save_results_to_csv(x, y, inside_circle, pi_estimate):
    """
    Save the simulation results to a CSV file.

    Parameters:
        x (np.ndarray): Array of x coordinates.
        y (np.ndarray): Array of y coordinates.
        inside_circle (np.ndarray): Boolean mask indicating if a point is inside the circle.
        pi_estimate (float): The estimated value of π.

    Returns:
        file_path (str): The file path to the saved CSV file.
    """
    df = pd.DataFrame({
        "x": x,
        "y": y,
        "inside_circle": inside_circle
    })
    df["pi_estimate"] = pi_estimate
    file_path = "results.csv"
    df.to_csv(file_path, index=False)
    return file_path

def upload_to_s3(file_path):
    """
    Upload the CSV file to a specified S3 bucket.

    Parameters:
        file_path (str): The local file path to upload.
    """
    bucket = os.getenv("S3_BUCKET_NAME")
    s3_key = "monte_pi/results.csv"
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket, s3_key)
    print(f"✅ Uploaded {file_path} to s3://{bucket}/{s3_key}")

def main():
    """
    Run the full simulation, save results, and upload them to S3.
    """
    print("🎯 Estimating π the Joker way...")
    pi, x, y, mask = estimate_pi()
    print(f"🎲 Estimated π ≈ {pi}")
    path = save_results_to_csv(x, y, mask, pi)
    upload_to_s3(path)

if __name__ == "__main__":
    main()
