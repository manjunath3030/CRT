#create
create table sales
(
Slno int, product_id varchar(200), product_name varchar(200), quality int,categoty varchar(100));
#insert
insert into sales(slno, product_id, product_name, quality, categoty)
values(1, "3456", "mobile",1, "electronic"),
(2,"3458", "t.v",1,"electronic"),
(3,"3459","bike",2,"automobile");
#select
select * from sales
#drop

