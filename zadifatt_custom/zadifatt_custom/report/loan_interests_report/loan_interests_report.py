# Copyright (c) 2023, Billy Adwar && OdukTech Limited and contributors
# For license information, please see license.txt


import frappe

def execute(filters=None):
	columns = []
	data = get_data(filters)
	return columns, data

def get_data(filters):
	from_date, to_date = filters.get('from_date'),filters.get('to_date')
	conditions ="1=1"

	if(filters.get('status')):
		conditions += f"AND status='{filters.get('status')}' "

	if (filters.get('name')):
		conditions += f"AND loan='{filters.get('name')}'"

	if (filters.get('applicant')):
		conditions  += f"AND applicant ='{filters.get('applicant')}'"
		

	query = f""" SELECT name,applicant,loan_type, disbursed_amount, repayment_start_date,total_payment, total_amount_paid,status AS loan_status, 
				(total_payment-total_amount_paid) AS payment_balance FROM `tabLoan` WHERE         
				status IN ('Disbursed','Closed') GROUP BY applicant"""