# Python Email Sender

The Python Email Sender is a Python script that allows you to send emails to a list of recipients using Gmail's SMTP server. It validates email addresses, reads recipient emails from a column in a CSV file, and sends an emails to each recipient.

## Prerequisites

Before running the Python Email Sender script, make sure you have the following:

- Python 3.x installed
- The required Python libraries: `pandas`

## Installation

1. Clone the repository or download the script file.
2. Install the necessary dependencies by running the following command:

   ```shell
   pip install pandas
   ```

## Usage

1. Open the script file, and make sure to replace the following variables with your own details:
    **make sure you have two factor verification enabled**
   - `sender`: Your Gmail account email address.
   - `password`: Your Gmail account [App Password]
   - `csv_path`: The path to the CSV file containing the recipient email addresses in a column.
   - `subject_line`: The subject line for the email.
   - `body`: The content of the email.

2. Optionally, you can varify email to check if they are correct

3. Save the changes to the script file.

4. Run the Python script by executing the following command:

   ```shell
   python Mass_mail_sender.py
   ```

   The script will validate the email addresses, read the recipient list from the specified CSV file, and send individualized emails to each recipient.

## CSV File Format

The CSV file should have a column that contains the recipient email addresses. The script will read the email addresses from this column and send emails to each recipient.

Here is an example of the CSV file format:

```
EMAIL_ADDR
gsmith123@example.com
jdoe456@example.com
lwilliams789@example.com
akim321@example.com
bharris654@example.com
```

## Email Validation

The script includes an email validation function that checks the validity of each email address. It uses regular expressions to match the email pattern. If an invalid email address is found, the script will display a message indicating which email address is invalid and exit the program.

## License

MIT


## Contributions

pass

## Contact

Check my linkedin
