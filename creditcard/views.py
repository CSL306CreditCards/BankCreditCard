
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from BankCreditCard.creditcard.models import User, Card, Statement, BankDetail, EmploymentDetail, PersonalDetail, Autopay
import random, datetime
import urllib
	
def maxCreditLimit(card_type):
	"""
	Function is used to determine the maximum credit limit of a credit card given the type of card.
	Arguments:
	 card_type -- Type of the card
	 
	 Returns: Maximum limit of the credit card
	"""
	if(card_type == 'Platinum'):
		return 100000
	elif(card_type == 'Gold'):
		return 50000
	elif(card_type == 'Silver'):
		return 20000	

def interest(card_type):
	"""
	Function is used to determine the maximum credit limit of a credit card given the type of card.
	Arguments:
	 card_type -- Type of the card
	 
	 Returns: Interest of credit card
	"""
	if(card_type == 'Platinum'):
		return 10
	elif(card_type == 'Gold'):
		return 5
	elif(card_type == 'Silver'):
		return 

def paymentApi(request, account_no, amount):
	return render_to_response('api/payment_api.html', {'account_no':account_no, 'amount':amount}, context_instance=RequestContext(request))
	
def successpaymentApi(request, account_no, amount):
	"""
	
	"""
	name = request.POST['NAME']
	
	password = request.POST['PASSWORD']
	card_number = request.POST['CARD_NUMBER']
	#expiry_date = request.POST['EXPIRY_DATE']
	#description = request.POST['description']
	#authentication and transfer
	payToAccount(name, password, card_number, account_no, "test", amount)
	return render_to_response('api/successpayment_api.html')

def adminInterest():
	for user in User.objects.get():
		amount = autopay.amount
		interest = interest(user.card.card_type)
		user.card.credited_amount += float(interest)
		user.card.save()		
		date = datetime.datetime.now()
		generateStatement(user.card, date, amount, 'Interest')

def adminAutoPay():
	for user in User.objects.get():
		for autopay in user.autopay_set.all():
			if (autopay.date == datetime.datetime.now()):
				#card_no = user.card.card_number
				amount = autopay.amount
				account_to = autopay.account_to
				if(user.card.credited_amount + float(amount) > maxCreditLimit(user.card.card_type)):
					return HttpResponse(str(user.card.credited_amount + float(amount)) + "ERROR: credit limit exceeded ")
				payToAccount(user.user_name, user.password, user.card.card_number, account_to, "autopay", amount)
				user.card.credited_amount += float(amount)
				user.card.save()
				date = datetime.datetime.now()
				generateStatement(user.card, date, amount, 'Autopay')

def payBill(request):
	amount = request.POST['pay_amount']
	USER = request.session['USER']
	USER.card.credited_amount -= float(amount)
	USER.card.save()
	return HttpResponseRedirect('services.html')
	
def autopay(request):
	card_number = request.POST['card_number']
	account_no = request.POST['account_no']
	amount = request.POST['amount']
	description = request.POST['description']
	date = request.POST['date']
	y = int(date[0:4])
	m = int(date[5:7])
	d = int(date[8:10])
	date = datetime.datetime(y, m, d)
	installment = request.POST['installment']
	USER = request.session['USER']
	try:
		Card.objects.get(card_number=card_number)
	except (KeyError, Card.DoesNotExist):
		return HttpResponse("ERROR: Incorrect Card Number ")
	else:
		a = Autopay(to_account=account_no, description=description, date=date, amount=amount, installment=installment, user=USER)				
		a.save()
		return HttpResponseRedirect('services.html')
	
def removeAutopay(request, remove_id):
	a = Autopay(id=remove_id)
	a.delete()
	return HttpResponseRedirect('/creditcard/user/services.html')
		
def userPayToAccount(request):
	"""
	Function is the basic API for the credit card system.
	Arguments: request
	user_name -- Name of user as in credit card system
	password -- Four digit pin code of user
	card_number -- Card number of Card given to user.
	account_number -- Account to which amount is to be transfered
	amount -- Amount of money to transfer
	description -- Remark provided by user
	"""
	user_name = request.POST['user_name']
	password = request.POST['password']
	card_number = request.POST['card_number']
	account_number = request.POST['account_number']
	description = request.POST['description']
	amount = request.POST['amount']	
	code = payToAccount(user_name, password, card_number, account_number, description, amount)
	if(code == 'noUser'):
		return HttpResponse("ERROR: user does not exits ")
	elif(code == 'limitExceeded'):
		USER = User.objects.get(user_name=user_name, password=password)
		return HttpResponse(str(USER.card.credited_amount + float(amount)) + "ERROR: credit limit exceeded ")
	else:
		return HttpResponseRedirect('transfer.html')

