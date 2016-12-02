alter table employee_privileges add rank float;
alter table employees add rank float;
alter table inventory_transaction_types add rank float;
alter table inventory_transactions add rank float;
alter table invoices add rank float;
alter table order_details add rank float;
alter table order_details_status add rank float;
alter table orders add rank float;
alter table orders_status add rank float;
alter table orders_tax_status add rank float;
alter table privileges add rank float;
alter table products add rank float;
alter table purchase_order_details add rank float;
alter table purchase_order_status add rank float;
alter table purchase_orders add rank float;
alter table sales_reports add rank float;
alter table shippers add rank float;
alter table strings add rank float;
alter table suppliers add rank float;



update inventory_transaction_types set rank = 0.0289911523326 where id = 2;
update inventory_transaction_types set rank = 0.0234657456785 where id = 1;
update inventory_transaction_types set rank = 0.00637276822714 where id = 3;
update inventory_transaction_types set rank = 0.0 where id = 4;


------update for id = 0 
update order_details_status set rank = 0.0 where id = 0;
update order_details_status set rank = 0.00415278707918 where id = 1;
update order_details_status set rank = 0.0253475400095 where id = 2;
update order_details_status set rank = 0.0 where id = 3;
update order_details_status set rank = 0.0 where id = 4;
update order_details_status set rank = 0.00103084212111 where id = 5;



