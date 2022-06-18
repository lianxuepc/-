create user 'dcl'@'localhost' identified by 'dcl';

grant all privileges 
on *.*
to 'dcl'@'localhost';

show grants for 'dcl'@'localhost';

create database dcldemo;

use dcldemo;
create table abc(
	a1 varchar(20) primary key not null,
    b2 dec(4,2),
    c3 int
    );
insert into abc 
values
('dcl测试','90.5',30);
 
 
 revoke all privileges
on *.*
from 'dcl'@'localhost';