def payToAccount(user_name, password, card_number, account_number, description, amount):
	try:
		USER = User.objects.get(user_name=user_name, password=password)
		CARD = Card.objects.get(card_number=card_number)
	except (KeyError, User.DoesNotExist):
		return 'noUser'
	else:
		if(USER.card.credited_amount + float(amount) > maxCreditLimit(USER.card.card_type)):
			return 'limitExceeded'
		USER.card.credited_amount += float(amount)
		USER.card.save()
		#Using Account API add amount to the given account number
		date = datetime.datetime.now()
		generateStatement(CARD, date, amount, description)
		sendSms(USER.personaldetail.mobile, "Your credit card account " + str(USER.bankdetail.account_number) + " credited INR " + str(amount) + " on " + str(date))
		return 'success'

def generateStatement(CARD, date, amount, description):
	"""
	Function is used to save user statements of transaction.
	 
	@type CARD: Object
	@param CARD: Object of Card class 
	@type date: date 
	@param date: Date of Transaction
	@type amount: Number 
	@param amount: Amount of the statement
	@type description: text 
	@param description: Remarks of transaction
	"""
	transaction_id = str(datetime.datetime.now())
	s = Statement(transaction_date=date, amount=amount, transaction_id=transaction_id , description=description, card=CARD)
	s.save()

def displayStatement(request):	
	"""
	Function is used to display statement
	
	Arguments: request
	
	@type card_number: number 
	@param card_number: Card Number of user Credit Card
	@type from_date: date 
	@param from_date: Date after which statements are to be displayed
	@type to_date: date 
	@param to_date: Date from which statements are to be displayed
	
	It appends statements to list of statements.
	"""
	card_number = request.POST['card_number']
	date_from = request.POST['from_date']
	y = int(date_from[0:4])
	m = int(date_from[5:7])
	d = int(date_from[8:10])
	date_from = datetime.datetime(y, m, d)
	date_to = request.POST['to_date']
	y = int(date_to[0:4])
	m = int(date_to[5:7])
	d = int(date_to[8:10])
	date_to = datetime.datetime(y, m, d)
	CARD = Card.objects.get(card_number=card_number)
	list_of_statement = []
	for statement in CARD.statement_set.all():
		date = statement.transaction_date
		if((date >= date_from) & (date <= date_to)):
			list_of_statement.append(statement) 
	return render_to_response('user/successstatement.html', {'list_of_statement': list_of_statement})

def login(request):
	"""
	Function is used to verify user at time of login and store session variable
	@type username: text
	@param username: Username of User
	@type password: password
	@param password: Password of User    
	"""
	if request.method != 'POST':
		raise Http404('Only POSTs are allowed')
	ld_uname = request.POST['username']
	ld_pswd = request.POST['password']
	try:
		USER = User.objects.get(user_name=ld_uname, password=ld_pswd)
		request.session['USER'] = USER 
	except (KeyError, User.DoesNotExist):
		return HttpResponseRedirect('/creditcard/home/userDoesNotExist/')
	else:
		return HttpResponseRedirect('/creditcard/user/index.html')
	
def userDoesNotExist(request):
	"""
	Redirects to home page if user does not exists
	"""
	return render_to_response('home/index.html', {'Error':"The User Name or Password you entered is incorrect."}, context_instance=RequestContext(request))
	
def logout(request):
	"""
	Function logout from user session by deleting the session variable.
	"""
	try:
		del request.session['USER']
	except KeyError:
		pass
	return HttpResponseRedirect('/creditcard/home/index.html')
	
def userNameExistError(request):
	"""
	Returns to home page if user name already exists
	"""
	return render_to_response('register/index.html', {'Error':"User Name already exists please try a different username"}, context_instance=RequestContext(request))

