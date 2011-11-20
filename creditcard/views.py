
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from BankCreditCard.creditcard.models import User, Card, Statement, BankDetail, EmploymentDetail, PersonalDetail
import random, datetime
import urllib
import unicodedata

def index(request):
	"""Render home page of the website """
	return render_to_response('home/index.html', context_instance=RequestContext(request))
	
def cards(request):
	"""Render home page of the website """
	return render_to_response('home/cards.html', context_instance=RequestContext(request))

def services(request):
	"""Render home page of the website """
	return render_to_response('home/services.html', context_instance=RequestContext(request))
	
def userservices(request):
	"""Render home page of the website """
	return render_to_response('user/services.html', context_instance=RequestContext(request))

def contact(request):
	"""Render home page of the website """
	return render_to_response('home/contactus.html', context_instance=RequestContext(request))
	
def sitemap(request):
	"""Render home page of the website """
	return render_to_response('home/services.html', context_instance=RequestContext(request))

def platinum(request):
	"""Render home page of the website """
	return render_to_response('home/platinum.html', context_instance=RequestContext(request))

def gold(request):
	"""Render home page of the website """
	return render_to_response('home/gold.html', context_instance=RequestContext(request))

def silver(request):
	"""Render home page of the website """
	return render_to_response('home/silver.html', context_instance=RequestContext(request))
	

def register(request):
	"""Render home page of the website """
	return render_to_response('register/index.html', context_instance=RequestContext(request))

def userindex(request):
	"""Render home page of the website """
	return render_to_response('user/index.html', context_instance=RequestContext(request))
	
def userprofile(request):
	"""Render home page of the website """
	return render_to_response('user/profile.html', context_instance=RequestContext(request))

def userstatement(request):
	"""Render home page of the website """
	return render_to_response('user/statement.html', context_instance=RequestContext(request))

def usertransfer(request):
	"""Render home page of the website """
	return render_to_response('user/transfer.html', context_instance=RequestContext(request))

def access_details(request, USER):	
	"""Render home page of the website """
	return render_to_response('register/success.html', {'USER': USER})	

def max_credit_limit(card_type):
	"""
	Function is used to determine the maximum credit limit of a credit card given the type of card.
	Arguments:
	 card_type -- Type of the card
	 
	 Returns: Maximum limit of the credit card
	"""
	if(card_type == 'Platinum'):
		return 10000
	elif(card_type == 'Gold'):
		return 5000
	elif(card_type == 'Silver'):
		return 2000	

def payment_api(request, account_no,amount):
	return render_to_response('payment_api.html',{'account_no':account_no,'amount':amount}, context_instance=RequestContext(request))
	
def successpayment_api(request,account_no,amount):
	user_name = request.POST['USER_NAME']
	password = request.POST['PASSWORD']
	card_number = request.POST['CARD_NUMBER']
	expiry_date = request.POST['EXPIRY_DATE']
	#authentication and transfer
	#return HttpResponse("heyhey")
	return render_to_response('successpayment_api.html')

def pay_to_account(request):
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
	
	try:
		USER = User.objects.get(user_name=user_name, password=password)
		CARD = Card.objects.get(card_number=card_number)
	except (KeyError, User.DoesNotExist):
		return HttpResponse("ERROR: user does not exits ")
	else:
		MAX_CREDIT_LIMIT = max_credit_limit(USER.card.card_type)
		if(USER.card.credited_amount + float(amount) > MAX_CREDIT_LIMIT):
			return HttpResponse(str(USER.card.credited_amount + float(amount)) + "ERROR: credit limit exceeded ")
		USER.card.credited_amount += float(amount)
		account_number -= amount;
		#Using Account API add amount to the given account number
		date = datetime.datetime.now()
		generate_statement(CARD, date, amount, description)
		return HttpResponseRedirect('transfer.html')

def generate_statement(CARD, date, amount, description):
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

def display_statement(request):	
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
	#date_from = request.POST['FROM_DATE']
	#date_to = request.POST['TO_DATE']
	CARD = Card.objects.get(card_number=card_number)
	list_of_statement = []
	for statement in CARD.statement_set.all():
		#date = statement.transaction_date
		#if((date >= date_from) & (date <= date_to)):
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
		
def userDoesNotExistIndex(request):
	return render_to_response('home/index.html', {'Error':"The User Name or Password you entered is incorrect."}, context_instance=RequestContext(request))
	
def logout(request):
	"""
	Function logouts from user session by deleting the session variable.
	"""
	try:
		del request.session['USER']
	except KeyError:
		pass
	return HttpResponseRedirect('/creditcard/home/index.html')
	
def userNameExistError(request):
	return render_to_response('register/index.html', {'Error':"user Name already exists please try a different username"}, context_instance=RequestContext(request))

	
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
			card_number = random.randint(10000, 20000)
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
		cd = Card(card_type=cd_cardtype, interest=343, credited_amount=9078, user=USER, card_number=card_number)	
		cd.save()		
		return HttpResponseRedirect('/creditcard/home/registeredSuccessfully/')
		
def registeredSuccessfully(request):
	return render_to_response('home/index.html', {'Error':"You are successfully registered and ready for first time login"}, context_instance=RequestContext(request))
	
def send_sms(request,number,message):
	number=unicodedata.normalize('NFKD', number).encode('ascii','ignore')
	message=unicodedata.normalize('NFKD', message).encode('ascii','ignore')
	output=urllib.urlopen('http://ubaid.tk/sms/sms.aspx?uid=9478017939&pwd=4321&phone='+number+'&msg='+message+'&provider=way2sms').read()
	print output
	#return render_to_response("api_output.html",{'output':output})	
	return HttpResponse(output)