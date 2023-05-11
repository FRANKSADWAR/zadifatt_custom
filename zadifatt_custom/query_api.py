"""
Custom API's and server scripts for Zadifatt Loan Management
"""

import frappe
## This filter makes sure that one cannot be a loan quarantor if they have not yet cleared their loans
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def filter_defaulted_customers(doctype, txt, searchfield, start, page_len, filters):
    mid_section_query = ""
    query = f"""
            SELECT applicant FROM `tabLoan` WHERE "1=1" AND status <> 'Sanctioned' {mid_section_query}
	        GROUP BY applicant HAVING (CAST(SUM(total_payment) - SUM(total_amount_paid) AS decimal) <= CAST(0 AS decimal));
            """
    if filters and filters.get("customer_name"):
	    mid_section_query += " AND applicant <> {customer_name}".format(
	        customer_name=frappe.db.escape(filters.get("customer_name")))
        
    return frappe.db.sql(query, filters)      