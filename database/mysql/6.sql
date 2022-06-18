use demo;
create table student(
	id varchar(20) primary key not null,
    nam varchar(10),
    age int,
    depart varchar(30)
    );
create table course (
	cid varchar(15) primary key not null,
    nam varchar(30),
    befor varchar(15)
    );
create table choose(
	id varchar(20),
    cid varchar(30),
    score dec(5,2)
    );
insert into demo.student(id,nam,age,depart)
values
	('00001','张三',20,'计算机系'),
    ('00002','李四',19,'计算机系'),
    ('00003','王五',21,'计算机系')
    ;

insert into demo.course (cid,nam,befor)
values
	('c1','计算机引论',''),
    ('c2','Pascal语言','c1'),
    ('c3','数据结构','c2')
;

insert into demo.choose(id,cid,score)
values
	('00001','c1','95'),
    ('00001','c2','80'),
    ('00001','c3','84'),
    ('00002','c1','80'),
    ('00002','c2','85'),
    ('00003','c1','78'),
    ('00003','c3','70')
;

select id,nam 
from student 
where depart='计算机系';

select student.id,choose.score
from student,choose
where student.id=choose.id and choose.cid='c1' and choose.score<(
select choose.score from student,choose where student.nam='张三' and student.id=choose.id and choose.cid='c1');

select choose.id
from choose
where choose.cid='c2' and id in(
select choose.id from choose where choose.cid='c3');