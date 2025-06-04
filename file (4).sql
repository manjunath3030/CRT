#create
create table sales
(
Slno int, product_id varchar(200), product_name varchar(200), quality int,category varchar(100));
#insert
insert into sales(slno, product_id, product_name, quality, category)
values(1, "3456", "mobile",1, "electronic"),
(2,"3458", "t.v",1,"electronic"),
(3,"3459","bike",2,"automobile");
#update
update sales
set quality=30
where product_id="3458";
#select
select *from sales
where slno=2;