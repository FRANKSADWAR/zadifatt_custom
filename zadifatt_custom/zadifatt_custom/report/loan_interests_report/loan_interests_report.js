// Copyright (c) 2023, Billy Adwar && OdukTech Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Loan Interests Report"] = {
	"filters": [
		{
			fieldname: 'applicant',
			label: __('Applicant'),
			fieldtype: 'Link',
			reqd: 0,
			width: 100
		},
		{
			fieldname: 'loan_application',
			label: __('Loan Application'),
			fieldtype: 'Link',
			width: 100

		},
		{
			fieldname: 'status',
			label: __('Status'),
			fieldtype: 'Select',
			default: 'Disbursed',
			width: 50
		},
		{
			fieldname: 'start_date',
			label: __('Start Date'),
			fieldtype: 'Date',
			default: frappe.datetime.add_months(frappe.datetime.get_today(),-1),
			width: 80
		},
		{
			fieldname: 'to_date',
			label: __('To Date'),
			fieldtype: 'Date',
			default: frappe.datetime.get_today(),
			width: 80
		}
	]
};
