## Zadifatt Custom
> Custom reports to get the customer's loan payment balance from Loan Management
> Filtering the customers using a custom query which gets only the customers who have completed their loan arrears as guarantors
i.e a customer cannot be a guarantor if they have not cleared their loans
> Hooks applied for fixtures to capture custom fields and for custom doctype.js
Custom reports for loan management system
###
> Custom DocTypes i.e Guarantors, and child DocTypes i.e Loan Guarantors and Customer Guarantors used in Table MultiSelect field
### Installation

```
bench get-app https://github.com/FRANKSADWAR/zadifatt_custom.git
```

```
bench --site [site_name] install-app zadifatt_custom
```

```
bench restart
```

 #### License

MIT