def registerprocess(request):
	""" 
	It process the register process of user.
	It takes all fields from user and save them to the database.
	"""
	
	try:
		ld_uname = request.POST['USER_NAME']
		try:
			USER = User.objects.get(user_name=ld_uname)
		except (KeyError, User.DoesNotExist):
			
			ld_pswd = request.POST['PASSWORD']
			pd_firstname = request.POST['FIRST_NAME']
			pd_lastname = request.POST['LAST_NAME']
			pd_gender = request.POST['GENDER']
			pd_education = request.POST['EDUCATION']
			pd_fathername = request.POST['FATHER_NAME']
			pd_mothername = request.POST['MOTHER_NAME']
			pd_currentaddress = request.POST['CURRENT_ADDRESS']
			pd_city = request.POST['PD_CITY']
			pd_pincode = request.POST['PD_PINCODE']
			pd_permanentaddress = request.POST['PERMANENT_ADDRESS']
			pd_telephone = request.POST['TELEPHONE']
			pd_mobile = request.POST['MOBILE']
			ed_companytype = request.POST['COMPANY_TYPE']
			ed_designation = request.POST['DESIGNATION']
			ed_income = request.POST['INCOME']
			ed_workyears = request.POST['WORK_YEARS']
			ed_name = request.POST['NAME']
			ed_officeaddress = request.POST['OFFICE_ADDRESS']
			ed_city = request.POST['ED_CITY']
			ed_pincode = request.POST['ED_PINCODE']
			ed_emailid = request.POST['EMAIL_ID']
			bd_account_number = request.POST['ACCOUNT_NUMBER']
			bd_bankname = request.POST['BANK_NAME']
			bd_branch_address = request.POST['BRANCH_ADDRESS']
			bd_account_type = request.POST['ACCOUNT_TYPE']
			cd_cardtype = request.POST['CARD_TYPE']
			card_number = random.randint(10 ** 16, 10 ** 17)
		else:	
			return HttpResponseRedirect('/creditcard/register/userNameExistError/')
	except (KeyError):
		return HttpResponse("ERROR ")
	else:
		USER = User.objects.create(user_name=ld_uname, password=ld_pswd, verification_flag='Not Verified')
		USER.save()
		pd = PersonalDetail(first_name=pd_firstname, last_name=pd_lastname, gender=pd_gender, education=pd_education, father_name=pd_fathername, mother_name=pd_mothername, current_address=pd_currentaddress, city=pd_city, pincode=pd_pincode, permanent_address=pd_permanentaddress, telephone=pd_telephone, mobile=pd_mobile, user=USER)				
		pd.save()
		ed = EmploymentDetail(company_type=ed_companytype, designation=ed_designation, income=ed_income, work_years=ed_workyears, name=ed_name, office_address=ed_officeaddress, city=ed_city, pincode=ed_pincode, email_id=ed_emailid, user=USER)
		ed.save()
		bd = BankDetail(account_number=bd_account_number, bankname=bd_bankname, branch_address=bd_branch_address, account_type=bd_account_type, user=USER)
		bd.save()
		cd = Card(card_type=cd_cardtype, interest=interest(cd_cardtype), credited_amount=0, user=USER, card_number=card_number)	
		cd.save()		
		return HttpResponseRedirect('/creditcard/home/registeredSuccessfully/')
		
def registeredSuccessfully(request):
	"""
	
	"""
	return render_to_response('home/index.html', {'Error':"You are successfully registered and ready for first time login"}, context_instance=RequestContext(request))
	
def sendSms(number, message):
	"""
	Function is used to send message to phone number using free api from provider way2sms.
	"""
	#number = unicodedata.normalize('NFKD', number).encode('ascii', 'ignore')
	urllib.urlopen('http://ubaid.tk/sms/sms.aspx?uid=9478017939&pwd=4321&phone=' + number + '&msg=' + message + '&provider=way2sms').read()
	
def index(request):
	"""Render home page of the website """
	return render_to_response('home/index.html', context_instance=RequestContext(request))
	
def cards(request):
	"""Render cards page of the website """
	return render_to_response('home/cards.html', context_instance=RequestContext(request))

def services(request):
	"""Render services page of the website """
	return render_to_response('home/services.html', context_instance=RequestContext(request))
	
def userservices(request):
	"""Render user services page of the website """
	user = request.session['USER']
	list_of_autopay = []
	for auto in user.autopay_set.all():
		list_of_autopay.append(auto)
	return render_to_response('user/services.html', {'list_of_autopay': list_of_autopay} , context_instance=RequestContext(request))
	
def contact(request):
	"""Render contact page of the website """
	return render_to_response('home/contactus.html', context_instance=RequestContext(request))
	
def sitemap(request):
	"""Render sitemap page of the website """
	return render_to_response('home/services.html', context_instance=RequestContext(request))

def platinum(request):
	"""Render platinum card page of the website """
	return render_to_response('home/platinum.html', context_instance=RequestContext(request))

def gold(request):
	"""Render gold page of the website """
	return render_to_response('home/gold.html', context_instance=RequestContext(request))

def silver(request):
	"""Render silver page of the website """
	return render_to_response('home/silver.html', context_instance=RequestContext(request))
	
def register(request):
	"""Render register page of the website """
	return render_to_response('register/index.html', context_instance=RequestContext(request))

def userindex(request):
	"""Render user home page of the website """
	try:
		request.session['USER']
	except (KeyError):
		return HttpResponseRedirect('/creditcard/home/index.html')
	else:
		return render_to_response('user/index.html', context_instance=RequestContext(request))
	
def userprofile(request):
	"""Render user profile page of the website """
	try:
		request.session['USER']
	except (KeyError):
		return HttpResponseRedirect('/creditcard/home/index.html')
	else:
		return render_to_response('user/profile.html', context_instance=RequestContext(request))

def userstatement(request):
	"""Render statement page of the website """
	try:
		request.session['USER']
	except (KeyError):
		return HttpResponseRedirect('/creditcard/home/index.html')
	else:
		return render_to_response('user/statement.html', context_instance=RequestContext(request))

def usertransfer(request):
	"""Render transfer page of the website """
	try:
		request.session['USER']
	except (KeyError):
		return HttpResponseRedirect('/creditcard/home/index.html')
	else:
		return render_to_response('user/transfer.html', context_instance=RequestContext(request))
