# AI Agent n8n Project Setup

This document provides the steps to complete and run the AI Agent n8n project.

## 1. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## 2. Run the FastAPI Backend

Run the FastAPI application using uvicorn:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## 3. Import the n8n Workflow

1.  Open your n8n instance.
2.  Go to **Workflows** and click on **New**.
3.  Click on **Import from file** and select the `workflow.json` file included in this project.

## 4. Configure the n8n Workflow

You need to configure the following nodes in your n8n workflow:

### Webhook

1.  Copy the **Test URL** from the Webhook node.
2.  Update the `n8n_webhook_url` variable in the `main.py` file with this URL.

### Google Sheets

1.  Create a new Google Sheet.
2.  Share the sheet with your n8n Google account.
3.  Update the **Sheet ID** in the Google Sheets node with the ID of your sheet.

### Email

1.  Configure the **Email** node with your email provider's SMTP settings.
2.  Update the **From Email** and **To Email** fields as needed.

## 5. Test the Application

1.  Open your web browser and go to `http://127.0.0.1:8000`.
2.  Enter your email and an article URL.
3.  Click on **Process Article**.

This will trigger the FastAPI backend, which will then trigger the n8n workflow. You should see the data in your Google Sheet and receive an email with the summary and insights.
