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

	
	
	query_2 = f"""
				select applicant, sum(disbursed_amount) AS `Total Disbursed Amount`, SUM(total_payment) AS `Total Payments`, SUM(total_amount_paid) AS `Total Amount Paid`,
        		(SUM(total_payment)-SUM(total_amount_paid)) AS `Payment Balance` FROM tabLoan WHERE status <> 'Sanctioned' AND (disbursement_date BETWEEN 
				'{from_date}' AND '{to_date}') GROUP BY applicant;

				
				"""