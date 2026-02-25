# Image Automation System

## Live Deployment
The application is deployed and accessible at:

Live URL:
http://127.0.0.1:5000

# Project Description
Image Automation System is a web-based image processing application that executes a fully automated backend pipeline.

Users can:

+ Provide a search keyword
+ Select the number of images to retrieve
+ Enter an email address to receive the output

Once submitted, the application performs the complete workflow automatically in the background without blocking the main server thread.

## What the System Does:

- After receiving user input, the application:
- Retrieves images based on the provided keyword
- Resizes each image to 256 × 256 pixels
- Converts images into grayscale format
- Packages the processed images into a ZIP archive
- Emails the ZIP file to the user using the SendGrid API

The entire pipeline is executed asynchronously to ensure smooth user experience.

# Technology Stack

The project is built using:

- Python
- Flask (Web Framework)
- Gunicorn (Production WSGI Server)
- icrawler (Bing Image Crawler)
- Pillow (Image Processing Library)
- SendGrid Email API
- Railway (Cloud Hosting Platform)
- python-dotenv (Environment Variable Handling)

# Directory Structure

```
Image_automation/
│
├── templates/
│   └── index.html
│
├── raw_data/        # Downloaded original images
├── final_images/    # Processed grayscale images
├── archives/        # Generated ZIP files
│
├── app.py
├── pipeline.py
├── Procfile
├── requirements.txt
├── .env
└── README.md
```

# Pipeline Workflow

1) The user submits a form containing:
   - Search keyword
   - Number of images
   - Email address
2) A background thread is initiated to execute the processing pipeline:
   - Required directories are created if missing
   - Previous execution data is cleared
   - Images are downloaded using BingImageCrawler
   - Each image is resized to 256 × 256 pixels
   - Images are converted to grayscale
   - Processed files are stored separately
   - A timestamp-based ZIP archive is generated
3) The ZIP file is encoded using Base64.
4) The SendGrid API delivers the archive to the specified email address.

# Design Considerations

- Background threading prevents request blocking.
- Automatic directory cleanup ensures consistent execution.
- Environment variables protect sensitive API credentials.
- Timestamped filenames prevent file overwriting.
- Exception handling ensures corrupted images do not crash the pipeline.
- Base64 encoding allows seamless attachment handling via email API.

# Potential Enhancements

- Integrate a task queue system such as Celery or RQ
- Implement real-time progress tracking
- Introduce user authentication and dashboard
- Apply rate limiting mechanisms
- Replace web scraping with official image search APIs
- Provide dynamic frontend status updates

# Author

Manavjot Singh
COPC – Third Year
