
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from BankCreditCard.creditcard.models import User, Card, Statement, BankDetail, EmploymentDetail, PersonalDetail
import random
import datetime

def max_credit_limit(card_type):
	if(card_type == 'Platinum'):
		return 10000
	elif(card_type == 'Gold'):
		return 5000
	elif(card_type == 'Silver'):
		return 2000	
	
def pay_to_account(request):
	user_name = request.POST['USER_NAME']
	password = request.POST['PASSWORD']
	card_number = request.POST['CARD_NUMBER']
	account_number = request.POST['ACCOUNT_NUMBER']
	amount = request.POST['AMOUNT']	
	try:
		USR = User.objects.get(user_name=user_name, password=password)
		CARD = Card.objects.get(card_number=card_number)
	except (KeyError, User.DoesNotExist):
		return HttpResponse("ERROR: user does not exits ")
	else:
		MAX_CREDIT_LIMIT = max_credit_limit(USR.card.card_type)
		if(USR.card.credited_amount + float(amount) > MAX_CREDIT_LIMIT):
			return HttpResponse(str(USR.card.credited_amount + float(amount)) + "ERROR: credit limit exceeded ")
		USR.card.credited_amount += float(amount)
		#Using Account API add amount to the given account number
		generate_statement(CARD, amount, account_number)
		return HttpResponseRedirect('transfer.html')

def generate_statement(CARD, amount, to_account):
	transaction_id = random.randint(1000, 2000)
	stmt = Statement(transaction_date=datetime.datetime.now(), amount=amount, to_account=to_account , transaction_id=transaction_id , card=CARD)	
	stmt.save()

def display_statement(request):	
	card_number = request.POST['CARD_NUMBER']
	#date_from = request.POST['FROM_DATE']
	#date_to = request.POST['TO_DATE']
	CARD = Card.objects.get(card_number=card_number)
	list_of_statement = []
	for statement in CARD.statement_set.all():
		#date = statement.transaction_date
		#if((date >= date_from) & (date <= date_to)):
		list_of_statement.append(statement) 
	return render_to_response('user/successstatement.html', {'list_of_statement': list_of_statement})

def index(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))
	
def cards(request):
	return render_to_response('home/cards.html', context_instance=RequestContext(request))

def services(request):
	return render_to_response('home/services.html', context_instance=RequestContext(request))
	
def contact(request):
	return render_to_response('home/contact-us.html', context_instance=RequestContext(request))
	
def sitemap(request):
	return render_to_response('home/sitemap.html', context_instance=RequestContext(request))
	
def register(request):
	return render_to_response('register/index.html', context_instance=RequestContext(request))

def login(request):
	if request.method != 'POST':
		raise Http404('Only POSTs are allowed')
	ld_uname = request.POST['USER_NAME']
	ld_pswd = request.POST['PASSWORD']
	try:
		USR = User.objects.get(user_name=ld_uname, password=ld_pswd)
		request.session['USER'] = USR 
	except (KeyError, User.DoesNotExist):
		return HttpResponse("Username and Password you provide does not match, Please enter again")
	else:
		return HttpResponseRedirect('index.html')
	
def logout(request):
	try:
		del request.session['user_name']
	except KeyError:
		pass
	return HttpResponse("You're logged out.")

'''
def verify_user(request):
    ld_uname = request.POST['USER_NAME']
    ld_pswd = request.POST['PASSWORD']
    try:
        USR = User.objects.get(user_name=ld_uname, password=ld_pswd)
    except (KeyError, User.DoesNotExist):
        return HttpResponse("ERROR ")
    else:
        return render_to_response('user/index.html', {'USR': USR})
'''

def userindex(request):
	return render_to_response('user/index.html', context_instance=RequestContext(request))
	
def userprofile(request):
	return render_to_response('user/profile.html', context_instance=RequestContext(request))

def userstatement(request):
	return render_to_response('user/statement.html', context_instance=RequestContext(request))

def usertransfer(request):
	return render_to_response('user/transfer.html', context_instance=RequestContext(request))

def access_details(request, USR):	
	return render_to_response('register/success.html', {'USR': USR})	
	
def process(request):
	try:
		ld_uname = request.POST['USER_NAME']
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
	except (KeyError):
		return HttpResponse("ERROR ")
	else:
		#Code for login account app for verification of user
		usr = User.objects.create(user_name=ld_uname, password=ld_pswd, verification_flag='Not Verified')
		usr.save()
		pd = PersonalDetail(first_name=pd_firstname, last_name=pd_lastname, gender=pd_gender, education=pd_education, father_name=pd_fathername, mother_name=pd_mothername, current_address=pd_currentaddress, city=pd_city, pincode=pd_pincode, permanent_address=pd_permanentaddress, telephone=pd_telephone, mobile=pd_mobile, user=usr)				
		pd.save()
		ed = EmploymentDetail(company_type=ed_companytype, designation=ed_designation, income=ed_income, work_years=ed_workyears, name=ed_name, office_address=ed_officeaddress, city=ed_city, pincode=ed_pincode, email_id=ed_emailid, user=usr)
		ed.save()
		bd = BankDetail(account_number=bd_account_number, bankname=bd_bankname, branch_address=bd_branch_address, account_type=bd_account_type, user=usr)
		bd.save()
		cd = Card(card_type=cd_cardtype, interest=343, credited_amount=9078, user=usr, card_number=card_number)	
		cd.save()		
		return render_to_response('register/success.html', {'USR': usr})
		

				
