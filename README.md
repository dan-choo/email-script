# Email Script

A quick, very hacky script to send grade estimations to students.

To get started, first make sure your umich email is approved for Authenticated
SMTP. You can get send a request here: https://documentation.its.umich.edu/authenticated-smtp

Next, make sure you have `python3` downloaded. Then download the grades spreadsheet as a `.csv`
file and rename it to `grades.csv` (or you can also just change the name in
the script itself).

The `email_script.txt` file is the template used for the email so feel free to edit that
however you want.

Then the command `python3 email_script.py` should be all you need to start running!
Note that there's no delay between sending the emails so I'm not too sure if it'll get
blocked. Maybe we need to send them in batches?


