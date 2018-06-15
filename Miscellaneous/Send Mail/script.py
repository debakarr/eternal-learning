import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from email.mime.text import MIMEText
import mimetypes

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/gmail.readonly', 'https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/gmail.compose', 'https://www.googleapis.com/auth/gmail.send']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('client_secret_2.json', scope)
		creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

####################################################################

# change 'Your Spreadsheet Name'
sheet = client.open('Your Spreadsheet Name').sheet1


####################################################################

def SendMessage(service, user_id, message):
	"""Send an email message.

	Args:
		service: Authorized Gmail API service instance.
		user_id: User's email address. The special value "me"
		can be used to indicate the authenticated user.
		message: Message to be sent.

	Returns:
		Sent Message.
	"""
	try:
		message = (service.users().messages().send(userId=user_id, body=message)
							 .execute())
		print('Message Id: %s' % message['id'])
		return message
	except errors.HttpError as error:
		print('An error occurred: %s' % error)

####################################################################

def CreateMessage(sender, to, subject, message_text):
	"""Create a message for an email.

	Args:
		sender: Email address of the sender.
		to: Email address of the receiver.
		subject: The subject of the email message.
		message_text: The text of the email message.

	Returns:
		An object containing a base64url encoded email object.
	"""
	message = MIMEText(message_text, 'html')
	message['to'] = to
	message['from'] = sender
	message['subject'] = subject
	return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

# Loop to iterate through all cell and send mail if email id is avialable
for i in range(2, 5):
	result = sheet.row_values(i) # get whole row
	# if email field is not null
	if result[5] != '':
		roll = result[1]
		name = result[2]
		dept = result[3]
		contact_no = result[4]
		email_id = result[5]
		alternate_email_id = result[6]
		tenth_board = result[7]
		tenth_percent = result[8]
		tenth_yop = result[9]
		twelveth_board = result[10]
		twelveth_percent = result[11]
		twelveth_yop = result[12]
		sem1 = result[13]
		sem2 = result[14]
		sem3 = result[15]
		sem4 = result[16]
		sem5 = result[17]
		sem6 = result[18]
		sem7 = result[19]
		sem8 = result[20]
		cgpa = result[21]
		academic_year_gap = result[22]
		current_backlog = result[23]
		diploma_marks = result[24]
		diploma_yop = result[25]
		city_town = result[26]
		gender = result[27]
		dob = result[28]
		cv_link = result[29]
		cv_text = 'Click Here'
		
		# if CV Link field is null
		if cv_link == '':
			cv_text = '''<p><em><span style="color: rgb(184, 49, 47);">No record available</span></em> (<strong>doesn&#39;t mean you haven&#39;t submitted</strong>).&nbsp;</p>
			<p>It is most likely that <em>I do not have any details of your CV with me right now</em>.</p>
			<p>If you have submitted it to your coordinator then <strong>please contact him/her to verify the details</strong>. If you have already verified the details, then it&#39;s OK.</p>
			<p>If you <strong>haven&#39;t submitted your CV yet</strong>, then please do so by <strong>11:59 PM 15th June 2018</strong>.</p>
			'''

		# mesage to be send
		toSend = f'''<p>Hi {name},</p>
		<p>&nbsp;&nbsp;</p>
		<p><span style="font-family: Georgia,serif;">Here&#39;s an updated detail you provided (maybe some update in spreadsheet or you have submitted your CV):</span></p>		<p><span style="font-family: Georgia,serif;"><strong>Details</strong>:</span></p>
		<p>&nbsp;</p>
		<table dir="ltr" border="1" cellspacing="0" cellpadding="0"><colgroup><col width="121" /><col width="164" /></colgroup>
		<tbody>
		<tr>
		<td data-sheets-ischild=""><strong>ROLL</strong></td>
		<td>{roll}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>NAME</strong></td>
		<td>{name}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>DEPT</strong></td>
		<td>{dept}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>CONTACT NO.</strong></td>
		<td>{contact_no}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>EMAIL ID</strong></td>
		<td>{email_id}</td>
		</tr>
		<tr>
		<td data-sheets-ischild="">
		<div>
		<div><strong>ALTERNATE EMAIL ID</strong></div>
		</div>
		</td>
		<td>{alternate_email_id}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>10TH BOARD</strong></td>
		<td>{tenth_board}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>10TH MARKS (%)</strong></td>
		<td>{tenth_percent}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>10TH YOP</strong></td>
		<td>{tenth_yop}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>12TH BOARD</strong></td>
		<td>{twelveth_board}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>12TH MARKS(%)</strong></td>
		<td>{twelveth_percent}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>12TH YOP</strong></td>
		<td>{twelveth_yop}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>SEM1</strong></td>
		<td>{sem1}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>SEM2</strong></td>
		<td>{sem2}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>SEM3</strong></td>
		<td>{sem3}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>SEM4</strong></td>
		<td>{sem4}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>SEM5</strong></td>
		<td>{sem5}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>SEM6</strong></td>
		<td>{sem6}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>SEM 7</strong></td>
		<td>{sem7}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>SEM 8</strong></td>
		<td>{sem8}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>CGPA</strong></td>
		<td>{cgpa}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild="">
		<div>
		<div><strong>ACADEMIC YEAR GAP</strong></div>
		</div>
		</td>
		<td>{academic_year_gap}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild="">
		<div>
		<div><strong>CURRENT BACKLOG (IN NUMBER)</strong></div>
		</div>
		</td>
		<td>{current_backlog}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild="">
		<div>
		<div><strong>DIPLOMA MARKS(%)</strong></div>
		</div>
		</td>
		<td>{diploma_marks}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>DIPLOMA YOP</strong></td>
		<td>{diploma_yop}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>CITY/TOWN</strong></td>
		<td>{city_town}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>GENDER (M/F)</strong></td>
		<td>{gender}</td>
		</tr>
		<tr>
		<td  data-sheets-ischild=""><strong>DOB (DD-MM-YY)</strong></td>
		<td>{dob}</td>
		</tr>
		<tr>
		<td data-sheets-ischild=""><strong>CV Link</strong></td>
		<td><a href="{cv_link}">{cv_text}</a></td>
		</tr>
		</tbody>
		</table>
		<p>&nbsp;</p>
		<p><span style="color: #ff0000; font-family: Georgia, serif;"><sub>NOTE: This mail is automatically forwarded to everyone seperately, using the script I created (Google Sheets + Gmail API + Python). Your details are not forwarded to anyone else. If you find any problem in the format of the mail then feel free to contact me.</sub></span></p>
		<p><span style="font-family: Georgia, serif;"><strong>Thanks & Regards,</strong></span></p>
		<p><span style="font-family: Georgia, serif;"><strong>Debakar Roy</strong></span></p>
		<p>&nbsp;</p>
		'''

		# send after encoding to base64urlcode
		msg = CreateMessage(sender='me', to=email_id, subject='Your details are updated. Check Your details for CSE 2019 Passout Batch Database', message_text=toSend)
		SendMessage(service, user_id='me', message=msg)

		# display message whether sent is successful or not
		print('Email sent to', name)
		print('===============================================================')
	else:
		print('Email ID not available for ', result[2])
		print('===============================================================')
