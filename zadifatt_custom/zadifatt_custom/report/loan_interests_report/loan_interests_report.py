# Copyright (c) 2023, Billy Adwar && OdukTech Limited and contributors
# For license information, please see license.txt


import frappe

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_data(filters):
	from_date, to_date = filters.get('from_date'),filters.get('to_date')
	conditions ="1=1"

	if(filters.get('status')):
		conditions += f"AND status='{filters.get('status')}' "

	if (filters.get('name')):
		conditions += f"AND name='{filters.get('name')}'"

	if (filters.get('applicant')):
		conditions  += f"AND applicant ='{filters.get('applicant')}'"

	if filters.get('from_date') > filters.get('to_date'):
		frappe.throw("From date cannot be greater than to date {}".format(filters.get('to_date')))
	query = f"""
				select applicant AS Customer, sum(disbursed_amount) AS `Total Disbursed Amount`, SUM(total_payment) AS `Total Payments`, SUM(total_amount_paid) AS `Total Amount Paid`,
        		(SUM(total_payment)-SUM(total_amount_paid)) AS `Payment Balance` FROM tabLoan WHERE {conditions} AND status <> 'Sanctioned' AND (disbursement_date BETWEEN 
				'{from_date}' AND '{to_date}') GROUP BY applicant;
				"""
	
	data = frappe.db.sql(query)

	return data

def get_columns():
	return [
		"Customer:Link:100",
		"Total Disbursed Amount:Currency:100",
		"Total Payments:Currency:100",
		"Total Amount Paid:Currency:100",
		"Payment Balance:Currency:100"
	]

