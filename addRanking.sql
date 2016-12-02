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


update inventory_transaction_types set rank = 0.0173632394269 where id = 2;
update inventory_transaction_types set rank = 0.015597512857 where id = 1;
update inventory_transaction_types set rank = 0.00389041964906 where id = 3;
update inventory_transaction_types set rank = 0.0 where id = 4;



update order_details_status set rank = 0.000935893833019 where id = 0;
update order_details_status set rank = 0.003408593277 where id = 1;
update order_details_status set rank = 0.0211631055791 where id = 2;
update order_details_status set rank = 0.0 where id = 3;
update order_details_status set rank = 0.0 where id = 4;
update order_details_status set rank = 0.000911072143058 where id = 5;

purchase_orders-148            :
purchase_orders-105            :
purchase_orders-106            :
purchase_orders-94             :
update purchase_orders set rank = 0.0036243349427 where id = 90;
update purchase_orders set rank = 0.00501258082165 where id = 91;
update purchase_orders set rank = 0.00784183543681 where id = 92;
update purchase_orders set rank = 0.00294266023579 where id = 93;
update purchase_orders set rank = 0.00206887522443 where id = 94;
update purchase_orders set rank = 0.00231103707729 where id = 95;
update purchase_orders set rank = 0.002296347336 where id = 96;
update purchase_orders set rank = where id = 97;
update purchase_orders set rank = where id = 98;
update purchase_orders set rank = where id = 99;
update purchase_orders set rank = where id = 100;
update purchase_orders set rank = where id = 101;
update purchase_orders set rank = where id = 102;
update purchase_orders set rank = where id = 103;
update purchase_orders set rank = where id = 104;
update purchase_orders set rank = 0.00208983032477 where id = 105;
update purchase_orders set rank = 0.00210183208565 where id = 106;
update purchase_orders set rank = where id = 107;
update purchase_orders set rank = where id = 108;
update purchase_orders set rank = where id = 109;
update purchase_orders set rank = where id = 110;
update purchase_orders set rank = where id = 111;
update purchase_orders set rank = 0.00236049528971 where id = 140;
update purchase_orders set rank = 0.00231060315641 where id = 141;
update purchase_orders set rank = 0.00231013777864 where id = 142;
update purchase_orders set rank = 0.00257138554095 where id = 146;
update purchase_orders set rank = 0.0025216213459 where id = 147;
update purchase_orders set rank = 0.0022191167196 where id = 148;

